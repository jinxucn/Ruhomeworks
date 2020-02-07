#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-02 20:50:23
@LastEditTime : 2020-02-06 19:30:20
'''
from time import *

'''
@description: A naive implementation for 3 sum problem
@param : {list}
@return: count for 3 sum
'''


def naive3sum(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 0:
                    count += 1
    return count


'''
@description: A smart implementation for 3 sum problem
@param : {list}
@return: count for 3 sum
'''


def smart3sum(data):
    data.sort()
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if _binarySearch(data, -(data[i] + data[j])):  # binarysearch -(a+b) in data
                count += 1
    return count


'''
@description: recursively binary search element in data
@param : {list} {int} [option]{int} {int}
@return: boolean
'''


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
    Normal entry for a single file
    Input: change the file path below
    Output: print out of time cost for naive3sum and smart3sum
    '''
    a = []
    with open(r"./data/1024int.txt", 'r') as f:
        for line in f.readlines():
            a.append(int(line))
    begint = time()
    smart3sum(a)
    endtime = time()
    print('smart3sum takes {:.3f} s'.format(endtime - begint))
    begint = time()
    naive3sum(a)
    endtime = time()
    print('naiva3sum takes {:.3f} s'.format(endtime - begint))

    '''
    A run test for given data,
    4096 and above would take too long to run
    '''
    # files = [8, 32, 128, 512, 1024]
    # for size in files:
    #     a = []
    #     with open(r"./data/{}int.txt".format(size), 'r') as f:
    #         for line in f.readlines():
    #             a.append(int(line))
    #     print(size, end=' ')
    #     begint = time()
    #     naive3sum(a)
    #     endtime = time()
    #     print('{:.2f}'.format(1000*(endtime-begint)), end=' ')
    #     begint = time()
    #     smart3sum(a)
    #     endtime = time()
    #     print('{:.2f}'.format(1000*(endtime-begint)))
