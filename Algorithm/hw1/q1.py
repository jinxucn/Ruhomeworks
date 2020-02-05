# -*- coding: utf-8 -*-
# @Author: Jin X
# @Date:   2020-02-04 16:31:04
# @Last Modified by:   Jin X
# @Last Modified time: 2020-02-04 16:57:24
import os
from time import *


def naive3sum(data):
    count = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j+1, len(data)):
                if data[i] + data[j] + data[k] == 0:
                    count += 1
    return count


def smart3sum(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if _binarySearch(data, -(data[i] + data[j])):
                count += 1
    return count


def _binarySearch(data, val, *args):
    if len(args) == 0:
        lo = 0
        hi = len(data)
        return _binarySearch(data, val, lo, hi)
    else:
        lo = args[0]
        hi = args[1]
        if lo > hi:
            return False
        else:
            mid = (lo + hi) // 2
            if data[mid] == val:
                return True
            elif val < data[mid]:
                return _binarySearch(data, val, lo, mid-1)
            elif val > data[mid]:
                return _binarySearch(data, val, mid+1, hi)


if __name__ == "__main__":
    # a = _binarySearch([-67, -52, -43, -42, -37, -15, -6, -2,
    #                    3, 6, 12, 42, 65, 124, 342, 502], 502)
    # print(a)
    # files = os.listdir("./Algorithm./hw1/hw1-1.data")
    # for f in files:
    #     print(f)
    a = []
    with open(r"C:\Users\test1\Documents\Homework\Algorithm\hw1\hw1-1.data\8192int.txt", 'r') as f:
        for line in f.readlines():
            a.append(int(line))
    print(a)
    begint = time()
    print(smart3sum(a))
    endt = time()
    print(endt-begint)
