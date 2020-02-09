#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-07 15:46:39
@LastEditTime : 2020-02-08 18:07:22
'''

from time import *
import numpy as np

def fastest3sum(data):
    data = sorted(set(data))
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
                count += 1
                j += 1
                k -= 1
    return count


if __name__ == "__main__":

    a = np.random.randint(-10000,10000,8000)
    begint = process_time()
    print(fastest3sum(a))
    endtime = process_time()
    print('fastest3sum takes {:.3f} s'.format(endtime - begint))
