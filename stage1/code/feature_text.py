'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-03 21:24:31
@LastEditTime: 2019-06-13 23:37:47
'''

import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
from .utils import dist_utils, ngram_utils
from .config import GLOBAL_DIR
sys.path.append(GLOBAL_DIR)
from helper import ProcessChunk, ReadCSV, CHUNK_SIZE, Timer
import gc


def run(df, ngram, prefix):

    # ngram
    df['q_ngram'] = df['query'].apply(ngram)
    df['t_ngram'] = df['title'].apply(ngram)

    ## 长度特征
    with Timer("extract ngram length"):
        df['%s_q-len' % prefix] = np.vectorize(len)(df["q_ngram"])
        df['%s_t-len' % prefix] = np.vectorize(len)(df["t_ngram"])
        df['%s_q-log-len' % prefix] = np.vectorize(lambda x: np.log1p(len(x)))(df["q_ngram"])
        df['%s_t-log-len' % prefix] = np.vectorize(lambda x: np.log1p(len(x)))(df["t_ngram"])

    ## 字符集合相似度
    with Timer("extract ngram similarity"):
        df['%s_dice-ratio'% prefix] = np.vectorize(dist_utils.dice_ratio)(df['q_ngram'], df['t_ngram'])
        df['%s_jaccard-ratio'% prefix] = np.vectorize(dist_utils.jaccard_ratio)(df['q_ngram'], df['t_ngram'])
        df['%s_edit-seq-ratio'% prefix] = np.vectorize(dist_utils.edit_seq_ratio)(df['q_ngram'], df['t_ngram'])
        df['%s_edit-set-ratio'% prefix] = np.vectorize(dist_utils.edit_set_ratio)(df['q_ngram'], df['t_ngram'])
    
    print()

    df.drop(['q_ngram', 't_ngram'], axis=1, inplace=True)

    return df


def ExtractTextFeature(source_csv, save_dir, prefix, names, dtype, process_chunkly=True, chunk_size=CHUNK_SIZE, drop_first_cols=['query_id', 'query_title_id', 'label'], drop_last_cols=['query', 'title']):

    with Timer("Extract text feature"):
        
        save_path = os.path.join(save_dir, '%s_feature_text.csv' % prefix)
        if os.path.exists(save_path):
            os.remove(save_path)

        def process(df):
            # 先丢弃不需要的部分，避免长时间占用内存
            df.drop(drop_first_cols, axis=1, inplace=True, errors='ignore')
            # 提取特征
            df = run(df, ngram_utils.unigrams, '%s_%s' % (prefix, 'unigrams'))
            df = run(df, ngram_utils.bigrams, '%s_%s' % (prefix, 'bigrams'))
            df = run(df, ngram_utils.trigrams, '%s_%s' % (prefix, 'trigrams'))
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