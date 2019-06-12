'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-11 19:41:20
@LastEditTime: 2019-06-12 21:57:17
'''
import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime
from .utils import dist_utils
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from .config import GLOBAL_DIR
sys.path.append(GLOBAL_DIR)
from helper import ProcessChunk, ReadCSV, CHUNK_SIZE, Timer
from functools import partial
import gc


class VectorSpace(object):

    def __init__(self, tfidf):
        self.tfidf = tfidf
        self.lsi = TruncatedSVD(n_components=50, random_state=2019)

    def transform(self, df1, df2):
        corpus = pd.concat([df1, df2], ignore_index=True)
        with Timer("Fit tf-idf"):
            self.tfidf.fit(corpus)
            del corpus
            gc.collect()
        with Timer('transform df1'):
            tmp1 = self.tfidf.transform(df1)
            self.df1_lsi = self.lsi.fit_transform(tmp1)
            del tmp1
            gc.collect()
        with Timer('transform df2'):
            tmp2 = self.tfidf.transform(df2)
            self.df2_lsi = self.lsi.fit_transform(tmp2)
            del tmp2
            gc.collect()
        del df1, df2
        gc.collect()
    
    def cosine_distance(self):
        return list(map(dist_utils.cosine_distance, 
                self.df1_lsi, self.df2_lsi))
    
    def mahalanobis_distance(self):
        return list(map(dist_utils.mahalanobis_distance, 
                self.df1_lsi, self.df2_lsi))

    def minkowski_distance(self, p):
        func = partial(dist_utils.minkowski_distance, p=p)
        return list(map(func, self.df1_lsi, self.df2_lsi))

class WordTfidfLSA(VectorSpace):
    def __init__(self):
        word_tfidf = TfidfVectorizer(norm="l2",
                                    strip_accents="unicode",
                                    analyzer="word",
                                    ngram_range=(1, 3),
                                    use_idf=1,
                                    smooth_idf=1,
                                    sublinear_tf=1)
        super(WordTfidfLSA, self).__init__(word_tfidf)


def run(df, prefix, names):

    tmp = WordTfidfLSA()
    tmp.transform(df['query'], df['title'])
    df['%s_words-tfidf-lsa-cosine_dis' % prefix] = tmp.cosine_distance()
    df['%s_words-tfidf-lsa-euclidean_dis' %prefix] = tmp.minkowski_distance(2)
    del tmp
    gc.collect()

    return df


def ExtractVectorSpaceFeature(source_csv, save_dir, prefix, names, dtype, drop_cols=['query', 'title', 'label']):
    
    with Timer("Extract vector space feature"):
        
        df = ReadCSV(source_csv, names=names, dtype=dtype, iterator=False)
        df = run(df, prefix)
        df.drop(drop_cols, axis=1, inplace=True, errors='ignore')

        save_path = os.path.join(save_dir, '%s_feature_vector_space.csv' % prefix)
        tmp = pd.concat(feature, axis=0)
        tmp.to_csv(save_path, index=None)  # 带表头
        print("file saved to "+save_path)
        del feature, tmp
        gc.collect()