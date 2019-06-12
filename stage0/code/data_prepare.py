'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-09 09:56:20
@LastEditTime: 2019-06-12 20:54:35
'''
import sys
from .config import GLOBAL_DIR
sys.path.append(GLOBAL_DIR)
from helper import Timer, RandomSample, CHUNK_SIZE, ORI_TRAIN_NAMES, ORI_TRAIN_DTYPE, usetime, ReadCSV
import pandas as pd
import os
import gc


# 随机采样训练数据集
def RandomSampleCSV(source_csv, save_file, rate, names=ORI_TRAIN_NAMES, dtype=ORI_TRAIN_DTYPE, chunk_size=CHUNK_SIZE):
  with Timer("Random sample"):
    tmp = RandomSample(source_csv, rate, names=names, dtype=dtype, chunk_size=chunk_size)
    print(tmp.info())
    tmp.to_csv(
      save_file, header=False, index=None
    )
    del tmp
    gc.collect()


# 顺序采样数据集
def SampleCSV(source_csv, save_file, count, names=ORI_TRAIN_NAMES, dtype=ORI_TRAIN_DTYPE):
  with Timer("Orderly Sample"):
    reader = ReadCSV(source_csv, names, dtype, iterator=True)
    while True:
      try:
          tmp = reader.get_chunk(count)
          print(tmp.info())
          tmp.to_csv(
            save_file,
            header=False, 
            index=None
          )
          del tmp
          gc.collect()
          return
      except StopIteration:
          return

# 按照比例顺序采样
def SampleWithRate(source_csv, save_file, rate, names=ORI_TRAIN_NAMES, dtype=ORI_TRAIN_DTYPE, chunk_size=CHUNK_SIZE):
    with Timer("Sample with rate"):
        if os.path.exists(save_file):
          os.remove(save_file)  # 移除原本的文件，因为是增量存储
        reader = ReadCSV(source_csv, names, dtype, iterator=True)
        while True:
            try:
                print("processing chunk...")
                tmp = reader.get_chunk(chunk_size)[-int(chunk_size*rate):]
                tmp.to_csv(
                    save_file,
                    header=None,
                    index=None,
                    mode='a'
                )
                del tmp
                gc.collect()
            except StopIteration:
                print("Finished process.")
                return