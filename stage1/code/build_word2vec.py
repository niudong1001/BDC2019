'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-04 23:34:43
@LastEditTime: 2019-06-10 22:30:06
'''
import csv
import os
import sys
from .config import GLOBAL_DIR
sys.path.append(GLOBAL_DIR)
from helper import Timer
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


class SentenceStream(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for line in open(self.dirname):
            yield line.split()


def PrepareWord2vecSamples(source_csv, save_file):
    query_id = -1
    with Timer("Prepare for word2vec samples"):
        with open(save_file, 'w') as f:
            with open(source_csv) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    line_count += 1
                    if query_id != row[0]:
                        query_id = row[0]
                        f.write("{0}\n".format(row[1]))
                    f.write("{0}\n".format(row[3]))
                    if line_count % 5000000 == 0: 
                        print(f'Processed {line_count} lines.')


def TrainWord2vec(source_file, save_name):
    with Timer("Train word2vec"):
        # sentences = SentenceStream(source_file)
        # https://rare-technologies.com/word2vec-tutorial/
        # https://radimrehurek.com/gensim/models/word2vec.html
        # https://blog.csdn.net/szlcw1/article/details/52751314
        # https://github.com/lzhenboy/word2vec-Chinese/blob/master/word2vec_train.py
        # https://www.jianshu.com/p/6a34929c165e
        model = Word2Vec(LineSentence(source_file), size=200, window=5, min_count=5, workers=4, batch_words=500000)
        model.save(save_name+".model")
        model.wv.save(save_name+".kv")
        # model.wv.save_word2vec_format(save_file,binary=False)