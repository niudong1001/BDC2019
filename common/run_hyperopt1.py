'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-07 22:12:50
@LastEditTime: 2019-08-09 21:02:59
'''
import os, json, sys, time, pickle
import numpy as np
import pandas as pd
# https://www.jianshu.com/p/35eed1567463
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from models import LigthGBM_GBDT, LigthGBM_DART
from config import K_FOLD, COMMON_DIR, RES_TRAIN_OUT, RES_TEST_OUT, RES_OUT
sys.path.append(COMMON_DIR)
from utils import Timer, MyEncoder, CalQAuc
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.metrics import confusion_matrix


X, y, test_X, test_y = None, None, None, None
train_qid, test_qid = None, None
feature_names = None
model_map = {
    'lgb_dart': LigthGBM_DART,
    'lgb_gbdt': LigthGBM_GBDT
}


def LoadDataset(in_train_feature, in_train_label, in_feature_names, 
    in_train_qid=None, in_test_qid=None, in_test_feature=None, 
    in_test_label=None, verbose=True):
        
    params = {
        "in_train_feature": in_train_feature,
        "in_train_label": in_train_label,
        "in_feature_names": in_feature_names,
        "in_train_qid": in_train_qid,
        "in_test_qid": in_test_qid,
        "in_test_feature": in_test_feature,
        "in_test_label":in_test_label
    }
    print(json.dumps(params, indent=1))

    global X, y, test_X, test_y, feature_names, train_qid, test_qid
    
    # 加载基础数据
    X = np.load(in_train_feature)
    y = np.load(in_train_label)
    feature_names = list(pd.read_csv(in_feature_names, sep=",").columns.values)
    
    # 加载额外数据
    if in_train_qid:
        train_qid = np.load(in_train_qid)
    if in_test_qid:
        test_qid = np.load(in_test_qid)
    if in_test_feature:
        test_X = np.load(in_test_feature)
    if in_test_label:
        test_y = np.load(in_test_label)

    if verbose:
        print("X shape:", X.shape)
        print("X (2 rows):")
        print(X[:2])
        print("y shape:", y.shape)
        print("y (10 rows):", y[:10])
        if in_test_feature:
            print("test X shape:", test_X.shape)
            print("test X (2 rows):")
            print(test_X[:2])
        if in_test_label:
            print("test y shape:", test_y.shape)
            print("test y (10 rows):")
            print(test_y[:10])
        # if in_train_qid:
        #     print("train qid shape:", train_qid.shape)
        #     print("train qid (10 rows):")
        #     print(train_qid[:10])
        # if in_test_qid:
        #     print("test qid shape:", test_qid.shape)
        #     print("test qid (10 rows):")
        #     print(test_qid[:10])


def fn(params):
    
    prefix = params.pop('prefix')
    model_name = params.pop('model')
    # 'kfold' or 'simple'
    valid_type = params.pop('valid_type')  
    cal_qauc = params.pop('cal_qauc') 
    save_result = params.pop("save_result")
    model = model_map[model_name](**params)
    print(json.dumps(params, indent=1))
    
    global X, y, test_X, test_y, feature_names, train_qid, test_qid
    
    losses, aucs = [], []
    
    if valid_type == "simple":
        total_samples = X.shape[0]
        valid_num = int(total_samples * 0.3)
        valid_indexs = np.random.choice(total_samples, valid_num)
        train_indexs = [i for i in range(total_samples) if i not in valid_indexs]
        train_X, valid_X = X[train_indexs], X[valid_indexs]
        train_y, valid_y = y[train_indexs], y[valid_indexs]
        losses.extend(model.fit(train_X, train_y, valid_X, valid_y))
        valid_predicts = model.predict(valid_X)
        total_auc = round(roc_auc_score(valid_y, valid_predicts), 6)
        C = confusion_matrix(valid_y, valid_predicts>0.5)
        print("混淆矩阵：")
        print(C)
        # total_auc = 0
    elif valid_type == "kfold":
        valid_predicts = np.empty_like(y).astype(float)
        # TODO: 具有时间序列关系能不能这样划分？
        stratified_folder = StratifiedKFold(
            n_splits=K_FOLD, 
            random_state=0, 
            shuffle=True
        )
        for train_index, valid_index in stratified_folder.split(X, y):
            train_X, train_y = X[train_index], y[train_index]
            valid_X, valid_y = X[valid_index], y[valid_index]
            losses.extend(model.fit(train_X, train_y, valid_X, valid_y))
            valid_predicts[valid_index] = model.predict(valid_X)
        total_auc = round(roc_auc_score(y, valid_predicts), 6)
        C = confusion_matrix(y, valid_predicts>0.5)
        print("混淆矩阵：")
        print(C)
    
    importance_df = pd.DataFrame({
        'column': feature_names,
        'importance': model.bst.feature_importance(),
    }).sort_values(by='importance', ascending=False)
    
    print("feature importance:")
    print(importance_df)
    
    localtime = time.localtime(time.time())
    timestamp = time.strftime("%m%d%H%M%S", localtime)
    mean, std = round(np.mean(losses), 6), round(np.std(losses), 6)
    print("Valid Loss and AUC: {} {}".format(mean, total_auc))
    
    will_cal_qauc = cal_qauc and type(train_qid) == np.ndarray
    
    if will_cal_qauc:
        with Timer("cal valid qauc"):
            if valid_type == "simple":
                qauc_df = pd.DataFrame({
                    "query_id": train_qid[split_point:],
                    "label": y[split_point:],
                    "prediction": valid_predicts
                })
            elif valid_type == "kfold":
                qauc_df = pd.DataFrame({
                    "query_id": train_qid,
                    "label": y,
                    "prediction": valid_predicts
                })
            qauc_res = round(CalQAuc(qauc_df), 6)
            print("Valid QAUC: {}".format(qauc_res))
        filename = '%s_%s_qauc%f_loss%f_std%f_%s.npy' % (model_name, prefix, qauc_res, mean, std, timestamp)
    else:
        filename = '%s_%s_auc%f_loss%f_std%f_%s.npy' % (model_name, prefix, total_auc, mean, std, timestamp)
        
    # stack的时候可能会用
    # valid_save_file = os.path.join(RES_TRAIN_OUT, filename)
    # np.save(valid_save_file, valid_predicts)
    # print("Saved valid results to {}".format(valid_save_file))

    if type(test_X) == np.ndarray:
        model.fit(X, y)
        test_predicts = model.predict(test_X)
        if cal_qauc and type(test_y) == np.ndarray:
            with Timer("cal test qauc"):
                qauc_df = pd.DataFrame({
                    "query_id": test_qid,
                    "label": test_y,
                    "prediction": test_predicts
                })
                test_qauc_res = round(CalQAuc(qauc_df), 6)
                print("Test QAUC: {}".format(test_qauc_res))
        if save_result:
            test_save_file = os.path.join(RES_TEST_OUT, filename)
            np.save(test_save_file, test_predicts)
            print("Saved test results to {}".format(test_save_file))
    
    res = {
        'loss': mean,
        "auc": total_auc,  # 整体valid算auc
        'loss_variance': std,
        'status': STATUS_OK,
        'file_name': filename,
        "importance": np.array(importance_df)
    }
    
    if will_cal_qauc:
        res["qauc"] = qauc_res
        
    return res


def run_lgb_gbdt_fast(prefix, valid_type="simple", cal_qauc=False, save_result=True):
    
    params = {
        "model": "lgb_gbdt",
        "num_threads": 10,
        "prefix": prefix,
        "valid_type": valid_type,
        "cal_qauc": cal_qauc,
        "save_result": save_result
    }
    
    info = fn(params)
    loss = info["loss"]
    
    if type(test_X) == np.ndarray:
        mode = "online"
    else:
        mode = "debug"
        
    json.dump(info, open(RES_OUT+'lgbGbdt_{}_{}_{}_{}.json'.format(mode, prefix, loss, int(time.time())),'w'),
            indent=1, cls=MyEncoder)


def run_lgb_gbdt(prefix, eval_num=20, valid_type="simple", cal_qauc=False, save_result=True):
    
    trials = Trials()
    search_space = {
        'model': 'lgb_gbdt',
        'num_threads':5,
        'num_leaves': hp.quniform('num_leaves', 20, 50, 5),
        'min_data_in_leaf': hp.quniform('min_data_in_leaf', 10, 50, 10),
        'feature_fraction': hp.quniform('feature_fraction', 0.6, 1.0, 0.1),
        'bagging_fraction': hp.quniform('bagging_fraction', 0.6, 1.0, 0.1),
        'bagging_freq': hp.quniform('bagging_freq', 0, 20, 2),
        'max_bin': hp.choice('max_bin', [63, 255]),
        'learning_rate': hp.quniform('learning_rate', 0.1, 0.2, 0.01),
        'num_iterations': hp.quniform('num_iterations', 100, 200, 20),
        "lambda_l1": hp.quniform('lambda_l1', 0.0, 1.0, 0.1),
        "lambda_l2": hp.quniform('lambda_l2', 0, 10, 2),
        "min_gain_to_split": hp.quniform('min_gain_to_split', 0.0, 1.0, 0.1),
        "prefix": prefix,
        "valid_type": valid_type,
        "cal_qauc": cal_qauc,
        "save_result": save_result
    }
    best_param = fmin(fn, space=search_space,
                        algo=tpe.suggest,
                        max_evals=eval_num,
                        trials=trials)

    info = trials.best_trial
    info['param'] = best_param
    loss = info["result"]["loss"]

    if type(test_X) == np.ndarray:
        mode = "online"
    else:
        mode = "debug"

    json.dump(info, open(RES_OUT+'lgbGbdt_{}_{}_{}_{}.json'.format(mode, prefix, loss, int(time.time())),'w'),
            indent=1, cls=MyEncoder)