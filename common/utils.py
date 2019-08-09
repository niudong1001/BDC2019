'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-01 11:19:50
@LastEditTime: 2019-08-09 21:02:43
'''
import gc, os, sys, csv, json, random, time, shutil
from datetime import datetime
from sklearn.metrics import roc_auc_score
import pandas as pd
import numpy as np
import multiprocessing
from multiprocessing import Pool

NUM_CORES = multiprocessing.cpu_count()
ORI_TRAIN_NAMES = ["query_id", "query", "query_title_id", "title", "label"]
ORI_TEST_NAMES = ["query_id", "query", "query_title_id", "title"]


class Timer(object):
    def __init__(self, block_name, prefix="----->"):
        self.block_name = block_name
        self.prefix = prefix

    def __enter__(self):
        print(self.prefix+"started '"+self.block_name+"' block...")
        self.time_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = round(time.time() - self.time_start, 2)
        print(self.prefix+"finished '"+self.block_name+"' block, time used:" + str(elapsed_time)+"s.")


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


# 读取CSV文件
def ReadCSV(filename, names=None, sep=",", iterator=True):
    # http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv
    return pd.read_csv(
        filename, 
        names=names,
        sep=sep,
        iterator=iterator
    )


# 批量读入数据，并apply处理函数
def ProcessChunk(filename, func, chunk_size, names=None, params=None):
    reader = ReadCSV(filename, names=names, iterator=True)
    with Timer("process chunk"):
        while True:
            try:
                block = reader.get_chunk(chunk_size)
                func(block, params)
                del block
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


def ReadCSV1(filename, cols=["query", "title"]):
    count, res = 0, [[] for _ in cols]
    cols_map = {
        "query_id": 0,
        "query": 1,
        "query_title_id": 2,
        "title": 3,
        "label": 4
    }
    f = open(filename, "r")
    lines = f.readlines()  # 读取所有行
    print("read {} file, total {} lines".format(filename, len(lines)))
    for line in lines:
        count += 1
        new_line = line.strip().split(",")
        for i, _ in enumerate(cols):
            res[i].append(new_line[cols_map[_]])
        if count % 10000000 == 0:
            print("count:", count)
    f.close()
    del lines; gc.collect()
    return {key: res[i] for i, key in enumerate(cols)}


# 提取feature函数
def ExtractFeature(source_csv, save_dir, prefix, feature_name, 
    process_func, names=None, process_chunkly=False, chunk_size=None, 
    drop_first_cols=['query_id', 'query_title_id', 'label'], 
    drop_last_cols=['query', 'title'], reduce_mem=False):

    with Timer("extract {} feature".format(feature_name)):
        
        basefilename = os.path.join(save_dir, 
        '%s_%s' % (prefix, feature_name))
        save_path = basefilename + ".h5"
        res = []

        def process(df, params=None):
            # 先丢弃不需要的部分，避免长时间占用内存
            df.drop(drop_first_cols, axis=1, inplace=True, errors='ignore')
            # 优化内存使用
            if reduce_mem: df = ReduceMemUsage(df)
            # 提取特征
            df = process_func(df, save_dir, prefix, feature_name)
            # 如果有结果返回
            if type(df) == pd.core.frame.DataFrame:
                # 丢弃剩下的部分
                df.drop(drop_last_cols, axis=1, inplace=True, errors='ignore')
                # 压入结果
                res.append(df)

        if process_chunkly:
            ProcessChunk(
                source_csv, 
                names=names,
                func=process, 
                chunk_size=chunk_size
            )
        else:
            process(
                ReadCSV(
                    source_csv, 
                    names=names,
                    iterator=False
                )
            )
        if res:
            with Timer("save feature"):
                result = pd.concat(res)
                result.to_hdf(save_path, mode="w", key="df", complib="bzip2", complevel=9)
                print("saved {} feature to {}".format(feature_name, save_path))
                del result, res
                gc.collect()


def ExtractFeature1(train_csv, test_csv, train_name, test_name, process_func, save_dir, prefix, feature_name):
    
    with Timer("extract {} feature".format(feature_name)):
        
        train_df = pd.read_csv(train_csv, names=train_name)
        test_df = pd.read_csv(test_csv, names=test_name)
        train_len = train_df.shape[0]
        concat_df = pd.concat([train_df[['query', 'title']], test_df[['query', 'title']]], axis=0)
        del train_df, test_df
        gc.collect()
        
        df = process_func(concat_df, save_dir, prefix, feature_name)
        
        if type(df) == pd.core.frame.DataFrame:
            df.drop(["query", "title"], axis=1, inplace=True, errors='ignore')
            with Timer("save feature"):
                train_save_path = os.path.join(save_dir, '%s_%s_%s.h5' % ("train", prefix, feature_name))
                test_save_path = os.path.join(save_dir, '%s_%s_%s.h5' % ("test", prefix, feature_name))
                df[:train_len].to_hdf(train_save_path, mode="w", key="df", complib="bzip2", complevel=9)
                df[train_len:].to_hdf(test_save_path, mode="w", key="df", complib="bzip2", complevel=9)
                print("saved train feature {} to {}".format(feature_name, train_save_path))
                print("saved test feature {} to {}".format(feature_name, test_save_path))
                del df; gc.collect()


def ConcatFeatures(source_files, save_file_name, verbose=True, save_feature_name=True):
    with Timer("load features"):
        tmp = [ReduceMemUsage(pd.read_hdf(f)) for f in source_files]
        features = pd.concat(tmp, axis=1)
        del tmp; gc.collect()
    with Timer("deal with invalid values"):
        features = features.replace(np.inf, np.nan)
        features = features.fillna(0.0)
    if verbose:
        print("features shape:", features.shape)
        print("two rows of features:")
        print(features[:2])
    save_file = "{}.npy".format(save_file_name)
    if save_feature_name:
        save_names_file = "{}_name.csv".format(save_file_name)
        with open(save_names_file, "w") as f:
            feature_names = ",".join(list(features.columns.values))
            if verbose:
                print(list(features.columns.values))
            f.write(feature_names)
            print("concat features names saved to {}".format(save_names_file))
    np.save(save_file, features.values)
    print("concat features saved to {}".format(save_file))
    del features; gc.collect()


# 分析csv文件，注意尽量不要操作大文件
def AnalysisCSV(source_csv, print_rows=2, names=None):
    data = ReadCSV(source_csv, names=names, iterator=False)
    print("--->file shape:")
    print(data.shape)
    print("--->{} rows of file:".format(print_rows))
    if print_rows >= 0:
        print(data[:print_rows])
    else:
        print(data[print_rows:])
    # print("--->file info:")
    # print(data.info())
    # print("--->file describe:")
    # print(data.describe())
    del data
    gc.collect()


# 分析h5文件，注意尽量不要操作大文件
def AnalysisHDF(source_h5, print_rows=2):
    data = pd.read_hdf(source_h5)
    print("--->file shape:")
    print(data.shape)
    print("--->{} rows of file:".format(print_rows))
    print(data[:print_rows])
    del data
    gc.collect()


def CalQAuc(df):
    auc_score = []
    for name, group in df.groupby('query_id'):
        try:
            auc_score.append(roc_auc_score(group["label"], group["prediction"]))
        except:
            auc_score.append(0.5)
    return np.mean(auc_score)


def FuncMap2(func, a, b):
    return list(map(func, a, b))


def FuncMap1(func, a):
    return list(map(func, a))


def parallelize_map1(func, df, num_partitions=NUM_CORES-4, num_cores=NUM_CORES-2):
    if type(df) in [np.ndarray, list]:
        with Timer("mapping1"):
            pool = Pool(num_cores)
            tmp = pool.map(func, np.array_split(df, num_partitions))
            pool.close()
            pool.join()
        with Timer("prepare data"):
            res = []
            for _ in tmp:
                res.extend(_)
        del tmp, df, pool; gc.collect()
        return res
    else:
        raise ValueError("df must be a valid type ([np.ndarray, list])!")
    
    
def parallelize_map2(func, df1, df2, num_partitions=NUM_CORES-4, num_cores=NUM_CORES-2):
    if type(df1) in [np.ndarray, list] and type(df2) in [np.ndarray, list]:
        with Timer("mapping2"):
            pool = Pool(num_cores)
            c = zip(np.array_split(df1, num_partitions), 
                np.array_split(df2, num_partitions))
            tmp = pool.starmap(func, c)
            pool.close(); pool.join()
        with Timer("prepare data"):
            res = []
            for _ in tmp:
                res.extend(_)
        del c, tmp, df1, df2, pool; gc.collect()
        return res
    else:
        raise ValueError("df1 and df2 must be valid type ([np.ndarray, list])!")
        