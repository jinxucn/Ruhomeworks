#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-06 12:39:51
@LastEditTime : 2020-02-10 13:49:14
'''
from time import perf_counter

_N = 8193  # maximum number


class QuickFind:
    def __init__(self):
        self.id = [i for i in range(_N)]    # initialize array

    def find(self, p, q):
        if self.id[p] == self.id[q]:
            return True
        return False

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(1, _N):    # set all those who have the same id changed to new id
            if self.id[i] == pid:
                self.id[i] = qid

    def readPairs(self, pairs):             # if not connected, union them
        for pair in pairs:
            if not self.find(pair[0], pair[1]):
                self.union(pair[0], pair[1])


class QuickUnion:
    def __init__(self):
        self.id = [i for i in range(_N)]

    def _root(self, p):             # if onenode.id equal itself, it is a root
        while p != self.id[p]:
            p = self.id[p]
        return p

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):          # set p.root connected q.root
        self.id[self._root(p)] = self._root(q)

    def readPairs(self, pairs):
        for pair in pairs:
            if not self.find(pair[0], pair[1]):
                self.union(pair[0], pair[1])


class WQuickUnion:
    def __init__(self):
        self.id = [i for i in range(_N)]
        self.sz = [1] * _N

    def _root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        proot = self._root(p)
        qroot = self._root(q)
        if self.sz[proot] > self.sz[qroot]:     # find which branch has more nodes connected
            self.id[qroot] = proot              # and connect the smaller tree to the larger one
            self.sz[proot] += self.sz[qroot]
        else:
            self.id[proot] = qroot
            self.sz[qroot] += self.sz[proot]

    def readPairs(self, pairs):
        for pair in pairs:
            if not self.find(pair[0], pair[1]):
                self.union(pair[0], pair[1])


if __name__ == '__main__':
    '''
    Entry for a single file
    Input: change the file path below
    Output: print out of runtime for quickfind, quickunion, and weighted quickunion
    '''
    # a = []
    # with open(r"./data/8pair.txt", 'r') as f:
    #     for line in f.readlines():
    #         pair = line.split()
    #         a.append([int(pair[0]), int(pair[1])])
    # tstart = perf_counter()
    # qf = QuickFind()
    # qf.readPairs(a)
    # tend = perf_counter()
    # print('qf:{:.3f}'.format(1000*(tend - tstart)), end=' ')
    # tstart = perf_counter()
    # qu = QuickUnion()
    # qu.readPairs(a)
    # tend = perf_counter()
    # print('qu:{:.3f}'.format(1000*(tend - tstart)), end=' ')
    # tstart = perf_counter()
    # wqu = WQuickUnion()
    # wqu.readPairs(a)
    # tend = perf_counter()
    # print('wqu:{:.3f}'.format(1000*(tend - tstart)))

    ##################################################################

    '''
    Runtest for given data,
    '''
    files = [8, 32, 128, 512, 1024, 4096, 8192]
    for size in files:
        a = []
        with open(r"./data/{}pair.txt".format(size), 'r') as f:
            for line in f.readlines():
                pair = line.split()
                a.append([int(pair[0]), int(pair[1])])
        print('{:5d}'.format(size), end=' ')
        tstart = perf_counter()
        qf = QuickFind()
        qf.readPairs(a)
        tend = perf_counter()
        print('qf:{:.3f}'.format(1000*(tend - tstart)), end=' ')
        tstart = perf_counter()
        qu = QuickUnion()
        qu.readPairs(a)
        tend = perf_counter()
        print('qu:{:.3f}'.format(1000*(tend - tstart)), end=' ')
        tstart = perf_counter()
        wqu = WQuickUnion()
        wqu.readPairs(a)
        tend = perf_counter()
        print('wqu:{:.3f}'.format(1000*(tend - tstart)))
