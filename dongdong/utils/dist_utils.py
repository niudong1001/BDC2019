'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-03 21:56:31
@LastEditTime: 2019-08-09 21:05:24
'''
import lzma
import Levenshtein
from np_utils import try_divide
import numpy as np
from difflib import SequenceMatcher
from scipy.spatial.distance import cosine, jaccard, cityblock, canberra, euclidean, minkowski, braycurtis, mahalanobis

def edit_dist(str1, str2):
    try:
        # very fast
        # http://stackoverflow.com/questions/14260126/how-python-levenshtein-ratio-is-computed
        import Levenshtein
        d = Levenshtein.distance(str1, str2) / float(max(len(str1), len(str2)))
    except:
        # https://docs.python.org/2/library/difflib.html
        d = 1. - SequenceMatcher(lambda x: x == " ", str1, str2).ratio()
    return d

def is_str_match(str1, str2, threshold=0.8):
    assert threshold >= 0.0 and threshold <= 1.0, "Wrong threshold."
    if float(threshold) == 1.0:
        return str1 == str2
    else:
        return (1. - edit_dist(str1, str2)) >= threshold

def longest_match_size(str1, str2):
    sq = SequenceMatcher(lambda x: x == " ", str1, str2)
    match = sq.find_longest_match(0, len(str1), 0, len(str2))
    return match.size

def longest_match_ratio(str1, str2):
    sq = SequenceMatcher(lambda x: x == " ", str1, str2)
    match = sq.find_longest_match(0, len(str1), 0, len(str2))
    return try_divide(match.size, min(len(str1), len(str2)))

def compression_dist(x, y, l_x=None, l_y=None):
    if x == y:
        return 0
    x_b = x.encode('utf-8')
    y_b = y.encode('utf-8')
    if l_x is None:
        l_x = len(lzma.compress(x_b))
        l_y = len(lzma.compress(y_b))
    l_xy = len(lzma.compress(x_b + y_b))
    l_yx = len(lzma.compress(y_b + x_b))
    dist = try_divide(min(l_xy, l_yx) - min(l_x, l_y), max(l_x, l_y))
    return dist

# One line time: 36.7 µs ± 388 ns
def edit_set_ratio(a, b):
    return Levenshtein.setratio(list(a), list(b))


# One line time: 20.7 µs ± 1.25 µs
def edit_seq_ratio(a, b):
    return Levenshtein.seqratio(list(a), list(b))


# One line time: 4.38 µs ± 134 ns
def jaccard_ratio(a, b):
    a, b = set(a), set(b)
    c = a & b
    return try_divide(len(c), len(a) + len(b) - len(c))


# One line time: 4.2 µs ± 109 ns
def dice_ratio(a, b):
    a, b = set(a), set(b)
    return try_divide(2 * len(a & b), len(a) + len(b))


def cosine_distance(a, b):
    return np.nan_to_num(try_divide(np.dot(a, b), 
    np.linalg.norm(a) * np.linalg.norm(b)))


def jaccard_distance(a, b):
    return np.nan_to_num(jaccard(a, b))


def braycurtis_distance(a, b):
    return np.nan_to_num(braycurtis(a, b))


def canberra_distance(a, b):
    return np.nan_to_num(canberra(a, b))


def cityblock_distance(a, b):
    return np.nan_to_num(cityblock(a, b))


def euclidean_distance(a, b):
    return np.nan_to_num(euclidean(a, b))


def minkowski_distance(a, b, p=3):
    return np.nan_to_num(minkowski(a, b, p))


# One line time: 23.9 ms ± 491 µs
def lzma_ratio(a, b):
    '''Similarity after compressed using lzma'''
    if a == b:
        return 1
    a, b = a.encode('utf-8'), b.encode('utf-8')
    a_len = len(lzma.compress(a))
    b_len = len(lzma.compress(b))
    ab_len = len(lzma.compress(a + b))
    ba_len = len(lzma.compress(b + a))
    ratio = 1 - try_divide(min(ab_len, ba_len) - min(a_len, b_len), max(a_len, b_len))
    return ratio

if __name__ == '__main__':
    test_t1 = 'asfkhioa1239asfkhkashdfkjlhaskdf13r asfnka'
    test_t2 = '123or8y908adsufinzkxnvhihsdfasifh'

def lcs(seq1, seq2):
    seq1 = seq1.split()
    seq2 = seq2.split()
    dp = np.zeros((len(seq1)+1, len(seq2)+1))
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j], dp[i][j + 1])
            if seq1[i] == seq2[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j + 1])
    seq1_mask = [ 0 for wd in seq1]
    seq2_mask = [ 0 for wd in seq2]
    ii, jj = len(seq1), len(seq2)
    while ii != 0 and jj != 0:
        if dp[ii][jj] == dp[ii - 1][jj - 1] + 1 and seq1[ii - 1] == seq2[jj - 1]:
            seq1_mask[ii - 1] = 1
            seq2_mask[jj - 1] = 1
            ii = ii - 1
            jj = jj - 1
            continue
        if dp[ii][jj] == dp[ii - 1][jj]:
            ii = ii - 1
        elif dp[ii][jj] == dp[ii][jj - 1]:
            jj = jj - 1
        elif dp[ii][jj] == dp[ii - 1][jj - 1]:
            ii = ii - 1
            jj = jj - 1
    seq1_left = [ wd for wd, mk in zip(seq1, seq1_mask) if mk == 0]
    seq2_left = [ wd for wd, mk in zip(seq2, seq2_mask) if mk == 0]
    
    return np.max(dp), ' '.join(seq1_left), ' '.join(seq2_left)