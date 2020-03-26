#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-03-21 13:00:01
@LastEditTime: 2020-03-21 17:58:18
'''

class BST:
    class Node:
        left = right = None

        def __init__(self, key, val, N):
            self.key = key
            self.val = val
            self.N = N

    def __init__(self):
        self.root = None

    def size(self, *node):
        if not node:
            return self.size(self.root)
        else:
            x = node[0]
            if x is None:
                return 0
            else:
                return x.N

    def put(self, key, val, *node):
        if not node:
            self.root = self.put(key, val, self.root)
        else:
            x = node[0]
            if x is None:
                return self.Node(key, val, 1)
            if key < x.key:
                x.left = self.put(key, val, x.left)
            elif key > x.key:
                x.right = self.put(key, val, x.right)
            else:
                x.val = val
            x.N = 1+self.size(x.left)+self.size(x.right)
            return x

    def select(self, rank, *node):
        if not node:
            return self.select(rank, self.root)
        else:
            x = node[0]
            leftSize = self.size(x.left)
            if leftSize > rank:
                return self.select(rank, x.left)
            elif leftSize < rank:
                return self.select(rank-1-leftSize, x.right)
            else:
                return x.key

    def rank(self, key, *node):
        if not node:
            return self.rank(key, self.root)
        else:
            x = node[0]
            if key < x.key:
                return self.rank(key, x.left)
            elif key > x.key:
                return 1+self.size(x.left)+self.rank(key, x.right)
            else:
                return self.size(x.left)


if __name__ == "__main__":
    t = BST()
    with open("./select-data.txt", "r") as f:
        for line in f.readlines():
            t.put(int(line), None)
    print(t.select(7))
    print(t.rank(7))
