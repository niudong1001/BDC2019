
import pandas as pd
import numpy as np
import time
import random
import gc
import sys
import csv

ORI_TRAIN_NAMES = ["query_id", "query", "query_title_id", "title", "label"]
ORI_TEST_NAMES = ["query_id", "query", "query_title_id", "title"]
DEBUG_CHUNK_SIZE = 5000
CHUNK_SIZE = 5000000

# 计算执行某个函数需要的时间
class Timer(object):
    """
    Record the consumed time when ran a code block.
    """
    def __init__(self, block_name, prefix="----->"):
        self.block_name = block_name
        self.prefix = prefix

    def __enter__(self):
        print(self.prefix+"Started '"+self.block_name+"' block...")
        self.time_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = round(time.time() - self.time_start, 2)
        print(self.prefix+"Finished '"+self.block_name+"' block, time used:", str(elapsed_time)+"s.")


# 读取CSV文件
def ReadCSV(filename, names, sep=",", iterator=True):
    # http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv
    return pd.read_csv(
        filename, 
        names=names,
        sep=sep,
        iterator=iterator
    )


# 批量读入数据，并apply处理函数
def ProcessChunk(filename, func, names, chunk_size=5000000):
    reader = ReadCSV(filename, names, iterator=True)
    while True:
        try:
            print("Reading chunk...")
            func(reader.get_chunk(chunk_size))
        except StopIteration:
            print("Finished process.")
            return
# def handle(x):
#     print(x)
#     print()
# ProcessChunk(train_data_file, handle, names=ori_train_names, chunk_size=5)


# 按照rate比例从每个chunk中随机采样样本
def RandomSample(filename, rate, names, chunk_size=1000000, random_state=None):
    print("Random sample...")
    reader = ReadCSV(filename, names, iterator=True)
    chunks = []
    while True:
        try:
            # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html
            chunks.append(reader.get_chunk(chunk_size).sample(
                n=int(chunk_size*rate), 
                random_state=random_state)
            )
        except StopIteration:
            print("Finished sample.")
            break
    # 删除无用引用, https://blog.csdn.net/jiangjiang_jian/article/details/79140742
    # for x in locals().keys():
    #     if x != "res":
    #         # 会被放入内存池？
    #         del locals()[x]
    # gc.collect()
    return pd.concat(chunks, ignore_index=True)
# tmp = RandomSample(train_data_file, .5, chunk_size=5)
# print(tmp)

# Stage1

def ProcessForTrainWord2vec(source_csv, embed_sentences_file):
    query_id = -1
    with Timer("Process csv to embedding sentences"):
        with open(embed_sentences_file, 'w') as f:
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