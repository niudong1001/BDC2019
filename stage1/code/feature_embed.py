'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-04 23:04:29
@LastEditTime: 2019-06-09 16:48:51
'''
import config
import sys
sys.path.append(config.GLOBAL_DIR)
import os
import gensim
import argparse
import numpy as np
import pandas as pd
from datetime import datetime
from utils import dist_utils, ngram_utils
from scipy.stats import skew, kurtosis
from helper import ProcessChunk, ReadCSV, ORI_TRAIN_NAMES, ORI_TEST_NAMES, DEBUG_CHUNK_SIZE, CHUNK_SIZE

parser = argparse.ArgumentParser(description='Exctract embed features.')
parser.add_argument('-f', '--file', type=str, help='file name to process')
parser.add_argument('-p', '--prefix', type=str, help='prefix for features')
parser.add_argument('-d', '--save-dir', type=str, help='dir for save')
parser.add_argument('-e', '--embedding', type=str, help='embedding mode')
parser.add_argument('-b', '--debug', type=str, help='is debug', default="true")
parser.add_argument('-t', '--train', type=str, help='is train file', default="true")
args = parser.parse_args()

if not args.file or not os.path.isfile(args.file):
    print("Not a valid file.")
    exit()
if not args.save_dir or not os.path.isdir(args.save_dir):
    print("Not a valid dir.")
    exit()


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


# def norm_wmd(s1, s2):
#     dis = norm_model.wmdistance(s1, s2)
#     dis = np.nan_to_num(dis)
#     return dis if dis<100 else 100


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

if __name__ == '__main__':

    # python feature_embed.py -f ../input/train_data.csv  -e word2vec -p test -d ../output  
    global model

    if 'glove' in args.embedding:
        # model_file = config.GLOVE_MODEL
        exit()
    elif 'word2vec' in args.embedding:
        model_file = config.WORD2VEC_MODEL
    else :
        exit()

    model = gensim.models.KeyedVectors.load(model_file, mmap='r')
    # norm_model = gensim.models.KeyedVectors.load(model_file, mmap='r')
    # norm_model.init_sims(replace=True)

    start_time = datetime.now()
    feature = []

    def process(df):
        df = run(df, ngram_utils.unigrams, '%s_%s' % (args.prefix, 'unigrams'))
        if args.train == "true":
            df.drop(['query', 'title', 'label'], axis=1, inplace=True, errors='ignore')
        else:
            df.drop(['query', 'title'], axis=1, inplace=True, errors='ignore')
        feature.append(df)
    
    if args.debug == "true":
        chunk_size = DEBUG_CHUNK_SIZE
    else:
        chunk_size = CHUNK_SIZE

    if args.train == "true":
        ProcessChunk(args.file, process, names=ORI_TRAIN_NAMES, chunk_size=chunk_size)
    else:
        process(ReadCSV(args.file, names=ORI_TEST_NAMES, iterator=False))

    save_path = os.path.join(args.save_dir, '%s_feature_embed.csv' % args.prefix)
    pd.concat(feature, axis=0).to_csv(save_path, index=None) # 带表头
    print('Use time: {}. Save file to {}'.format(datetime.now()-start_time, save_path))