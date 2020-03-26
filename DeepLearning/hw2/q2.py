#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-03-06 22:31:19
@LastEditTime: 2020-03-06 23:24:23
'''
import numpy as np


def sigmod(q):
    return 1 / (1 + np.exp(-q))


def numericalGradient(x, w):
    q = w.dot(x)
    sig = sigmod(q)
    return np.dot(w.T, (2*(1-sig)*sig**2)), np.dot((2*(1-sig)*sig**2), x.T)


forward = [
    lambda args: args[1].dot(args[0]),
    lambda arg: sigmod(arg),
    # lambda arg: sum([q**2 for q in arg])
]
backward = [
    lambda arg, up: up * 2*arg,
    lambda arg, up: up*(1-sigmod(arg))*sigmod(arg),
    lambda args, up: (args[1].T.dot(up), up.dot(args[0].T))
]


def cgGradient(x, w):
    mid = []
    args = (x, w)
    mid.append(args)
    for func in forward:
        args = func(args)
        mid.append(args)
    up = 1
    for func in backward:
        args = mid.pop()
        up = func(args, up)
    return up


w = np.array([
    [-1, -2, -3],
    [2, 3, 4],
    [3, 4, 5]
])
x = np.array([-1, 3, 2])[:, None]
nG = numericalGradient(x, w)
cG = cgGradient(x, w)
print((nG[0] == cG[0]).all())
