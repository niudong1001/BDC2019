'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-07 22:12:50
@LastEditTime: 2019-07-12 23:32:38
'''
import os
import json
import sys
import time
import pickle
import numpy as np
import pandas as pd
from .config import K_FOLD, UTILS_DIR, RES_TRAIN_OUT, RES_TEST_OUT, RES_OUT
sys.path.append(UTILS_DIR)
# https://www.jianshu.com/p/35eed1567463
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
# from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from .models import LigthGBM_GBDT, LigthGBM_DART
from helper import Timer, MyEncoder, CalQAuc
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.linear_model import LogisticRegression


X, y, test_X  = None, None, None
# q_auc_data是用来辅助qauc的计算，上面有query_id, label等
feature_names, q_auc_data = None, None
model_map = {
    'lgb_dart': LigthGBM_DART,
    'lgb_gbdt': LigthGBM_GBDT,
    # 'sklearn_rf': Sklearn_RF,
    # 'torch_nn': Torch_DNN
}


def LoadDataset(in_train_feature, in_train_label, in_feature_names, in_test_feature=None, in_q_auc_data=None, verbose=True):

    global X, y, test_X, feature_names, q_auc_data

    def _load_train():
        X = np.load(in_train_feature)
        y = np.load(in_train_label)
        return X, y
    def _load_test():
        X = np.load(in_test_feature)
        return X
    def _load_feature_names():
        return list(
            pd.read_csv(
                in_feature_names, 
                sep=","
            ).columns.values
        )
    
    X, y =  _load_train()
    feature_names = _load_feature_names()
    if in_test_feature:
        test_X = _load_test()
    if in_q_auc_data:
        q_auc_data = np.load(in_q_auc_data)

    if verbose:
        print("feature names:")
        pritn(feature_names)
        print("X shape:", X.shape)
        print("X (two rows):")
        print(X[:2])
        print("y shape:", y.shape)
        print("y (two rows):")
        print(y[:2])
        if test_X:
            print("test X shape:", test_X.shape)
            print("test X (two rows):")
            print(test_X[:2])


def fn(params):

    model_name = params.pop('model')
    model = model_map[model_name](**params)
    print(json.dumps(params, indent=1))
    global X, y, test_X, q_auc_data, feature_names

    losses, aucs = [], []
    valid_predicts = np.empty_like(y).astype(float)
    # TODO: 具有时间序列关系能不能这样划分？
    stratified_folder = StratifiedKFold(
        n_splits=K_FOLD, 
        random_state=0, 
        shuffle=False
    )
    for train_index, valid_index in stratified_folder.split(X, y):
        train_X, train_y = X[train_index], y[train_index]
        valid_X, valid_y = X[valid_index], y[valid_index]
        losses.extend(model.fit(train_X, train_y, valid_X, valid_y))
        valid_predicts[valid_index] = model.predict(valid_X)
    
    importance_df = pd.DataFrame({
        'column': feature_names,
        'importance': model.bst.feature_importance(),
    }).sort_values(by='importance', ascending=False)
    
    print("feature importance:")
    print(importance_df)
    
    localtime = time.localtime(time.time())
    timestamp = time.strftime("%m%d%H%M%S", localtime)
    mean, std = round(np.mean(losses), 6), round(np.std(losses), 6)
    total_auc = round(roc_auc_score(y, valid_predicts), 6)
    print("Valid Loss, AUC: {} {}".format(mean, total_auc))
    
    if q_auc_data:
        q_auc_df = pd.DataFrame({
            "query_id": q_auc_data[:, 0],
            "label": q_auc_data[:, 1],
            "prediction": valid_predicts
        })
        with Timer("cal qauc"):
            q_auc_res = CalQAuc(q_auc_df)
            print("Valid Q AUC: {}".format(q_auc_res))
    
    filename = '%s_%d_auc%f_loss%f_std%f.npy' % (model_name, timestamp, total_auc, mean, std)
    valid_save_file = os.path.join(RES_TRAIN_OUT, filename)
    np.save(valid_save_file, valid_predicts)
    print("Saved valid results to {}".format(valid_save_file))

    if test_X:
        model.fit(X, y)
        test_predicts = model.predict(test_X)
        test_save_file = os.path.join(RES_TEST_OUT, filename)
        np.save(test_save_file, test_predicts)
        print("Saved test results to {}".format(test_save_file))
    
    res = {
        'loss': mean,
        # 整体valid算auc
        "auc": total_auc,  
        'loss_variance': std,
        'status': STATUS_OK,
        'file_name': filename,
        "importance": np.array(importance_df)
    }
    if q_auc_data:
        res["q_auc_res"] = q_auc_res
        
    return res


def run_lgb_gbdt_fast(comment):

    params = {
        "model": "lgb_gbdt",
        "num_threads": 4
    }
    info = fn(params)
    loss = info["loss"]
    
    if test_X:
        mode = "online"
    else:
        mode = "debug"

    json.dump(info, open(RES_OUT+'lgb_gbdt_{}_{}_{}_{}.json'.format(mode, comment, loss, int(time.time())),'w'),indent=1, cls=MyEncoder)


def run_lgb_gbdt(comment, eval_num=20):
    trials = Trials()
    search_space = {
        'model': 'lgb_gbdt',
        'num_threads':4,
        'num_leaves': hp.quniform('num_leaves', 20, 50, 5),
        'min_data_in_leaf': hp.quniform('min_data_in_leaf', 10, 50, 10),
        'feature_fraction': hp.quniform('feature_fraction', 0.6, 1.0, 0.1),
        'bagging_fraction': hp.quniform('bagging_fraction', 0.6, 1.0, 0.1),
        'bagging_freq': hp.quniform('bagging_freq', 0, 20, 2),
        'max_bin': hp.choice('max_bin', [63, 255, 511, 1023]),
        'learning_rate': hp.quniform('learning_rate', 0.1, 0.2, 0.01),
        'num_iterations': hp.quniform('num_iterations', 100, 200, 50)
    }
    best_param = fmin(fn, space=search_space,
                        algo=tpe.suggest,
                        max_evals=eval_num,
                        trials=trials)

    info = trials.best_trial
    info['param'] = best_param
    loss = info["result"]["loss"]

    if test_X:
        mode = "online"
    else:
        mode = "debug"

    json.dump(info, open(RES_OUT+'lgb_gbdt_{}_{}_{}_{}.json'.format(mode, comment, loss, int(time.time())),'w'),indent=1, cls=MyEncoder)