'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-03 21:24:31
@LastEditTime: 2019-06-10 19:28:18
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
    df['%s_q-len' % prefix] = df['q_ngram'].apply(lambda x: len(x))
    df['%s_t-len' % prefix] = df['t_ngram'].apply(lambda x: len(x))
    df['%s_q-log-len' % prefix] = df['q_ngram'].apply(lambda x: np.log1p(len(x)))
    df['%s_t-log-len' % prefix] = df['t_ngram'].apply(lambda x: np.log1p(len(x)))

    ## 字符集合相似度
    df['%s_dice-ratio'% prefix] = df.apply(lambda x: dist_utils.dice_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_jaccard-ratio'% prefix] = df.apply(lambda x: dist_utils.jaccard_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_edit-seq-ratio'% prefix] = df.apply(lambda x: dist_utils.edit_seq_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_edit-set-ratio'% prefix] = df.apply(lambda x: dist_utils.edit_set_ratio(x['q_ngram'], x['t_ngram']), axis=1)

    df.drop(['q_ngram', 't_ngram'], axis=1, inplace=True)

    return df


def ExtractTextFeature(source_csv, save_dir, prefix, names, dtype, process_chunkly=True, chunk_size=CHUNK_SIZE, drop_cols=['query', 'title', 'label']):

    with Timer("Extract text feature"):
        
        feature = []

        def process(df):
            # df = run(df, ngram_utils.unichars, '%s_%s' % (prefix, 'unichars'))
            # df = run(df, ngram_utils.bichars, '%s_%s' % (prefix, 'bichars'))
            # df = run(df, ngram_utils.trichars, '%s_%s' % (prefix, 'trichars'))
            df = run(df, ngram_utils.unigrams, '%s_%s' % (prefix, 'unigrams'))
            df = run(df, ngram_utils.bigrams, '%s_%s' % (prefix, 'bigrams'))
            df = run(df, ngram_utils.trigrams, '%s_%s' % (prefix, 'trigrams'))
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

        save_path = os.path.join(save_dir, '%s_feature_text.csv' % prefix)
        tmp = pd.concat(feature, axis=0)
        tmp.to_csv(save_path, index=None)  # 带表头
        del feature, tmp
        gc.collect()