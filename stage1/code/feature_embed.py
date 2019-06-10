'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-04 23:04:29
@LastEditTime: 2019-06-10 20:12:50
'''
import os
import sys
import gc
import gensim
import numpy as np
import pandas as pd
from datetime import datetime
from .config import GLOBAL_DIR
sys.path.append(GLOBAL_DIR)
from .utils import dist_utils, ngram_utils
from scipy.stats import skew, kurtosis
from helper import ProcessChunk, ReadCSV, ORI_TRAIN_NAMES, ORI_TEST_NAMES, CHUNK_SIZE, Timer


model, norm_model = None, None


def sent2vec(words):
    # 计算embedding均值
    assert isinstance(words, list)
    vector_size = model.syn0.shape[1]
    v = np.array([np.zeros(vector_size)]+[model[w] for w in words if w in model]).mean(axis=0)
    return np.nan_to_num(v)


def wmd(s1, s2):
    # 从文档整体上来考虑两个文档之间的相似性，这种技术称为词移距离（WMD）,https://blog.csdn.net/qrlhl/article/details/78512598
    # https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.WordEmbeddingsKeyedVectors.wmdistance
    dis = model.wmdistance(s1, s2)
    dis = np.nan_to_num(dis)
    return dis if dis<100 else 100


def norm_wmd(s1, s2):
    dis = norm_model.wmdistance(s1, s2)
    dis = np.nan_to_num(dis)
    return dis if dis<100 else 100


def run(df, ngram, prefix):

    # ngram
    df['q_ngram'] = df['query'].apply(ngram)
    df['t_ngram'] = df['title'].apply(ngram)

    # wmd, 衡量两个文档的语义相似性
    df['%s_wmd' % prefix] = df.apply(lambda x: wmd(x['q_ngram'], x['t_ngram']), axis=1)
    # df['%s_norm-wmd' % prefix] = df.apply(lambda x: norm_wmd(x['q_ngram'], x['t_ngram']), axis=1)

    # Embeddings
    ## 偏态, https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html
    df['%s_q-skew' % prefix] = df['q_ngram'].apply(lambda x :skew(sent2vec(x)))
    df['%s_t-skew' % prefix] = df['t_ngram'].apply(lambda x :skew(sent2vec(x)))
    ## 峰度, https://blog.csdn.net/xbmatrix/article/details/69360167
    df['%s_q-kurtosis' % prefix] = df['q_ngram'].apply(lambda x :kurtosis(sent2vec(x)))
    df['%s_t-kurtosis' % prefix] = df['t_ngram'].apply(lambda x :kurtosis(sent2vec(x)))
    ## 距离
    df['%s_cosine-distance' % prefix] = df.apply(lambda x: dist_utils.cosine_distance(sent2vec(x['q_ngram']), sent2vec(x['t_ngram'])), axis=1)
    # df['%s_jaccard-distance' % prefix] = df.apply(lambda x: dist_utils.jaccard_distance(sent2vec(x['q_ngram']), sent2vec(x['t_ngram'])), axis=1)
    df['%s_canberra-distance' % prefix] = df.apply(lambda x: dist_utils.canberra_distance(sent2vec(x['q_ngram']), sent2vec(x['t_ngram'])), axis=1)
    df['%s_cityblock-distance' % prefix] = df.apply(lambda x: dist_utils.cityblock_distance(sent2vec(x['q_ngram']), sent2vec(x['t_ngram'])), axis=1)
    df['%s_euclidean-distance' % prefix] = df.apply(lambda x: dist_utils.euclidean_distance(sent2vec(x['q_ngram']), sent2vec(x['t_ngram'])), axis=1)
    df['%s_minkowski-distance' % prefix] = df.apply(lambda x: dist_utils.minkowski_distance(sent2vec(x['q_ngram']), sent2vec(x['t_ngram'])), axis=1)
    df['%s_braycurtis-distance' % prefix] = df.apply(lambda x: dist_utils.braycurtis_distance(sent2vec(x['q_ngram']), sent2vec(x['t_ngram'])), axis=1)

    df.drop(['q_ngram', 't_ngram'], axis=1, inplace=True)
    
    return df


def ExtractEmbedFeature(source_csv, save_dir, prefix, names, dtype, embed_mode, embed_model_file, process_chunkly=True, chunk_size=CHUNK_SIZE, drop_cols=['query', 'title', 'label']):

    with Timer("Extract embedding feature"):

        global model
        
        if embed_mode == "fastText":
            pass
        elif embed_mode == "word2vec":
            model = gensim.models.KeyedVectors.load(embed_model_file, mmap='r')
            # norm_model = gensim.models.KeyedVectors.load(embed_model_file, mmap='r')
            # norm_model.init_sims(replace=True)

        feature = []
        
        def process(df):
            df = run(df, ngram_utils.unigrams, '%s_%s' % (prefix, 'unigrams'))
            df.drop(drop_cols, axis=1, inplace=True, errors='ignore')
            feature.append(df)
        
        if process_chunkly:
            ProcessChunk(source_csv, process, 
            names=names, dtype=dtype,
            chunk_size=chunk_size)
        else:
            process(
                ReadCSV(source_csv, names=names, 
                dtype=dtype, iterator=False)
            )

        save_path = os.path.join(save_dir, '%s_feature_embed.csv' % prefix)
        tmp = pd.concat(feature, axis=0)
        tmp.to_csv(save_path, index=None)  # 带表头
        
        del feature, tmp
        gc.collect()