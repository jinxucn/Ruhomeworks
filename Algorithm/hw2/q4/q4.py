#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-22 20:31:47
@LastEditTime: 2020-02-23 20:11:40
'''
from time import perf_counter

data = [1] * 1024 + [11] * 2048 + [111] * 4096 + [1111] * 1024


def insertionSort(a):
    for i in range(1, len(a)):
        j = i
        while j >= 1 and a[j] < a[j - 1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


if __name__ == '__main__':

    tstart = perf_counter()
    for i in range(100):
        insertionSort(data)
    tend = perf_counter()
    print(tend-tstart)
