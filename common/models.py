'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-06 23:58:52
@LastEditTime: 2019-08-09 21:03:53
'''
import sys
import numpy as np
import lightgbm as lgb


class LigthGBM(object):
    
    def __init__(self, num_leaves=31, min_data_in_leaf=20, max_bin=255, 
    feature_fraction=1.0, bagging_fraction=1.0, bagging_freq=0, 
    num_iterations=100, learning_rate=0.1, num_threads=10, lambda_l1=0,
    lambda_l2=0, min_gain_to_split=0):
        self.HYPER_PARAM = {
            'verbose':-1,
            'num_threads':num_threads,
            'objective': 'binary',
            'metric': ['binary_logloss'],
            'num_leaves':int(num_leaves),
            'min_data_in_leaf':int(min_data_in_leaf),
            'feature_fraction':feature_fraction,
            'bagging_fraction':bagging_fraction,
            'bagging_freq':int(bagging_freq),
            'max_bin':int(max_bin),
            'learning_rate':learning_rate,
            "device": "gpu",
            "gpu_platform_id": 0,
            "gpu_divice_id": 0,
            "lambda_l1": lambda_l1,
            "lambda_l2": lambda_l2,
            "min_gain_to_split": min_gain_to_split
        }
        self.num_boost_round = int(num_iterations)
        self.bst = None

    def fit(self, X, y, valid_X=None, valid_y=None):
        train_set = lgb.Dataset(X, label=y)
        if valid_X is None or valid_y is None:
            self.bst = lgb.train(self.HYPER_PARAM,
                            train_set,verbose_eval=50,
                            num_boost_round=self.num_boost_round)
        else :
            evals_result = {}
            valid_set = lgb.Dataset(valid_X, label=valid_y)
            self.bst = lgb.train(self.HYPER_PARAM,
                            train_set,
                            verbose_eval=50,
                            evals_result = evals_result,
                            valid_names=['valid'],
                            valid_sets=[valid_set],
                            num_boost_round=self.num_boost_round)
            self.valid_loss = evals_result['valid']['binary_logloss']
            return self.valid_loss

    def predict(self, X):
        return self.bst.predict(X)


class LigthGBM_DART(LigthGBM):
    def __init__(self, drop_rate, skip_drop, **kargv):
        super(LigthGBM_DART, self).__init__(**kargv)
        self.HYPER_PARAM.update({
            'drop_rate': drop_rate,
            'skip_drop': skip_drop,
            'boosting':'dart'
        })


class LigthGBM_GBDT(LigthGBM):
    def __init__(self, **kargv):
        super(LigthGBM_GBDT, self).__init__(**kargv)
        self.HYPER_PARAM.update({
            'boosting':'gbdt',
        })