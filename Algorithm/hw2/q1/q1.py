#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-21 14:39:09
@LastEditTime: 2020-02-21 19:17:35
'''
import numpy as np
from time import perf_counter


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def less(a, b):
    return a < b


def isSorted(a):
    return all([a[i] <= a[i+1] for i in range(len(a)-1)])


_SEQ = [7, 3, 1]


def shellSort(a):
    for h in _SEQ:
        for i in range(h, len(a)):
            j = i
            while j >= h and less(a[j], a[j - h]):
                swap(a, j, j - h)
                j -= h


def insertionSort(a):
    for i in range(1, len(a)):
        j = i
        while j >= 1 and less(a[j], a[j - 1]):
            swap(a, j, j-1)
            j -= 1


if __name__ == '__main__':
    sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    print('worst case')
    for size in sizes:
        with open(r'./Algorithm/hw2/q1/data/data0.{}'.format(size)) as f:
            a = []
            for line in f.readlines():
                a.append(int(line))
        print('size : {}'.format(size), end=' ')
        tstart = perf_counter()
        shellSort(a)
        tend = perf_counter()
        print('shellSort takes : {} s'.format(tend-tstart), end=' ')
        tstart = perf_counter()
        insertionSort(a.copy())
        tend = perf_counter()
        print('insertionSort takes : {} s'.format(tend-tstart))

    print('average case')
    for size in sizes:
        with open(r'./Algorithm/hw2/q1/data/data1.{}'.format(size)) as f:
            a = []
            for line in f.readlines():
                a.append(int(line))
        print('size : {}'.format(size), end=' ')
        tstart = perf_counter()
        shellSort(a.copy())
        tend = perf_counter()
        print('shellSort takes : {} s'.format(tend-tstart), end=' ')
        tstart = perf_counter()
        insertionSort(a)
        tend = perf_counter()
        print('insertionSort takes : {} s'.format(tend-tstart))
