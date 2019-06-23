'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-04 23:04:29
@LastEditTime: 2019-06-13 22:26:31
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


model, norm_model, vector_size = None, None, None


def sent2vec(words):
    # 计算embedding均值
    global vector_size
    # assert isinstance(words, list)
    return np.nan_to_num(
        np.array([
            np.zeros(vector_size)]+[model[w] for w in words if w in model]
        ).mean(axis=0)
    )


def wmd(s1, s2):
    # 从文档整体上来考虑两个文档之间的相似性，这种技术称为词移距离（WMD）,https://blog.csdn.net/qrlhl/article/details/78512598
    # https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.WordEmbeddingsKeyedVectors.wmdistance
    dis = np.nan_to_num(model.wmdistance(s1, s2))
    return dis if dis < 100 else 100


def norm_wmd(s1, s2):
    dis = np.nan_to_num(norm_model.wmdistance(s1, s2))
    return dis if dis<100 else 100


def run(df, ngram, prefix):

    # ngram
    with Timer("extract preparing"):
        df['q_ngram'] = df['query'].apply(ngram)
        df['t_ngram'] = df['title'].apply(ngram)
        df['q_sen_vec'] = df["q_ngram"].apply(sent2vec)
        df['t_sen_vec'] = df["t_ngram"].apply(sent2vec)

    # wmd, 衡量两个文档的语义相似性
    with Timer("extract wmd"):
        df['%s_wmd' % prefix] = np.vectorize(wmd)(df['q_ngram'], df['t_ngram'])
        # df['%s_norm-wmd' % prefix] = np.vectorize(norm_wmd)(df['q_ngram'], df['t_ngram'])

    # Embeddings
    with Timer("extract skew"):
        ## 偏态, https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html
        df['%s_q-skew' % prefix] = np.vectorize(skew)(df['q_sen_vec'])
        df['%s_t-skew' % prefix] = np.vectorize(skew)(df['t_sen_vec'])
        
    ## 峰度, https://blog.csdn.net/xbmatrix/article/details/69360167
    with Timer("extract kurtosis"):
        df['%s_q-kurtosis' % prefix] = np.vectorize(kurtosis)(df['q_sen_vec'])
        df['%s_t-kurtosis' % prefix] = np.vectorize(kurtosis)(df['t_sen_vec'])
        
    ## 距离
    with Timer("extract embed distance"):
        df['%s_cosine-distance' % prefix] = np.vectorize(dist_utils.cosine_distance)(df["q_sen_vec"], df["t_sen_vec"])
        df['%s_cityblock-distance' % prefix] = np.vectorize(dist_utils.cityblock_distance)(df["q_sen_vec"], df["t_sen_vec"])
        df['%s_euclidean-distance' % prefix] = np.vectorize(dist_utils.euclidean_distance)(df["q_sen_vec"], df["t_sen_vec"])
        df['%s_jaccard-distance' % prefix] = np.vectorize(dist_utils.jaccard_distance)(df["q_sen_vec"], df["t_sen_vec"])
        df['%s_canberra-distance' % prefix] = np.vectorize(dist_utils.canberra_distance)(df["q_sen_vec"], df["t_sen_vec"])
        df['%s_braycurtis-distance' % prefix] = np.vectorize(dist_utils.braycurtis_distance)(df["q_sen_vec"], df["t_sen_vec"])

    df.drop(['q_ngram', 't_ngram', "q_sen_vec", "t_sen_vec"], axis=1, inplace=True)
    
    return df


def ExtractEmbedFeature(source_csv, save_dir, prefix, names, dtype, embed_mode, embed_model_file, process_chunkly=True, chunk_size=CHUNK_SIZE, drop_first_cols=['query_id', 'query_title_id', 'label'], drop_last_cols=['query', 'title'], add_header=True):

    with Timer("Extract embedding feature"):

        global model, norm_model, vector_size
        
        if embed_mode == "fastText":
            pass
        elif embed_mode == "word2vec":
            model = gensim.models.KeyedVectors.load(embed_model_file, mmap='r')
            vector_size = model.vectors.shape[1]
            # norm_model = gensim.models.KeyedVectors.load(embed_model_file, mmap='r')
            # norm_model.init_sims(replace=True)

        save_path = os.path.join(save_dir, '%s_feature_embed.csv' % prefix)
        if os.path.exists(save_path):
            os.remove(save_path)
        
        def process(df):
            # 先丢弃不需要的部分，避免长时间占用内存
            df.drop(drop_first_cols, axis=1, inplace=True, errors='ignore')
            # 提取特征
            df = run(df, ngram_utils.unigrams, '%s_%s' % (prefix, 'unigrams'))
            # 丢弃剩下的部分
            df.drop(drop_last_cols, axis=1, inplace=True, errors='ignore')
            # 增量存储
            add_header = True
            if os.path.exists(save_path): add_header = False
            df.to_csv(save_path, index=None, mode="a", header=add_header)  # 带表头
            print("Saved feature to "+save_path)

        
        if process_chunkly:
            ProcessChunk(
                source_csv, process, 
                names=names, dtype=dtype,
                chunk_size=chunk_size
            )
        else:
            process(
                ReadCSV(source_csv, names=names, 
                dtype=dtype, iterator=False)
            )