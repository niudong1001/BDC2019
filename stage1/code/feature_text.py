import os
import argparse
import pandas as pd
from datetime import datetime
from utils import dist_utils, ngram_utils
import numpy as np
import sys
import config
sys.path.append(config.GLOBAL_DIR)
from helper import ProcessChunk, ORI_TRAIN_NAMES, DEBUG_CHUNK_SIZE, CHUNK_SIZE

parser = argparse.ArgumentParser(description='Exctract text features.')
parser.add_argument('-f', '--file', type=str, help='file name to process')
parser.add_argument('-p', '--prefix', type=str, help='prefix for features')
parser.add_argument('-d', '--save-dir', type=str, help='dir for save')
parser.add_argument('-b', '--debug', type=str, help='is debug', default="true")
args = parser.parse_args()

if not args.file or not os.path.isfile(args.file):
    print("Not a valid file.")
    exit()
if not args.save_dir or not os.path.isdir(args.save_dir):
    print("Not a valid dir.")
    exit()


def run(df, ngram, prefix):

    # ngram
    df['q_ngram'] = df['query'].apply(ngram)
    df['t_ngram'] = df['title'].apply(ngram)

    ## 长度特征
    df['%s_q-len' % prefix] = df['q_ngram'].apply(lambda x: np.log1p(len(x)))
    df['%s_t-len' % prefix] = df['t_ngram'].apply(lambda x: np.log1p(len(x)))

    ## 字符集合相似度
    df['%s_dice-ratio'% prefix] = df.apply(lambda x: dist_utils.dice_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_jaccard-ratio'% prefix] = df.apply(lambda x: dist_utils.jaccard_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_edit-seq-ratio'% prefix] = df.apply(lambda x: dist_utils.edit_seq_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_edit-set-ratio'% prefix] = df.apply(lambda x: dist_utils.edit_set_ratio(x['q_ngram'], x['t_ngram']), axis=1)

    df.drop(['q_ngram', 't_ngram'], axis=1, inplace=True)

    return df

if __name__ == '__main__':

    # python feature_text.py -f "../input/train_01_0607.csv" -p "v1" -d "../output"
    
    start_time = datetime.now()
    feature = []

    def process(df):
        # df = run(df, ngram_utils.unichars, '%s_%s' % (args.prefix, 'unichars'))
        # df = run(df, ngram_utils.bichars, '%s_%s' % (args.prefix, 'bichars'))
        # df = run(df, ngram_utils.trichars, '%s_%s' % (args.prefix, 'trichars'))
        df = run(df, ngram_utils.unigrams, '%s_%s' % (args.prefix, 'unigrams'))
        df = run(df, ngram_utils.bigrams, '%s_%s' % (args.prefix, 'bigrams'))
        df = run(df, ngram_utils.trigrams, '%s_%s' % (args.prefix, 'trigrams'))
        df.drop(['query', 'title', 'label'], axis=1, inplace=True, errors='ignore')
        feature.append(df)
    
    if args.debug == "true":
        chunk_size = DEBUG_CHUNK_SIZE
    else:
        chunk_size = CHUNK_SIZE

    ProcessChunk(args.file, process, names=ORI_TRAIN_NAMES, chunk_size=chunk_size)

    save_path = os.path.join(args.save_dir, '%s_feature_text.csv' % args.prefix)
    pd.concat(feature, axis=0).to_csv(save_path, index=None)  # 带表头
    print('Use time: {}. Save file to {}'.format(datetime.now()-start_time, save_path))