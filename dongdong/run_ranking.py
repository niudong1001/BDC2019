'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-07 22:12:50
@LastEditTime: 2019-08-09 21:07:00
'''
import os, json, sys, time, pickle
import numpy as np
import pandas as pd
# https://www.jianshu.com/p/35eed1567463
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
# from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
sys.path.append("dongdong")
sys.path.append("common")
from config import K_FOLD, COMMON_DIR, RES_TRAIN_OUT, RES_TEST_OUT, RES_OUT
from ranking import RankSVM, RankRidge, transform_pairwise
from utils import Timer, MyEncoder, CalQAuc
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler


X, y, test_X  = None, None, None
# q_auc_data是用来辅助qauc的计算，上面有query_id, label等
feature_names, q_auc_data = None, None
train_qid, test_qid = None, None
models = {
    "ridge": RankRidge,
    "svm":RankSVM
}


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
            

def run_ranking(model_name, prefix, valid_type="simple", cal_qauc=True):

    global X, y, test_X, q_auc_data, feature_names
    global train_qid, test_qid
    
    with Timer("cal pairwise"):
        print(X.shape)
        print(y.shape)
        print(train_qid.shape)
        X_pairs, y_pairs = transform_pairwise(X, np.c_[y, train_qid])
    
    model = models[model_name]()
    accs, aucs = [], []
    
    if valid_type == "simple":
        pass
        # total_samples = X_pairs.shape[0]
        # split_point = int(total_samples * 0.7)
        # train_X, valid_X = X_pairs[:split_point], X_pairs[split_point:]
        # train_y, valid_y = y_pairs[:split_point], y_pairs[split_point:]
        # model.fit(train_X, train_y)
        # accs.append(model.score(valid_X, valid_y))
        # valid_predicts = model.predict(valid_X, train_qid[split_point:])
        # print("valid res:")
        # print(valid_predicts.shape)
        # print("valid pred:", valid_predicts[:20])
        # print("qid:", train_qid[:20])
        # total_auc = round(roc_auc_score(y[split_point:], valid_predicts), 6)
        # C = confusion_matrix(valid_y[:, 0], valid_predicts>0.5)
        # print(C)
    elif valid_type == "kfold":
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
        total_auc = round(roc_auc_score(y, valid_predicts), 6)
        C = confusion_matrix(y, valid_predicts>0.5)
        print(C)
    
    # importance_df = pd.DataFrame({
    #     'column': feature_names,
    #     'importance': model.coef_,
    # }).sort_values(by='importance', ascending=False)
    
    # print("feature importance:")
    # print(importance_df)
    
    localtime = time.localtime(time.time())
    timestamp = time.strftime("%m%d%H%M%S", localtime)
    # mean, std = round(np.mean(accs), 6), round(np.std(accs), 6)
    # print("Valid Acc: {}".format(mean))
    
    if cal_qauc and type(q_auc_data) == np.ndarray:
        with Timer("cal qauc"):
            if valid_type == "simple":
                query_id = q_auc_data[:, 0][split_point:]
                label = q_auc_data[:, 1][split_point:]
                print(query_id.shape, label.shape, valid_predicts.shape)
                q_auc_df = pd.DataFrame({
                    "query_id": query_id,
                    "label": label,
                    "prediction": valid_predicts
                })
            elif valid_type == "kfold":
                q_auc_df = pd.DataFrame({
                    "query_id": q_auc_data[:, 0],
                    "label": q_auc_data[:, 1],
                    "prediction": valid_predicts
                })
            q_auc_res = round(CalQAuc(q_auc_df), 6)
            print("Valid QAUC: {}".format(q_auc_res))
        filename = '%s_%s_qauc%f_acc%f_std%f_%s.npy' % (model_name, prefix, q_auc_res, mean, std, timestamp)
    else:
        filename = '%s_%s_%s.npy' % (model_name, prefix, timestamp)
        
    # stack的时候可能会用
    # valid_save_file = os.path.join(RES_TRAIN_OUT, filename)
    # np.save(valid_save_file, valid_predicts)
    # print("Saved valid results to {}".format(valid_save_file))

    if type(test_X) == np.ndarray:
        model.fit(X_pairs, y_pairs)
        test_predicts = model.predict(test_X, test_qid)
        test_save_file = os.path.join(RES_TEST_OUT, filename)
        np.save(test_save_file, test_predicts)
        print("Saved test results to {}".format(test_save_file))
    
    res = {
        # 'loss': mean,
        # 'loss_variance': std,
        'status': STATUS_OK,
        'file_name': filename,
        # "importance": np.array(importance_df)
    }
    if type(q_auc_data) == np.ndarray:
        # res["q_auc_res"] = q_auc_res
        pass
        
    return res

