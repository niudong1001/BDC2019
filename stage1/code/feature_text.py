import os
import argparse
import pandas as pd
from datetime import datetime
from utils import dist, ngram_util

parser = argparse.ArgumentParser(description='Exctract the pos and ner features.')
parser.add_argument('-f', '--file', type=str, help='file name to process')
parser.add_argument('-p', '--prefix', type=str, help='prefix for features')
parser.add_argument('-d', '--save-dir', type=str, help='dir for save')
args = parser.parse_args()
if not args.file or not os.path.isfile(args.file):
    exit()
if not args.save_dir or not os.path.isdir(args.save_dir):
    exit()


def run(df, ngram, prefix):
    # ngram
    df['q_ngram'] = df['query'].apply(ngram)
    df['t_ngram'] = df['title'].apply(ngram)

    ## 长度特征
    df['%s_q-len' % prefix] = df['q_ngram'].apply(len)
    df['%s_t-len' % prefix] = df['t_ngram'].apply(len)

    ## 字符集合相似度
    df['%s_dice-ratio'% prefix] = df.apply(lambda x: dist_utils.dice_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_jaccard-ratio'% prefix] = df.apply(lambda x: dist_utils.jaccard_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_edit-seq-ratio'% prefix] = df.apply(lambda x: dist_utils.edit_seq_ratio(x['q_ngram'], x['t_ngram']), axis=1)
    df['%s_edit-set-ratio'% prefix] = df.apply(lambda x: dist_utils.edit_set_ratio(x['q_ngram'], x['t_ngram']), axis=1)

    df.drop(['q_ngram', 't_ngram'], axis=1, inplace=True)
    return df

if __name__ == '__main__':
    start_time = datetime.now()
    df = pd.read_csv(args.file, index_col=0, dtype=str)
    df = df.fillna('')
    print('Lines: %d' %len(df))

    # df = run(df, ngram_utils.unichars, '%s_%s' % (args.prefix, 'unichars'))
    # df = run(df, ngram_utils.bichars, '%s_%s' % (args.prefix, 'bichars'))
    # df = run(df, ngram_utils.trichars, '%s_%s' % (args.prefix, 'trichars'))
    df = run(df, ngram_utils.unigrams, '%s_%s' % (args.prefix, 'unigrams'))
    df = run(df, ngram_utils.bigrams, '%s_%s' % (args.prefix, 'bigrams'))
    df = run(df, ngram_utils.trigrams, '%s_%s' % (args.prefix, 'trigrams'))

    # save
    df.drop(['query', 'title', 'clicked'], axis=1, inplace=True, errors='ignore')
    save_path = os.path.join(args.save_dir, '%s_feature_text.csv' % args.prefix)
    df.to_csv(save_path)
    print('Use time: {}. Save file to {}'.format(datetime.now()-start_time, save_path))




        