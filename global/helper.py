
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


OFFLINE = True  # 是否为离线，本地调试为True，上线为False
ORI_TRAIN_NAMES = ["query_id", "query", "query_title_id", "title", "label"]
# 关于数据类型所占内存（https://blog.csdn.net/xingkong_dahai/article/details/77140918）
# 具体转换参考（https://www.jianshu.com/p/d54fc84f3b42）
ORI_TRAIN_DTYPE = {"query_id":np.uint32, "query":np.object, "query_title_id":np.uint32, "title":np.object, "label":np.uint8}

ORI_TEST_NAMES = ["query_id", "query", "query_title_id", "title"]
ORI_TEST_DTYPE = {"query_id":np.uint32, "query":np.object, "query_title_id":np.uint32, "title":np.object}

if OFFLINE:
    CHUNK_SIZE = 5000
else:
    CHUNK_SIZE = 1000000


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


# 使用装饰器计算函数所需时间
def usetime(desc=None):
    def _usetime(func):
        def __usetime(*args, **kwargs):
            print("-------------------------------------")
            # if desc: print('[Description]: ' + desc)
            print('[Runing function]: [%s] ' % func.__name__)
            stime = datetime.now()
            res = func(*args, **kwargs)
            utime = datetime.now() - stime
            print('[Used Time]: {}'.format(utime))
            print("-------------------------------------")
            return res
        return __usetime
    return _usetime


# 读取CSV文件
def ReadCSV(filename, names, dtype, sep=",", iterator=True):
    # http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv
    return pd.read_csv(
        filename, 
        names=names,
        sep=sep,
        iterator=iterator,
        dtype=dtype
    )


# 批量读入数据，并apply处理函数
def ProcessChunk(filename, func, names, dtype, chunk_size=CHUNK_SIZE):
    reader = ReadCSV(filename, names, dtype, iterator=True)
    while True:
        try:
            print("Reading chunk...")
            tmp = reader.get_chunk(chunk_size)
            func(tmp)
            del tmp
            gc.collect()
        except StopIteration:
            print("Finished process.")
            return
# def handle(x):
#     print(x)
#     print()
# ProcessChunk(train_data_file, handle, names=ori_train_names, chunk_size=5)


# 按照rate比例从每个chunk中随机采样样本
def RandomSample(filename, rate, names, dtype, chunk_size=CHUNK_SIZE, random_state=0):
    print("Random sample...")
    reader = ReadCSV(filename, names, dtype, iterator=True)
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
    res = pd.concat(chunks, ignore_index=True)
    del chunks
    gc.collect()
    return res
# tmp = RandomSample(train_data_file, .5, chunk_size=5)
# print(tmp)

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


def cp(srcfile, dstfile):
    if os.path.isfile(srcfile):
        shutil.copyfile(srcfile, dstfile)
    else:
        print("srcfile not exist!")
        return