#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-03-20 17:40:43
@LastEditTime: 2020-03-21 16:43:41
'''


class TwoThreeTree:
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

    def put(self, key, val, *node):
        if not node:
            self.root = self.put(key, val, self.root)
            self.root.color = self.BLACK
        else:
            x = node[0]
            if x is None:
                # at buttom default 3-nodes
                return self.Node(key, val, self.RED, 1)
            if key < x.key:
                x.left = self.put(key, val, x.left)
                if self.isRed(x) or self.isRed(x.right):    # 4-nodes to 3-nodes
                    x.left.color = self.BLACK
            elif key > x.key:
                x.right = self.put(key, val, x.right)
                if self.isRed(x) or self.isRed(x.left):     # 4-nodes to 3-nodes
                    x.right.color = self.BLACK
            else:
                x.val = val
            x.N = 1+self.size(x.left)+self.size(x.right)
            return x

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

    def deleteMin(self, node):
        if node.left is None:
            return node.right
        node.left = self.deleteMin(node.left)
        node.N = 1+self.size(node.left)+self.size(node.right)
        return node

    def getMin(self, node):
        if node.left is None:
            return node
        else:
            return self.getMin(node.left)

    def delete(self, key, *node):
        if not node:
            self.root = self.delete(key, self.root)
        else:
            x = node[0]
            if key < x.key:
                x.left = self.delete(key, x.left)
            elif key > x.key:
                x.right = self.delete(key, x.right)
            else:
                if x.right is None:
                    return x.left
                if x.left is None:
                    return x.right
                t = x
                x = self.getMin(t.right)
                x.right = self.deleteMin(t.right)
                x.left = t.left
            x.N = 1+self.size(x.left)+self.size(x.right)
            return x


if __name__ == "__main__":
    t = TwoThreeTree()
    t.put(6, 'a')
    t.put(2, 'c')
    t.put(5, 'g')
    t.put(7, 'h')
    t.delete(6)
    print(t.contains(6))
    print(t.get(10))
    print(t.size())
    print(t)
