#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-07 15:46:39
@LastEditTime : 2020-02-08 18:07:22
'''

from time import *
import numpy as np
import random


def fastest3sum(data):
    count = 0
    for i in range(len(data)):
        j = i + 1
        k = len(data) - 1
        while j < k:
            if data[i] + data[j] + data[k] > 0:
                k -= 1
            elif data[i] + data[j] + data[k] < 0:
                j += 1
            else:
                jsame = 1
                ksame = 1
                while j + jsame < k and data[j] == data[j + jsame]:
                    jsame += 1
                while k - ksame > j and data[k] == data[k - ksame]:
                    ksame += 1
                count += jsame * ksame
                j += jsame
                k -= ksame
    return count


if __name__ == "__main__":
    sizes = [128, 512, 1024, 4096, 8192, 16384]
    for size in sizes:

        # a = random.sample(range(-10000, 10000), size)
        a = np.random.randint(-10000, 10000, size)
        a.sort()
        print('{:5d}'.format(size), end=' ')
        tstart = process_time()
        print('{} matches'.format(fastest3sum(a)), end=' ')
        endtime = process_time()
        print('takes {:.3f} ms'.format(1000*(endtime - tstart)))
