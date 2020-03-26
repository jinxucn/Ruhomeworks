#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-03-21 12:22:31
@LastEditTime: 2020-03-21 17:57:23
'''
import random
import numpy as np


class RedBlackTree:
    RED = True
    BLACK = False

    class Node:
        left = right = None

        def __init__(self, key, val, color, N):
            self.key = key
            self.val = val
            self.color = color
            self.N = N

    def __init__(self):
        self.root = None

    def isRed(self, node):
        if node is None:
            return False
        return node.color == self.RED

    def size(self, *node):
        if not node:
            return self.size(self.root)
        else:
            x = node[0]
            if x is None:
                return 0
            else:
                return x.N

    def isEmpty(self):
        return self.size() == 0

    def __str__(self, *node):
        if not node:
            return self.__str__(self.root)
        else:
            x = node[0]
            if x is None:
                return ""
            else:
                return self.__str__(x.left)+"({}:{}), ".format(x.key, x.val)+self.__str__(x.right)

    def get(self, key, *node):
        if not node:
            return self.get(key, self.root)
        else:
            x = node[0]
            if x is None:
                return None
            if key < x.key:
                return self.get(key, x.left)
            elif key > x.key:
                return self.get(key, x.right)
            else:
                return x.val

    def contains(self, key):
        return self.get(key) is not None

    def getMin(self, node):
        if node.left is None:
            return node
        else:
            return self.getMin(node.left)

    def rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        x.N = node.N
        node.N = 1+self.size(node.left)+self.size(node.right)
        return x

    def rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        x.N = node.N
        node.N = 1+self.size(node.left)+self.size(node.right)
        return x

    def flipColors(self, node):
        node.color = self.RED
        node.left.color = node.right.color = self.BLACK

    def put(self, key, val, *node):
        if not node:
            self.root = self.put(key, val, self.root)
            self.root.color = self.BLACK
        else:
            x = node[0]
            if x is None:
                return self.Node(key, val, self.RED, 1)
            if key < x.key:
                x.left = self.put(key, val, x.left)
            elif key > x.key:
                x.right = self.put(key, val, x.right)
            else:
                x.val = val

            if self.isRed(x.right) and not self.isRed(x.left):
                x = self.rotateLeft(x)
            if self.isRed(x.left) and self.isRed(x.left.left):
                x = self.rotateRight(x)
            if self.isRed(x.left) and self.isRed(x.right):
                self.flipColors(x)
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
    with open("./q4.csv", "a+") as f:

        for N in range(1, 10000):
            aveLen = []
            for i in range(5):
                t = RedBlackTree()
                for k in random.sample(range(N), N):
                    t.put(k, None)
                aveLen.append(t.aveLen())
            f.write(str(N)+','+str(np.mean(aveLen)) +
                    ',' + str(np.std(aveLen, ddof=1))+'\n')
            print(str(N)+','+str(np.mean(aveLen)) +
                  ','+str(np.std(aveLen, ddof=1)))
