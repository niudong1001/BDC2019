'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-01 11:19:50
@LastEditTime: 2019-06-23 20:48:07
'''

import pandas as pd
import numpy as np
import time
import random
import gc
import sys
import csv
import json 
from datetime import datetime
import shutil
import os
from sklearn.metrics import roc_auc_score
import tqdm


OFFLINE = True
CAL_Q_AUC = False


ORI_TRAIN_NAMES = ["query_id", "query", "query_title_id", "title", "label"]
# 关于数据类型所占内存（https://blog.csdn.net/xingkong_dahai/article/details/77140918）; 具体转换参考（https://www.jianshu.com/p/d54fc84f3b42）
ORI_TRAIN_DTYPE = {"query_id":np.uint32, "query":np.object, "query_title_id":np.uint32, "title":np.object, "label":np.uint8}

ORI_TEST_NAMES = ["query_id", "query", "query_title_id", "title"]
ORI_TEST_DTYPE = {"query_id":np.uint32, "query":np.object, "query_title_id":np.uint32, "title":np.object}


CHUNK_SIZE = 1000000


# Record the consumed time when ran a code block.
class Timer(object):
    def __init__(self, block_name, prefix="----->"):
        self.block_name = block_name
        self.prefix = prefix

    def __enter__(self):
        print(self.prefix+"Started '"+self.block_name+"' block...")
        self.time_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = round(time.time() - self.time_start, 2)
        print(self.prefix+"Finished '"+self.block_name+"' block, time used:" + str(elapsed_time)+"s.")


# 读取CSV文件
def ReadCSV(filename, names=None, dtype=None, sep=",", iterator=True):
    # http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv
    return pd.read_csv(
        filename, 
        names=names,
        dtype=dtype,
        sep=sep,
        iterator=iterator
    )


# 批量读入数据，并apply处理函数
def ProcessChunk(filename, func, names=None, dtype=None, chunk_size=CHUNK_SIZE):
    reader = ReadCSV(filename, names, dtype, iterator=True)
    while True:
        try:
            with Timer("read chunk"):
                tmp = reader.get_chunk(chunk_size)
            with Timer("process chunk"):
                func(tmp)
            # 删除chunk数据
            del tmp
            gc.collect()
        except StopIteration:
            print("finished process.")
            return


# Json转换的类
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        else:
            return super(MyEncoder, self).default(obj)
            

# 减少df的内存
def ReduceMemUsage(df, verbose=True):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2    
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)    
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    return df


# 提取feature函数
def ExtractFeature(source_csv, save_dir, prefix, feature_name, process_func, names=None, dtype=None, process_chunkly=True, chunk_size=CHUNK_SIZE, drop_first_cols=['query_id', 'query_title_id', 'label'], drop_last_cols=['query', 'title']):

    with Timer("extract {} feature".format(feature_name)):
        
        basefilename = os.path.join(save_dir, 
        '%s_%s' % (prefix, feature_name))
        save_path = basefilename + ".csv.gz"
        # 存在则移除，注意会覆盖
        if os.path.exists(save_path):
            os.remove(save_path)

        def process(df):
            # 先丢弃不需要的部分，避免长时间占用内存
            df.drop(drop_first_cols, axis=1, inplace=True, errors='ignore')
            # 优化内存使用
            df = ReduceMemUsage(df)
            # 提取特征
            df = process_func(df, prefix, basefilename)
            # 如果有结果返回
            if type(df) == pd.core.frame.DataFrame:
                # 丢弃剩下的部分
                df.drop(drop_last_cols, axis=1, inplace=True, errors='ignore')
                # 增量存储
                add_header = True
                if os.path.exists(save_path): add_header = False
                df.to_csv(save_path, index=None, mode="a", header=add_header, compression='gzip')  # 带表头
                print("saved {} feature to {}".format(feature_name, save_path))
                del df
                gc.collect()

        if process_chunkly:
            ProcessChunk(
                source_csv, process, 
                names=names, dtype=dtype,
                chunk_size=chunk_size
            )
        else:
            process(
                ReadCSV(source_csv, names=names, 
                dtype=dtype, iterator=False)
            )

# 分析csv文件，注意尽量不要操作大文件
def AnalysisCSV(source_csv, print_rows=2, names=None, dtype=None):
    tmp = ReadCSV(source_csv, names=names, dtype=dtype, iterator=False)
    print("--->file shape:")
    print(tmp.shape)
    print("--->{} rows of file:".format(print_rows))
    print(tmp[:print_rows])
    print("--->file info:")
    print(tmp.info())
    print("--->file describe:")
    print(tmp.describe())
    del tmp
    gc.collect()
    
    
def CalQAuc(df):
    # invalid_count = 0
    # query_ids = df['query_id'].unique()
    # aucs = []
    # for query_id in query_ids:
    #     current = df[df['query_id'] == query_id]
    #     if sum(current['label']) not in [0, len(current['label'])]:
    #         auc = roc_auc_score(current['label'], current['prediction'])  # 这里计算qauc
    #     else:
    #         auc = 0.5
    #         invalid_count += 1
    #     aucs.append(auc)
    # print(f'q_auc invalid_count = {invalid_count}')
    # return np.mean(aucs)

    auc_score = []
    for name, group in df.groupby('query_id'):
        try:
            auc_score.append(roc_auc_score(group["label"], group["prediction"]
                                       ))
        except:
            auc_score.append(0.5) 

    return np.mean(auc_score)


def cal_sim(a, b, func):
    return list(map(func, a, b))