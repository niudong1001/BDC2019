import csv
import os
import sys
import config
sys.path.append(config.GLOBAL_DIR)
from helper import Timer
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


embed_sentences = config.INPUT_DIR +'/embed_sentences.txt'
source_csv = config.INPUT_DIR + '/train_data.csv'
word2vec_model = config.OUTPUT_DIR +'/word2vec.model'
word2vec_kv = config.OUTPUT_DIR +'/word2vec.kv'

def ProcessForEmbedsInput():
    query_id = -1
    with Timer("Process to embedding sentences"):
        with open(embed_sentences, 'w') as f:
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

class SentenceStream(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for line in open(self.dirname):
            yield line.split()

# a memory-friendly iterator
sentences = SentenceStream(embed_sentences) 

with Timer("Train word2vec"):
    # https://www.cnblogs.com/pinard/p/7278324.html
    # https://radimrehurek.com/gensim/models/word2vec.html
    model = Word2Vec(sentences, size=200, window=5, min_count=5, workers=4)
    model.save(word2vec_model)
    model.wv.save(word2vec_kv)
