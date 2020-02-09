#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-06 21:50:42
@LastEditTime : 2020-02-08 17:59:02
'''
from time import *
import numpy as np


def farthestPair(data):
    min = max = data[0]
    for val in data:
        if val < min:
            min = val
        if val > max:
            max = val
    diff = max - min
    return diff


if __name__ == '__main__':
    a = np.random.randint(-10000, 10000, 50000000)
    tstart = process_time()
    print(farthestPair(a))
    tend = process_time()
    print('farthestPair takes {:.10f} s'.format(tend - tstart))
