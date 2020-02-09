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
    # diff = max - min
    return [min,max]


if __name__ == '__main__':
    sizes = [128, 512, 1024, 4096,  8192, 16384, 32768, 65536]
    for size in sizes:

        a = np.random.randint(-100000, 100000, size)
        print('{:5d}'.format(size), end=' ')
        tstart =perf_counter()
        print('pair is {}'.format(farthestPair(a)), end=' ')
        tend = perf_counter()
        print('takes {:.2f} ms'.format(1000 * (tend - tstart)))
