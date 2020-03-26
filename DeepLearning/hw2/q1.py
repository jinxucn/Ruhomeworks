#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-03-06 14:02:23
@LastEditTime: 2020-03-06 23:06:20
'''
from math import *


def numericalGradient(x1, w1, x2, w2):
    deno = (2 + sin(x1 * w1) ** 2 + cos(x2*w2)) ** 2
    n_x1 = -1*w1*sin(2*x1*w1)
    n_w1 = -1*x1*sin(2*x1*w1)
    n_x2 = w2*sin(x2*w2)
    n_w2 = x2*sin(x2*w2)
    return n_x1/deno, n_w1/deno, n_x2/deno, n_w2/deno


forward = [
    lambda args: (args[0] * args[1], args[2] * args[3]),
    lambda args: (sin(args[0]) ** 2, cos(args[1])),
    lambda args: sum(args),
    lambda arg: arg + 2,
    # lambda arg: 1/arg
]
backward = [
    lambda arg, up:  up * -1 / (arg ** 2),
    lambda args, up: up,
    lambda args, up: (up * 1, up * 1),
    lambda args, up: (up[0]*sin(2*args[0]), up[1] * -sin(args[1])),
    lambda args, up: (up[0]*args[1], up[0] * args[0],
                      up[1]*args[3], up[1]*args[2])
]


def cgGradient(x1, w1, x2, w2):
    mid = []
    args = (x1, w1, x2, w2)
    mid.append(args)
    for func in forward:
        args = func(args)
        mid.append(args)
    up = 1
    for func in backward:
        args = mid.pop()
        up = func(args, up)
    return up


print(numericalGradient(1, 2, -5, 4))
print(cgGradient(1, 2, -5, 4))
