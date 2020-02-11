#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-02 20:50:23
@LastEditTime : 2020-02-10 21:40:39
'''
from time import perf_counter


def naive3sum(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 0:
                    count += 1
    return count


def smart3sum(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            # binarysearch -(a+b) in data
            if _binarySearch(data, -(data[i] + data[j])):
                count += 1
    return count


# local function, binary search val in data
# usage: _binarySearch(data,val) or _binarySearch(data,val,low,high)
def _binarySearch(data, val, *args):
    if len(args) == 0:
        lo = 0
        hi = len(data) - 1
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
                return _binarySearch(data, val, lo, mid - 1)
            elif val > data[mid]:
                return _binarySearch(data, val, mid + 1, hi)


if __name__ == "__main__":

    '''
    Entry for a single file
    Input: change the file path below
    Output: print out of runtime for naive3sum and smart3sum
    '''
    # a = []
    # with open(r"./data/8int.txt", 'r') as f:
    #     for line in f.readlines():
    #         a.append(int(line))
    # tstart = perf_counter()
    # smart3sum(a)
    # endtime = perf_counter()
    # print('smart3sum takes {} s'.format(endtime - tstart))
    # tstart = perf_counter()
    # naive3sum(a)
    # endtime = perf_counter()
    # print('naive3sum takes {} s'.format(endtime - tstart))

    ##################################################################

    '''
    Runtest for given data,
    4096 and above would take too long to run
    '''
    files = [8, 32, 128, 512, 1024]
    for size in files:
        a = []
        with open(r"./data/{}int.txt".format(size), 'r') as f:
            for line in f.readlines():
                a.append(int(line))
        print(size, end=' ')
        tstart = perf_counter()
        naive3sum(a)
        endtime = perf_counter()
        print('{:.2f}'.format(1000 * (endtime - tstart)), end=' ')
        a.sort()
        tstart = perf_counter()
        smart3sum(a)
        endtime = perf_counter()
        print('{:.2f}'.format(1000*(endtime-tstart)))
