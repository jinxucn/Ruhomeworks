#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-21 14:39:09
@LastEditTime: 2020-02-23 17:05:23
'''
from time import perf_counter


def shellSort(a, SEQ=[7, 3, 1]):
    count = 0
    for h in SEQ:
        for i in range(h, len(a)):
            j = i
            while j >= h:
                count += 1
                if a[j] < a[j - h]:
                    a[j], a[j-h] = a[j-h], a[j]
                    j -= h
                else:
                    break
    return count


# def sedgewickStep(i=5):
#     while i >= 0:
#         yield 4 ** (i + 2) - 3 * 2 ** (i + 2) + 1
#         yield 9 * (4 ** i) - 9 * (2 ** i) + 1
#         i -= 1


def insertionSort(a):
    count = 0
    for i in range(1, len(a)):
        j = i
        while j >= 1:
            count += 1
            if a[j] < a[j - 1]:
                a[j], a[j-1] = a[j-1], a[j]
                j -= 1
            else:
                break
    return count


if __name__ == '__main__':
    sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    print('best case')
    for size in sizes:
        with open(r'./data/data0.{}'.format(size)) as f:
            a = []
            for line in f.readlines():
                a.append(int(line))
        print('size : {}'.format(size), end=' ')
        tstart = perf_counter()
        comparison = shellSort(a)
        tend = perf_counter()
        print('shellSort: comparison: {}, takes: {:.3f} ms'.format(
            comparison, 1000*(tend-tstart)), end=' ')
        tstart = perf_counter()
        comparison = insertionSort(a)
        tend = perf_counter()
        print('insertionSort: comparison: {}, takes: {:.3f} ms'.format(
            comparison, 1000*(tend-tstart)))

    print('average case')
    for size in sizes:
        with open(r'./data/data1.{}'.format(size)) as f:
            a = []
            for line in f.readlines():
                a.append(int(line))
        tempa = a.copy()
        print('size : {}'.format(size), end=' ')
        tstart = perf_counter()
        comparison = shellSort(tempa)
        tend = perf_counter()
        print('shellSort: comparison: {}, takes: {:.3f} ms'.format(
            comparison, 1000*(tend-tstart)), end=' ')
        tstart = perf_counter()
        comparison = insertionSort(a)
        tend = perf_counter()
        print('insertionSort: comparison: {}, takes: {:.3f} ms'.format(
            comparison, 1000*(tend-tstart)))
