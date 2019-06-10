'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-08 10:22:21
@LastEditTime: 2019-06-10 22:49:15
'''
import os

ROOT_DIR = os.path.abspath('./stage2/')

INPUT_DIR = '%s/input/' % ROOT_DIR
OUTPUT_DIR = '%s/output/' % ROOT_DIR

GLOBAL_DIR = os.path.abspath('./global/')

OUTPUT_TRAIN_DIR = OUTPUT_DIR + "train/"
OUTPUT_TEST_DIR = OUTPUT_DIR + "test/"

K_FOLD = 10