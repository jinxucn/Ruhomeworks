#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-03-20 22:00:13
@LastEditTime: 2020-03-21 17:12:27
'''
import random
import sys
sys.setrecursionlimit(10000)

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

    def aveLen(self, *node):
        if not node:
            length = self.aveLen(self.root)
            return length/self.size()
        else:
            x = node[0]
            if x is None:
                return 0
            length = self.size(x)+self.aveLen(x.left)+self.aveLen(x.right)
            return length


if __name__ == "__main__":
    with open("./q2.csv", "a") as f:

        for N in [2**i for i in range(15)]:
            randomlen = 0
            for i in range(10):

                t = BST()
                for k in random.sample(range(N), N):
                    t.put(k, None)
                randomlen += t.aveLen()
            randomlen /= 10
            t = BST()
            for k in range(N):
                t.put(k, None)
            orderlen = t.aveLen()
            f.write(str(N)+","+str(randomlen)+","+str(orderlen)+"\n")
