
import os
# import config
import pickle
import numpy as np
import pandas as pd
import time
import json
# https://www.jianshu.com/p/35eed1567463
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import log_loss
from models import LigthGBM_GDBT

model_map = {
    'lgb_dart': LigthGBM_DART,
    'lgb_gbdt': LigthGBM_GDBT,
    # 'sklearn_rf': Sklearn_RF,
    # 'torch_nn': Torch_DNN
}

def _load_train():
    with Timer("Load train"):
      X = np.load('train_excalibur_v5.npy', mmap_mode='r')
      y = np.load(config.IN_TRAIN_LABEL, mmap_mode='r')
      return X, y


def fn(params):

    model_name = params.pop('model')
    model = model_map[model_name](**params)
    
    print(json.dumps(params, indent=1))

    train_predicts = np.empty_like(y)
    losses = []
    for i, (train_index, valid_index) in enumerate(kf):
        train_X, train_y = X[train_index], y[train_index]
        valid_X, valid_y = X[valid_index], y[valid_index]
        eval_loss = model.fit(train_X, train_y, valid_X, valid_y)
        losses.append(eval_loss)
        train_predicts[valid_index] = model.predict(valid_X)

    timestamp, mean, std = int(time.time()), np.mean(losses), np.std(losses)
    filename = '%s_%d_%f_%f_[parmas]_%s.npy' % (model_name, timestamp, mean, std, json.dumps(params))
    np.save(os.path.join(config.OUTPUT_TRAIN_DIR, filename), train_predicts)
    # Save Test
    model.fit(X, y)
    test_predicts = model.predict(test_X)
    np.save(os.path.join(config.OUTPUT_TEST_DIR, filename), test_predicts)

    return {
        'loss': mean,
        'loss_variance': std,
        'status': STATUS_OK,
        'file_name': filename
    }


def run_lgb_gbdt():
    trials = Trials()
    search_space = {
        'model': 'lgb_gbdt',
        'num_threads':8,
        'num_leaves': hp.quniform('num_leaves', 20, 100, 5),
        'min_data_in_leaf': hp.quniform('min_data_in_leaf', 10, 100, 10),
        'feature_fraction': hp.quniform('feature_fraction', 0.6, 1.0, 0.1),
        'bagging_fraction': hp.quniform('bagging_fraction', 0.6, 1.0, 0.1),
        'bagging_freq': hp.quniform('bagging_freq', 0, 20, 2),
        'max_bin': hp.choice('max_bin', [15, 63, 255, 1023]),
        'learning_rate': hp.quniform('learning_rate', 0.01, 0.1, 0.01),
        'num_iterations': hp.quniform('num_iterations', 100, 500, 50)
    }
    best_param = fmin(fn,
                      space=search_space,
                      algo=tpe.suggest,
                      max_evals=100,
                      trials=trials)


    info = trials.best_trial
    info['param'] = best_param

    json.dump(info, open('lgb_gbdt_best_info.json','w'),indent=1)