import os
import numpy as np
import pandas as pd
import lightgbm as lgb
# from minepy import MINE
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFE, f_regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso


def normalize(ranks, order=1):
    ranks = np.array(ranks, dtype=float)
    minmax = MinMaxScaler()
    ranks = minmax.fit_transform(order*ranks.reshape([-1, 1])).reshape(-1)
    ranks = np.round(ranks, 3)
    return ranks


def linear_regression(X, y):
    lr = LinearRegression(normalize=True).fit(X, y)
    return normalize(np.abs(lr.coef_))


def ridge(X, y):
    # 岭回归
    ridge = Ridge(alpha=2).fit(X, y)
    return normalize(np.abs(ridge.coef_))


def lasso(X, y):
    lasso = Lasso(alpha=0.05).fit(X, y)
    return normalize(np.abs(lasso.coef_))


# def stability_select(X, y):
#     rlasso = RandomizedLasso(alpha=0.04).fit(X, y)
#     return normalize(np.abs(rlasso.scores_))


def ref(X, y):
    rfe = RFE(LinearRegression(normalize=True), n_features_to_select=50).fit(X, y)
    return normalize(rfe.ranking_, order=-1)


def correlation(X, y):
    f, pval = f_regression(X, y, center=True)
    return normalize(f)


def random_forest(X, y):
    rf = RandomForestRegressor().fit(X, y)
    return normalize(rf.feature_importances_)


def light_gbm(X, y):
    HYPER_PARAM = {
        'num_leaves': 30,
        'objective': 'binary',
        'metric': 'binary_logloss',
        'feature_fraction': 0.8,
        'bagging_fraction': 0.8,
        'silent': 1
    }
    NUM_ROUND = 80
    EARLY_STOP = 40
    skf = StratifiedKFold(5, shuffle=True)
    importances = []
    for i, (train_index, dev_index) in enumerate(skf.split(X, y)):
        train_data = lgb.Dataset(X[train_index], label=y[train_index])
        dev_data = lgb.Dataset(X[dev_index], label=y[dev_index])

        bst = lgb.train(HYPER_PARAM,
                        train_data,
                        verbose_eval=40,
                        valid_sets=[dev_data],
                        valid_names=['Dev'],
                        num_boost_round=NUM_ROUND,
                        early_stopping_rounds=EARLY_STOP)
        importances.append(bst.feature_importance())
    importances = np.stack(importances).mean(0)
    return normalize(importances)


def select_features(method, X, y, feature_cols, savedir):

    np.random.seed(2019)
    ranks = pd.DataFrame(index=feature_cols)

    if method == 'simple':
        ranks['Ridge'] = ridge(X, y)
        ranks['Lasso'] = lasso(X, y)
        ranks['Correlation'] = correlation(X, y)
        ranks['Linear Regression'] = linear_regression(X, y)
        # ranks['Stability Selection'] = stability_select(X, y)
    elif method == 'ref':
        ranks['REF'] = ref(X, y)
    elif method == 'lgb':
        ranks['LightGBM'] = light_gbm(X, y)
    elif method == 'rf':
        ranks['Random Forest'] = random_forest(X, y)
    # elif method == 'mic':
    #     ranks['MIC'] = mic(X, y)
    else:
        print('No such method !')

    savefile = savedir + 'features_weight_%s.csv' % method
    ranks.to_csv(savefile)
    print('Save to %s' % savefile)