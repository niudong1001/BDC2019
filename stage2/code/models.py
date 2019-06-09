import sys
import numpy as np
from .config import GLOBAL_DIR
# from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
# from sklearn.metrics import log_loss
sys.path.append(GLOBAL_DIR)
from helper import Timer, usetime
import lightgbm as lgb

class LigthGBM(object):

    def __init__(self, num_leaves, min_data_in_leaf, max_bin, feature_fraction, bagging_fraction, bagging_freq, num_iterations, learning_rate, num_threads):
        self.HYPER_PARAM = {
            'num_threads':num_threads,
            'verbose':-1,
            'objective': 'binary',
            'metric': ['binary_logloss', 'auc'],
            'num_leaves':int(num_leaves),
            'min_data_in_leaf':int(min_data_in_leaf),
            'feature_fraction':feature_fraction,
            'bagging_fraction':bagging_fraction,
            'bagging_freq':int(bagging_freq),
            'max_bin':int(max_bin),
            'learning_rate':learning_rate
        }
        self.num_boost_round = int(num_iterations)

    @usetime('fit')
    def fit(self, X, y, valid_X=None, valid_y=None):
        train_set = lgb.Dataset(X, label=y)
        if valid_X is None or valid_y is None:
            self.bst = lgb.train(self.HYPER_PARAM,
                            train_set,
                            verbose_eval=50,
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
            self.valid_auc = evals_result["valid"]["auc"]
            return self.valid_loss, self.valid_auc

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