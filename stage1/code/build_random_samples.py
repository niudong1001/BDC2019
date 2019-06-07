import sys
import config
sys.path.append(config.GLOBAL_DIR)
from helper import Timer, RandomSample, ORI_TRAIN_NAMES, DEBUG_CHUNK_SIZE, CHUNK_SIZE
import argparse
import os

parser = argparse.ArgumentParser(description='Random select samples.')
parser.add_argument('-f', '--file', type=str, help='file name to process')
parser.add_argument('-r', '--rate', type=float, help='rate to select', default=.1)
parser.add_argument('-d', '--save-dir', type=str, help='dir for save')
parser.add_argument('-s', '--save-file', type=str, help='file name for save')
parser.add_argument('-b', '--debug', type=str, help='is debug', default="true")
args = parser.parse_args()

if not args.save_dir or not os.path.isdir(args.save_dir):
    print("Not a valid dir.")
    exit()

if __name__ == "__main__":

  # python ./build_random_samples.py -f "/home/kesci/input/bytedance/first-round/train.csv" -r .1 -d ../input/ -s "train_01_0607.csv"

  with Timer("Build random samples"):

    if args.debug == "true":
        chunk_size = DEBUG_CHUNK_SIZE
    else:
        chunk_size = CHUNK_SIZE

    RandomSample(args.file, args.rate, names=ORI_TRAIN_NAMES, chunk_size=chunk_size).to_csv(
      os.path.join(args.save_dir, args.save_file), header=None, index=None
    )
