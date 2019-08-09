'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-07 22:12:50
@LastEditTime: 2019-08-09 21:06:45
'''
import os, json, sys, time, pickle
import numpy as np
import pandas as pd
# https://www.jianshu.com/p/35eed1567463
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
# from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
sys.path.append("dongdong")
sys.path.append("common")
from config import K_FOLD, RES_TRAIN_OUT, RES_TEST_OUT, RES_OUT
from utils import Timer, MyEncoder, CalQAuc
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import lightgbm  as lgb


X, y, test_X  = None, None, None
# q_auc_data是用来辅助qauc的计算，上面有query_id, label等
feature_names, q_auc_data = None, None
train_qid, test_qid = None, None


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def get_y_split_points(y):
    split_points = [i for i in range(1, len(y)) if y[i] != y[i-1]]
    return split_points


def get_qid_group(qid):
    res = []
    count = 1
    for _ in range(1, len(qid)):
        if qid[_] == qid[_-1]:
            count += 1
        else:
            res.append(count)
            count = 1
    res.append(count)
    return res


def get_res_prob(predicts, qid):
    split_points = get_y_split_points(qid)
    return np.concatenate([softmax(_) for _ in np.split(predicts, split_points)])


def LoadDataset(in_train_feature, in_train_label, in_train_qid, in_feature_names,
    in_q_auc_data=None, in_test_feature=None, in_test_qid=None, verbose=True):

    global X, y, test_X, feature_names, q_auc_data, train_qid, test_qid
    
    params = {
        "in_train_feature": in_train_feature,
        "in_train_label": in_train_label,
        "in_train_qid": in_train_qid,
        "in_feature_names": in_feature_names,
        "in_q_auc_data": in_q_auc_data,
        "in_test_feature": in_test_feature,
        "in_test_qid": in_test_qid
    }
    print(json.dumps(params, indent=1))
    
    X_scale =  StandardScaler()

    def _load_train():
        X = X_scale.fit_transform(
                np.load(in_train_feature)
            )
        y = np.load(in_train_label)
        return X, y
    def _load_test():
        X = X_scale.transform(
                np.load(in_test_feature)
            )
        return X
    def _load_feature_names():
        return list(
            pd.read_csv(
                in_feature_names, 
                sep=","
            ).columns.values
        )
    def _load_q_auc_data():
        return np.load(in_q_auc_data)
    def _load_train_qid():
        return np.load(in_train_qid)
    def _load_test_qid():
        return np.load(in_test_qid)
    
    X, y =  _load_train()
    train_qid = _load_train_qid()
    feature_names = _load_feature_names()
    if in_q_auc_data:
        q_auc_data = _load_q_auc_data()
    if in_test_feature:
        test_X = _load_test()
        test_qid = _load_test_qid()

    if verbose:
        print("X shape:", X.shape)
        print("X (two rows):")
        print(X[:2])
        print("y shape:", y.shape)
        print("y (two rows):", y[:2])
        if in_test_feature:
            print("test X shape:", test_X.shape)
            print("test X (two rows):")
            print(test_X[:2])
        if in_q_auc_data:
            print("qauc data shape:", q_auc_data.shape)
            print("qauc data (two rows):")
            print(q_auc_data[:2])
    
    
def run_lambdarank(prefix, valid_type="simple", cal_qauc=True):
    
    global X, y, test_X, q_auc_data, feature_names
    global train_qid, test_qid
    
    gbm = lgb.LGBMRanker()
    model_name = "lambdarank"
    
    if valid_type == "simple":
        total_samples = X.shape[0]
        split_point = int(total_samples * 0.7)
        train_X, valid_X = X[:split_point], X[split_point:]
        train_y, valid_y = y[:split_point], y[split_point:]
        train_qid_group = get_qid_group(train_qid[:split_point])
        valid_qid_group = get_qid_group(train_qid[split_point:])
        gbm.fit(train_X, train_y, group=train_qid_group, eval_set=[(valid_X, valid_y)],
                eval_group=[valid_qid_group], eval_at=[1, 3], early_stopping_rounds=5, verbose=False,
                callbacks=[lgb.reset_parameter(learning_rate=lambda x: 0.95 ** x * 0.1)])
        valid_predicts = get_res_prob(gbm.predict(valid_X, raw_score=True), train_qid[split_point:])
        total_auc = round(roc_auc_score(y[split_point:], valid_predicts), 6)
    else:
        pass
    
    importance_df = pd.DataFrame({
        'column': feature_names,
        'importance': gbm.feature_importances_,
    }).sort_values(by='importance', ascending=False)
    
    print("feature importance:")
    print(importance_df)
    
    localtime = time.localtime(time.time())
    timestamp = time.strftime("%m%d%H%M%S", localtime)
    
    if cal_qauc and type(q_auc_data) == np.ndarray:
        with Timer("cal qauc"):
            if valid_type == "simple":
                query_id = q_auc_data[:, 0][split_point:]
                label = q_auc_data[:, 1][split_point:]
                q_auc_df = pd.DataFrame({
                    "query_id": query_id,
                    "label": label,
                    "prediction": valid_predicts
                })
            elif valid_type == "kfold":
                pass
            q_auc_res = round(CalQAuc(q_auc_df), 6)
            print("Valid QAUC: {}".format(q_auc_res))
        filename = '%s_%s_qauc%f_%s.npy' % (model_name, prefix, q_auc_res, timestamp)
    else:
        filename = '%s_%s_auc%f_%s.npy' % (model_name, prefix, total_auc, timestamp)
    
    if type(test_X) == np.ndarray:
        train_qid_group = get_qid_group(train_qid)
        gbm.fit(X, y, group=train_qid_group, verbose=False,
                callbacks=[lgb.reset_parameter(learning_rate=lambda x: 0.95 ** x * 0.1)])
        test_predicts = get_res_prob(gbm.predict(test_X, raw_score=True), test_qid)
        test_save_file = os.path.join(RES_TEST_OUT, filename)
        np.save(test_save_file, test_predicts)
        print("Saved test results to {}".format(test_save_file))