#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-06 21:50:42
@LastEditTime : 2020-02-06 22:07:12
'''
from time import *


def farthestPair(pairs):
    fpair = [0, 0]
    for pair in pairs:
        if abs(pair[0]-pair[1]) > abs(fpair[0] - fpair[1]):
            fpair = pair
    return fpair


if __name__ == '__main__':
    files = [8, 32, 128, 512, 1024, 4096, 8192]
    a = []
    for size in files:
        a = []
        with open(r"./data/{}pair.txt".format(size), 'r') as f:
            for line in f.readlines():
                pair = line.split()
                a.append([int(pair[0]),int(pair[1])])
        print('{:5d}'.format(size), end=' ')
        tstart = time()
        fpair = farthestPair(a)
        tend = time()
        print('farthest pair is ({},{})'.format(fpair[0], fpair[1]), end=' ')
        print('taking {:.10f} s'.format(tend - tstart))
