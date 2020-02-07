#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-07 15:46:39
@LastEditTime : 2020-02-07 17:37:10
@description: I get the idea from a java implementation on https://www.programcreek.com/2012/12/leetcode-3sum/
'''

from time import *


def fastest3sum(data):
    data = sorted(set(data))
    count = 0
    k = len(data) - 1
    for i in range(len(data)):
        j = i + 1
        while j < k:
            if data[i] + data[j] + data[k] > 0:
                k -= 1
            elif data[i] + data[j] + data[k] < 0:
                j += 1
            else:
                print(data[i],end=' ')
                print(data[j],end=' ')
                print(data[k])
                count += 1
                j += 1
                k -= 1
    return count


if __name__ == "__main__":

    a = []
    with open(r"../q1/data/8192int.txt", 'r') as f:
        for line in f.readlines():
            a.append(int(line))
    begint = time()
    print(fastest3sum(a))
    endtime = time()
    print('fastest3sum takes {:.10f} s'.format(endtime - begint))
