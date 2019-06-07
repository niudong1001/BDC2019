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
parser.add_argument('-s', '--save-model', type=str, help='file name for save model')
args = parser.parse_args()

if not args.file or not os.path.isfile(args.file):
    print("Not a valid file.")
    exit()
if not args.save_dir or not os.path.isdir(args.save_dir):
    print("Not a valid dir.")
    exit()

if __name__ == "__main__":

  # python build_fastText.py -f "../input/fastText_labeled_content.txt" -d "../output/" -s "fastText_supervised.bin"

  # !head -n 90000000 labeled_content > train.txt
  # !tail -n 10000000 labeled_content > valid.txt
  
  with Timer("Train fastText"):
    model = train_supervised(
        input=args.file, epoch=25, lr=0.1, wordNgrams=2, verbose=2, minCount=5
    )
    model.save_model(os.path.join(args.save_dir, args.save_model))