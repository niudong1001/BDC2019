import os

ROOT_DIR = os.path.abspath('../')
DEBUG = False

INPUT_DIR = '%s/input/' % ROOT_DIR
OUTPUT_DIR = '%s/output/' % ROOT_DIR

GLOBAL_DIR = os.path.abspath('../../global/')

IN_TRAIN_FEATURE = INPUT_DIR + "train_v1_feature_text.npy"
IN_TRAIN_LABEL = INPUT_DIR + "train_labels.npy"
IN_TEST_FEATURE = INPUT_DIR + "test_v1_feature_text.npy"

if DEBUG:
  # Just use in offline
  IN_TEST_LABEL = INPUT_DIR + "test_labels.npy"

OUTPUT_TRAIN_DIR = OUTPUT_DIR + "train/"
OUTPUT_TEST_DIR = OUTPUT_DIR + "test/"

K_FOLD = 5