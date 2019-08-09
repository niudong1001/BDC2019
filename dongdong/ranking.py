'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-06 23:58:52
@LastEditTime: 2019-08-09 21:06:23
'''
import sys
import numpy as np
from sklearn import svm, linear_model
import itertools
sys.path.append("./common")
from utils import Timer
import gc


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def get_y_split_points(y):
    split_points = [i for i in range(1, len(y)) if y[i] != y[i-1]]
    return split_points
    

def transform_test_pairwise(X, qid):
    split_points = get_y_split_points(qid)
    X = np.split(X, split_points)
    X_new, y_new = [], []
    for _ in range(len(X)):
        tmp_X = X[_]
        if len(tmp_X) == 1:
            X_new.append(tmp_X[0])
            continue
        for i in range(1, len(tmp_X)):
            # 直接特征相减, 前减后
            X_new.append(tmp_X[i-1] - tmp_X[i])
    X_ = np.asarray(X_new)
    del X, X_new, split_points
    gc.collect()
    print("pairwise info:")
    print("X shape:", X_.shape)
    return X_


def transform_pairwise(X, y):
    # y: [[label, qid]], label = {0, 1}
    y = np.asarray(y)
    if len(y.shape) != 2:
        raise ValueError("y must has shape len of 2!")
    split_points = get_y_split_points(y[:, 1])
    X = np.split(X, split_points)
    y = np.split(y, split_points)
    X_new, y_new, count = [], [], 0
    for _ in range(len(y)):
        tmp_X, tmp_y = X[_], y[_]
        comb = itertools.combinations(range(len(tmp_y)), 2)
        for k, (i, j) in enumerate(comb):
            # 跳过标签一样
            # 跳过group不一样
            if tmp_y[i, 0] == tmp_y[j, 0] or tmp_y[i, 1] != tmp_y[j, 1]:
                continue
            # 直接特征相减
            X_new.append(tmp_X[i] - tmp_X[j])
            y_new.append(np.sign(tmp_y[i, 0] - tmp_y[j, 0]))
            # 平衡类别
            if y_new[-1] != (-1) ** count:
                X_new[-1] = -X_new[-1]
                y_new[-1] = -y_new[-1]
            count += 1
    X_ = np.asarray(X_new)
    y_ = np.asarray(y_new).ravel()
    del X, y, X_new, y_new, split_points
    gc.collect()
    print("pairwise info:")
    print("X shape:", X_.shape)
    print("y shape:", y_.shape)
    return X_, y_ 


# class RankSVM(svm.LinearSVC):
#     def fit(self, X, y):
#         # y第一列为标签、第二列为所属group_id
#         with Timer("pair construct"):
#             X_, y_ = transform_pairwise(X, y)
#         with Timer("fit"):
#             super(RankSVM, self).fit(X_, y_)
#         return self
#     def _predict(self, X):
#         if hasattr(self, "coef_"):
#             return np.dot(X, self.coef_.ravel())
#         else:
#             raise ValueError("Fit firstlly!")
#     def predict(self, X, qid):
#         res = self._predict(X)
#         group = get_y_group(qid)
#         res = np.concatenate([softmax(_) for _ in np.split(res, group)])
#         return res
#     def score(self, X, y):
#         X_, y_ = transform_pairwise(X, y)
#         return np.mean(super(RankSVM, self).predict(X_) == y_)


class RankRidge(linear_model.Ridge):
    
    def fit(self, X, y):
        with Timer("fit"):
            super(RankRidge, self).fit(X, y)
            return self
            
    def _predict(self, X):
        if hasattr(self, "coef_"):
            return np.dot(X, self.coef_.ravel())
        else:
            raise ValueError("Fit firstly!")
            
    def predict(self, X, qid):
        split_points = get_y_split_points(qid)
        res = np.concatenate([softmax(_) for _ in np.split(self._predict(X), split_points)])
        return res
        
    def valid_score(self, X, y):
        res = np.sign(super(RankRidge, self).predict(X))
        return np.mean(res == y)