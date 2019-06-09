'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-07 12:42:29
@LastEditTime: 2019-06-09 16:48:37
'''
import csv
import os
import sys
import config
sys.path.append(config.GLOBAL_DIR)
from helper import Timer
import argparse
import fastText
from fastText import train_supervised, train_unsupervised

# 除去 query_id 和 title_id 转换成 raw content 的，按行写入文件。
def ProcessForTrainFastText(source_csv, savefile, add_label=True):
    with Timer("Process csv to content for fastText train"):
        with open(savefile, 'w') as f:
            with open(source_csv) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    line_count += 1
                    query = row[1]
                    title = row[3]
                    if add_label:
                        label = row[4]
                        f.write("__label__{0} {1} {2}\n".format(label, query, title))
                    else:
                        f.write("{0} {1}\n".format(query, title))
                    if line_count % 5000000 == 0:
                        print(f'Processed {line_count} lines.')
                        
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