'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-09 11:44:03
@LastEditTime: 2019-06-13 23:31:08
'''
import os
import sys
import csv
import gc
import pandas as pd
import numpy as np
from datetime import datetime
from .config import GLOBAL_DIR
sys.path.append(GLOBAL_DIR)
from helper import ProcessChunk, ReadCSV, CHUNK_SIZE, Timer


# 提取label列并存储
def ExtractTrainLabel(source_csv, savefile):
    with Timer("Extract label"):
        with open(source_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # no header
            labels = np.array([int(_[-1]) for _ in csv_reader])
            print("labels shape:", labels.shape)
            np.save(savefile, labels)
            print("Label file saved to "+savefile)
            del labels
            gc.collect()


# 将特征csv转化为npy
def ConvertCSVToNPY(source_csv, savefile, rm_header=True):
    with Timer("Convert CSV To NPY"):
        tmp = np.array(ReadCSV(source_csv, iterator=False))
        print("csv file shape:", tmp.shape)
        np.save(savefile, tmp)
        print("Npy file saved to "+savefile)
        del tmp
        gc.collect()


# 合并所有特征
def CombineFeatures(feature_files, savefile):
    # 拼接特征
    with Timer("Concat features"):
        features = pd.concat([
            ReadCSV(f, iterator=False) for f in feature_files], 
            axis=1)
    # change inf to nan
    with Timer("Change inf to nan"):
        features = features.astype(dtype=np.float32)
        inf = np.nan_to_num(np.inf)
        features = features.replace(inf, np.nan)
    # fill nan
    with Timer("Fill nan"):
        features = features.fillna(0.0)
    features.to_csv(savefile, index=None)
    del features
    gc.collect()