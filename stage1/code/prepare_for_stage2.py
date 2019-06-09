import os
import sys
import csv
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
            labels = [int(_[-1]) for _ in csv_reader]
            print("Part of labels:", labels[:10])
            np.save(savefile, np.array(labels))
            print("Label file saved to "+savefile)


# 将csv转化为npy
def ConvertCSVToNPY(source_csv, savefile, rm_header=True):
    with Timer("Convert CSV To NPY"):
        with open(source_csv) as csv_file:
            csv_reader= csv.reader(csv_file, delimiter=',')
            if rm_header: next(csv_reader)
            res = [list(map(float, _)) for _ in csv_reader]
            print("Part of rows:", res[:2])
            np.save(savefile, np.array(res))
            print("Npy file saved to "+savefile)