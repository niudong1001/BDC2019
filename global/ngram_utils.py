# -*- coding: utf-8 -*-
'''
@Author: niudong
@LastEditors: niudong
@Date: 2019-06-02 22:05:02
@LastEditTime: 2019-06-30 13:35:55
'''
def _unigrams(words):
    """
        Input: a list of words, e.g., ["I", "am", "Denny"]
        Output: a list of unigram
    """
    assert type(words) == list
    return words

# One line time: 5.04 µs ± 272 ns
def _bigrams(words, join_string='_'):
    """
      Input: a list of words, e.g., ["I", "am", "Denny"]
      Output: a list of bigram, e.g., ["I_am", "am_Denny"]
      I use _ as join_string for this example.
    """
    assert type(words) == list
    L = len(words)
    if L > 1:
        lst = [join_string.join([words[i], words[i+1]]) for i in range(L-1)]
    else:
        # set it as unigram
        lst = _unigrams(words)
    return lst


# One line time: 5.89 µs ± 196 ns
def _trigrams(words, join_string='_'):
    """
      Input: a list of words, e.g., ["I", "am", "Denny"]
      Output: a list of trigram, e.g., ["I_am_Denny"]
      I use _ as join_string for this example.
    """
    assert type(words) == list
    L = len(words)
    if L > 2:
        lst = [join_string.join([words[_], words[_+1], words[_+2]]) for _ in range(L-2)]
    else:
        # set it as bigram
        lst = _bigrams(words, join_string)
    return lst

def unichars(text):
    return _unigrams(list(text))

def bichars(text):
    return _bigrams(list(text))

def trichars(text):
    return _trigrams(list(text))

def unigrams(text):
    return _unigrams(text.split())

def bigrams(text):
    return _bigrams(text.split())

def trigrams(text):
    return _trigrams(text.split())


if __name__ == '__main__':

    words = 'My it i you he me.'
    x = unigrams(words)
    y = bigrams(words)
    z = trigrams(words)
    print(x)
    print(y)
    print(z)
    # m = unichars(words)
    # n = bichars(words)
    # q = trichars(words)
    # print(m)
    # print(n)
    # print(q)