#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-21 19:32:51
@LastEditTime: 2020-02-23 19:51:03
'''
from time import perf_counter


def mergeSortTD(a, *args):
    global num              # use num globally for counting comparison
    if len(args) == 0:
        lo = 0
        hi = len(a) - 1
        aux = [0]*len(a)
        mergeSortTD(a, lo, hi, aux)
    else:
        lo, hi, aux = args
        if lo >= hi:
            return 0
        else:
            mid = (lo + hi) // 2
            mergeSortTD(a, lo, mid, aux)
            mergeSortTD(a, mid + 1, hi, aux)
            # merge
            aux[lo:hi+1] = a[lo:hi+1]
            i, j = lo, mid+1
            for k in range(lo, hi+1):
                if i > mid:                         # run out of left
                    a[k: hi + 1] = aux[j: hi + 1]   # take all right
                    break
                elif j > hi:                        # run out of right
                    a[k:hi+1] = aux[i: mid+1]       # take all left
                    break
                elif aux[j] < aux[i]:               # right is smaller
                    a[k], j = aux[j], j+1
                else:                               # left is smaller
                    a[k], i = aux[i], i+1
                num += 1


def mergeSortBU(a):
    global num
    aux = [0] * len(a)
    size = 1
    while size < len(a):
        lo = 0
        while lo < len(a) - size:
            mid = lo + size - 1
            hi = min(lo + size * 2 - 1, len(a) - 1)
            aux[lo:hi+1] = a[lo:hi+1]
            i, j = lo, mid+1
            for k in range(lo, hi+1):
                if i > mid:
                    a[k: hi + 1] = aux[j: hi + 1]
                    break
                elif j > hi:
                    a[k:hi+1] = aux[i: mid+1]
                    break
                elif aux[j] < aux[i]:
                    a[k], j = aux[j], j+1
                else:
                    a[k], i = aux[i], i+1
                num += 1
            lo += size * 2
        size = size * 2


if __name__ == '__main__':
    sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    print('best case')
    for size in sizes:
        with open(r'./data/data0.{}'.format(size)) as f:
            a = []
            for line in f.readlines():
                a.append(int(line))
        print('size : {}'.format(size), end=' ')
        num = 0
        tempa = a.copy()
        tstart = perf_counter()
        mergeSortTD(tempa)
        tend = perf_counter()
        print('mergeSortTD: comparison : {}, takes {:.2f} ms'.format(
            num, 1000*(tend-tstart)), end=' ')
        num = 0
        tstart = perf_counter()
        mergeSortBU(a)
        tend = perf_counter()
        print('mergeSortBU: comparison : {}, takes {:.2f} ms'.format(
            num, 1000*(tend-tstart)))
    print('average case')
    for size in sizes:
        with open(r'./data/data1.{}'.format(size)) as f:
            a = []
            for line in f.readlines():
                a.append(int(line))
        print('size : {}'.format(size), end=' ')
        num = 0
        tempa = a.copy()
        tstart = perf_counter()
        mergeSortTD(tempa)
        tend = perf_counter()
        print('mergeSortTD: comparison : {}, takes {:.2f} ms'.format(
            num, 1000*(tend-tstart)), end=' ')
        num = 0
        tstart = perf_counter()
        mergeSortBU(a)
        tend = perf_counter()
        print('mergeSortBU: comparison : {}, takes {:.2f} ms'.format(
            num, 1000*(tend-tstart)))
