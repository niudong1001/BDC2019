'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-02 21:57:56
@LastEditTime: 2019-06-09 16:48:47
'''
import os

ROOT_DIR = os.path.abspath('./stage1/')
INPUT_DIR = '%s/input'% ROOT_DIR
OUTPUT_DIR = '%s/output'% ROOT_DIR

GLOBAL_DIR = os.path.abspath('./global')

WORD2VEC_MODEL = OUTPUT_DIR + "/word2vec.kv"