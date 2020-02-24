#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-22 20:33:50
@LastEditTime: 2020-02-23 23:09:40
'''
from time import perf_counter
from random import sample


def quickSort(a, *args):
    if len(args) == 0:
        lo, hi = 0, len(a)-1
        quickSort(a, lo, hi)
    else:
        lo, hi = args
        if lo >= hi:
            return
        else:
            mid = (lo + hi) // 2
            # find median, move to a[lo]
            if (a[mid] > a[lo]) != (a[mid] > a[hi]):    # a[mid] is median?
                a[lo], a[mid] = a[mid], a[lo]
            elif (a[hi] > a[mid]) != (a[hi] > a[lo]):   # a[hi] is median?
                a[lo], a[hi] = a[hi], a[lo]
            # partitioning
            i, j = lo, hi
            pivot = a[lo]                               # save a[lo] -> pivot
            while i < j:
                while i < j and a[j] > pivot:           # find small at right
                    j -= 1
                while i < j and a[i] < pivot:           # find big at left
                    i += 1
                a[i], a[j] = a[j], a[i]                 # swap
            a[i] = pivot                                # meet point is pivot
            quickSort(a, lo, i - 1)
            quickSort(a, i+1, hi)


def insertionSort(a, lo, hi):  # insertion sort a[lo:hi+1]
    for i in range(lo+1, hi+1):
        j = i
        while j >= lo+1 and a[j] < a[j - 1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def quickSortCF(a, *args):
    if len(args) < 2:
        lo, hi = 0, len(a)-1
        quickSortCF(a, lo, hi, args[0])
    else:
        lo, hi, cut = args
        if hi-lo+1 <= cut:        # cut off, do insertion sort
            insertionSort(a, lo, hi)
            return
        else:
            mid = (lo + hi) // 2
            if (a[mid] > a[lo]) != (a[mid] > a[hi]):
                a[lo], a[mid] = a[mid], a[lo]
            elif (a[hi] > a[mid]) != (a[hi] > a[lo]):
                a[lo], a[hi] = a[hi], a[lo]
            i, j = lo, hi
            pivot = a[lo]
            while i < j:
                while i < j and a[j] > pivot:
                    j -= 1
                while i < j and a[i] < pivot:
                    i += 1
                a[i], a[j] = a[j], a[i]
            a[i] = pivot
            quickSortCF(a, lo, i - 1, cut)
            quickSortCF(a, i+1, hi, cut)


if __name__ == '__main__':
    sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    print('best case')
    for size in sizes:
        a = []
        with open(r'./data/data0.{}'.format(size)) as f:
            for line in f.readlines():
                a.append(int(line))
        print('size: {}'.format(size), end=' ')
        tempa = a.copy()
        tstart = perf_counter()
        quickSort(tempa)
        tend = perf_counter()
        print('quickSort takes {:.2f} ms'.format(1000*(tend-tstart)), end=' ')
        tstart = perf_counter()
        quickSortCF(a, 7)
        tend = perf_counter()
        print('quickSortCF takes {:.2f} ms'.format(1000*(tend-tstart)))

    print('average case')
    for size in sizes:
        a = []
        with open(r'./data/data1.{}'.format(size)) as f:
            for line in f.readlines():
                a.append(int(line))
        print('size: {}'.format(size), end=' ')
        tempa = a.copy()
        tstart = perf_counter()
        quickSort(tempa)
        tend = perf_counter()
        print('quickSort takes {:.2f} ms'.format(1000*(tend-tstart)), end=' ')
        tstart = perf_counter()
        quickSortCF(a, 7)
        tend = perf_counter()
        print('quickSortCF takes {:.2f} ms'.format(1000*(tend-tstart)))

    print('cut-off')
    a = []
    with open(r'./data/data1.32768') as f:
        for line in f.readlines():
            a.append(int(line))
    for cut in range(3, 40):
        tempa = a.copy()
        tstart = perf_counter()
        quickSortCF(tempa, cut)
        tend = perf_counter()
        print('cut: {}, takes: {:.2f} ms'.format(cut, 1000 * (tend - tstart)))
