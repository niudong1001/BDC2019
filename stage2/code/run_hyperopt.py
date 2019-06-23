'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-07 22:12:50
@LastEditTime: 2019-06-23 20:51:59
'''
import os
import json
import sys
import time
import pickle
import numpy as np
import pandas as pd
from .config import GLOBAL_DIR, K_FOLD, OUTPUT_DIR, OUTPUT_TRAIN_DIR, OUTPUT_TEST_DIR
sys.path.append(GLOBAL_DIR)
# https://www.jianshu.com/p/35eed1567463
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
# from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from .models import LigthGBM_GBDT, LigthGBM_DART
from helper import Timer, MyEncoder, OFFLINE, CalQAuc, CAL_Q_AUC
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.linear_model import LogisticRegression

if OFFLINE:
    feature_names_file = "stage2/input/debug_feature_names.csv"
else:
    feature_names_file = "stage2/input/online_feature_names.csv"


X, y, test_X, q_auc_cal, feature_names = None, None, None, None, None
model_map = {
    'lgb_dart': LigthGBM_DART,
    'lgb_gbdt': LigthGBM_GBDT,
    # 'sklearn_rf': Sklearn_RF,
    # 'torch_nn': Torch_DNN
}


def LoadDataset(in_train_feature, in_train_label, in_test_feature=None, in_q_auc_cal=None):

    global X, y, test_X, q_auc_cal, feature_names

    def _load_train():
        X = np.load(in_train_feature)
        y = np.load(in_train_label)
        return X, y

    def _load_test():
        X = np.load(in_test_feature)
        return X
    
    X, y =  _load_train()
    if not OFFLINE:
        test_X = _load_test()
    
    if CAL_Q_AUC:
        q_auc_cal = np.load(in_q_auc_cal)
    
    feature_names = list(pd.read_csv(feature_names_file, sep=",").columns.values)
    print("Feature names:", feature_names) 

    print("X:", X.shape, X[:2])
    print("y:", y.shape, y[:2])
    if not OFFLINE:
        print("Test x:", test_X.shape, test_X[:2])
    if CAL_Q_AUC:
        print("Cal q auc:", q_auc_cal.shape, q_auc_cal[:2])


def fn(params):

    model_name = params.pop('model')
    model = model_map[model_name](**params)
    
    print(json.dumps(params, indent=1))
    global X, y, test_X, q_auc_cal, feature_names

    # Train 
    losses, aucs = [], []
    train_predicts = np.empty_like(y).astype(float)
    # 分层采样，确保训练集，测试集中各类别样本的比例与原始数据集中相同
    stratified_folder = StratifiedKFold(
        n_splits=K_FOLD, 
        random_state=0, 
        shuffle=False
    )
    for train_index, valid_index in stratified_folder.split(X, y):
        train_X, train_y = X[train_index], y[train_index]
        valid_X, valid_y = X[valid_index], y[valid_index]
        loss = model.fit(train_X, train_y, valid_X, valid_y)
        losses.extend(loss)
        train_predicts[valid_index] = model.predict(valid_X)
    
    importance_df = pd.DataFrame({
        'column': feature_names,
        'importance': model.bst.feature_importance(),
    }).sort_values(by='importance', ascending=False)
    
    print("feature importance:", importance_df)
    
    timestamp = int(time.time())
    mean, std = np.mean(losses), np.std(losses)
    total_auc = roc_auc_score(y, train_predicts)
    print("Valid Loss, AUC: {} {}".format(round(mean, 6), round(total_auc, 6)))
    if CAL_Q_AUC:
        q_auc_df = pd.DataFrame({
            "query_id": q_auc_cal[:, 0],
            "label": q_auc_cal[:, 1],
            "prediction": train_predicts
        })
        with Timer("cal q auc"):
            q_auc_res = CalQAuc(q_auc_df)
            print("Valid Q AUC: {}".format(q_auc_res))
    filename = '%s_%d_auc%f_loss%f_std%f.npy' % (model_name, timestamp, round(total_auc, 6), 
        round(mean, 6), round(std, 6))
    np.save(os.path.join(OUTPUT_TRAIN_DIR, filename), train_predicts)
    print("Saved train results to {}".format(os.path.join(OUTPUT_TRAIN_DIR, filename)))

    # Test
    if not OFFLINE:
        model.fit(X, y)
        test_predicts = model.predict(test_X)
        np.save(os.path.join(OUTPUT_TEST_DIR, filename), test_predicts)
        print("Saved test results to {}".format(os.path.join(OUTPUT_TEST_DIR, filename)))
    
    res = {
        'loss': mean,
        "auc": total_auc,  # 整体valid算auc
        'loss_variance': std,
        'status': STATUS_OK,
        'file_name': filename,
        "importance": np.array(importance_df)
    }
    if CAL_Q_AUC:
        res["q_auc"] = q_auc_res
        
    return res


def run_lgb_gbdt(comment, eval_num=5):
    trials = Trials()
    search_space = {
        'model': 'lgb_gbdt',
        'num_threads':4,
        'num_leaves': hp.quniform('num_leaves', 5, 30, 5),
        'min_data_in_leaf': hp.quniform('min_data_in_leaf', 10, 50, 10),
        'feature_fraction': hp.quniform('feature_fraction', 0.6, 1.0, 0.1),
        'bagging_fraction': hp.quniform('bagging_fraction', 0.6, 1.0, 0.1),
        'bagging_freq': hp.quniform('bagging_freq', 0, 10, 2),
        'max_bin': hp.choice('max_bin', [15, 63, 255, 1023]),
        'learning_rate': hp.quniform('learning_rate', 0.1, 0.2, 0.01),
        'num_iterations': hp.quniform('num_iterations', 50, 200, 25)
    }
    best_param = fmin(fn, space=search_space,
                        algo=tpe.suggest,
                        max_evals=eval_num,
                        trials=trials)

    info = trials.best_trial
    info['param'] = best_param
    
    loss = round(info["result"]["loss"], 4)

    if OFFLINE:
        mode = "debug"
    else:
        mode = "online"

    json.dump(info, open(OUTPUT_DIR+'lgb_gbdt_{}_{}_{}_{}.json'.format(mode, comment, loss, int(time.time())),'w'),
        indent=1, cls=MyEncoder)


def run_lr():
    # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
    model = LogisticRegression(C=5, solver="liblinear")
    
    global X, y, test_X, q_auc_cal

    # Train 
    losses, aucs = [], []
    train_predicts = np.empty_like(y).astype(float)
    # 分层采样，确保训练集，测试集中各类别样本的比例与原始数据集中相同
    stratified_folder = StratifiedKFold(
        n_splits=K_FOLD, 
        random_state=0, 
        shuffle=False
    )
    for train_index, valid_index in stratified_folder.split(X, y):
        train_X, train_y = X[train_index], y[train_index]
        valid_X, valid_y = X[valid_index], y[valid_index]
        model.fit(train_X, train_y)
        train_predicts[valid_index] = model.predict_proba(valid_X)[:, 1]
        loss = log_loss(y[valid_index], train_predicts[valid_index])
        losses.append(loss)
    timestamp = int(time.time())
    mean, std = np.mean(losses), np.std(losses)
    total_auc = roc_auc_score(y, train_predicts)
    print("Valid Loss, AUC: {} {}".format(round(mean, 6), round(total_auc, 6)))
    if CAL_Q_AUC:
        q_auc_df = pd.DataFrame({
            "query_id": q_auc_cal[:, 0],
            "label": q_auc_cal[:, 1],
            "prediction": train_predicts
        })
        with Timer("cal q auc"):
            q_auc_res = CalQAuc(q_auc_df)
            print("Valid Q AUC: {}".format(q_auc_res))