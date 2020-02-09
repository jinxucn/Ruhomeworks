#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-06 12:39:51
@LastEditTime : 2020-02-08 17:41:05
'''
from time import *

_N = 8193


class QuickFind:
    def __init__(self):
        self.id = [i for i in range(_N)]

    def find(self, p, q):
        if self.id[p] == self.id[q]:
            return True
        return False

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(1, _N):
            if self.id[i] == pid:
                self.id[i] = qid

    def readPairs(self, pairs):
        for pair in pairs:
            if not self.find(pair[0],pair[1]):
                self.union(pair[0],pair[1])


class QuickUnion:
    def __init__(self):
        self.id = [i for i in range(8193)]

    def _root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        self.id[self._root(p)] = self._root(q)

    def readPairs(self, pairs):
        for pair in pairs:
            if not self.find(pair[0],pair[1]):
                self.union(pair[0],pair[1])


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
        if self.sz[proot] > self.sz[qroot]:
            self.id[qroot] = proot
            self.sz[proot] += self.sz[qroot]
        else:
            self.id[proot] = qroot
            self.sz[qroot] += self.sz[proot]

    def readPairs(self, pairs):
        for pair in pairs:
            if not self.find(pair[0],pair[1]):
                self.union(pair[0],pair[1])


if __name__ == '__main__':
    files = [8, 32, 128, 512, 1024, 4096, 8192]
    a = []
    for size in files:
        a = []
        with open(r"./data/{}pair.txt".format(size), 'r') as f:
            for line in f.readlines():
                pair = line.split()
                a.append([int(pair[0]), int(pair[1])])
        print('{:5d}'.format(size), end=' ')
        tstart = process_time()
        qf = QuickFind()
        qf.readPairs(a)
        tend = process_time()
        print('qf:{:.10f}'.format(tend - tstart), end=' ')
        tstart = process_time()
        qu = QuickUnion()
        qu.readPairs(a)
        tend = process_time()
        print('qu:{:.10f}'.format(tend - tstart), end=' ')
        tstart = process_time()
        wqu = WQuickUnion()
        wqu.readPairs(a)
        tend = process_time()
        print('wqu:{:.10f}'.format(tend - tstart))
