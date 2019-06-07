import csv
import os
import sys
import config
sys.path.append(config.GLOBAL_DIR)
from helper import Timer
import argparse
import fastText
from fastText import train_supervised, train_unsupervised

parser = argparse.ArgumentParser(description='Build fastText.')
parser.add_argument('-f', '--file', type=str, help='file to process')
parser.add_argument('-d', '--save-dir', type=str, help='dir for save')
parser.add_argument('-m', '--save-model', type=str, help='file name for save model')
parser.add_argument('-v', '--save-vector', type=str, help='file name for save vector')
parser.add_argument('-b', '--debug', type=str, help='is debug', default="true")
args = parser.parse_args()


if __name__ == "__main__":
  pass
