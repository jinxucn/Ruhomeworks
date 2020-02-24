#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-21 19:20:27
@LastEditTime: 2020-02-23 20:13:32
'''

from time import perf_counter


def mergeSortCount(a, *args):
    global num
    if len(args) == 0:
        lo = 0
        hi = len(a) - 1
        aux = [0]*len(a)
        mergeSortCount(a, lo, hi, aux)
    else:
        lo, hi, aux = args
        if lo >= hi:
            return
        else:
            mid = (lo + hi) // 2
            mergeSortCount(a, lo, mid, aux)
            mergeSortCount(a, mid + 1, hi, aux)
            aux[lo:hi+1] = a[lo:hi+1]
            i, j = lo, mid+1
            for k in range(lo, hi+1):
                if i > mid:
                    a[k: hi + 1] = aux[j: hi + 1]
                    break
                elif j > hi:
                    a[k:hi+1] = aux[i: mid+1]
                    break
                elif aux[j] < aux[i]:           # if right is bigger
                    a[k], j = aux[j], j + 1
                    num += mid-i+1              # count elements from i to mid
                else:
                    a[k], i = aux[i], i+1


def ktDistance(a, b):
    transfer = {}
    # mapping index,element -> element,index
    for index, element in enumerate(a):
        transfer[element] = index
    bIndex = [0]*len(b)
    for i in range(len(b)):
        bIndex[i] = transfer[b[i]]
    return mergeSortCount(bIndex)


if __name__ == '__main__':
    sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    for size in sizes:
        num = 0
        a, b = [], []
        with open(r'./data/data0.{}'.format(size)) as f:
            for line in f.readlines():
                a.append(int(line))
        with open(r'./data/data1.{}'.format(size)) as f:
            for line in f.readlines():
                b.append(int(line))
        tstart = perf_counter()
        ktDistance(a, b)
        tend = perf_counter()
        print('size: {}, inversions: {}, takes {:.3f} ms'.format(
            size, num, 1000*(tend-tstart)))
