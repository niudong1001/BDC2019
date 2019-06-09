import sys
from .config import GLOBAL_DIR
sys.path.append(GLOBAL_DIR)
from helper import Timer, RandomSample, CHUNK_SIZE, ORI_TRAIN_NAMES, ORI_TRAIN_DTYPE, usetime, ReadCSV
import pandas as pd
import os
import gc


def RandomSampleCSV(source_csv, save_file, rate, names=ORI_TRAIN_NAMES, dtype=ORI_TRAIN_DTYPE, chunk_size=CHUNK_SIZE):
  with Timer("Random sample"):
    tmp = RandomSample(source_csv, rate, names=names, dtype=dtype, chunk_size=chunk_size)
    print(tmp.info())
    tmp.to_csv(
      save_file, header=False, index=None
    )
    del tmp
    gc.collect()

def SampleCSV(source_csv, save_file, count, names=ORI_TRAIN_NAMES, dtype=ORI_TRAIN_DTYPE):
  with Timer("Sample"):
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