#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-03-06 14:02:23
@LastEditTime: 2020-03-06 18:20:38
'''
from math import *


def numericalGradient(x1, x2, w1, w2):
    deno = (2 + sin(x1 * w1) ** 2 + cos(x2, w2)) ** 2
    n_x1 = -1*w1*sin(2*x1*w1)
    n_w1 = -1*x1*sin(2*x1*w1)
    n_x2 = w2*sin(x2*w2)
    n_w2 = x2*sin(x2*w2)
    return n_x1/deno, n_w1/deno, n_x2/deno, n_w2/deno


forward = [
    lambda x1, w1, x2, w2: x1 * w1, x2 * w2,
    lambda a, c: sin(a) ** 2, cos(c),
    lambda b, d: b + d,
    lambda e: e + 2,
    lambda g: 1/g
]
backward = [
    lambda g, up: -1 * (g ** 2) * up,
    lambda e, up: 1 * up,
    lambda b, d, up: up * 1, up * 1,
    lambda a, c, up: up[0]*sin(2*a), up[1]*(-1)*sin(c),
    lambda x1, w1, x2, w2, up: up[0]*w1, up[0]*x1, up[1]*w2, up[1]*x2
],
'''
b4(...,b3(f0(...),b2( )))


'''
def cpGradient(x1, x2, w1, w2):
    def f(g, up): return -1 * (g ** 2) * up
    def g(e, up): return 1 * up
    def e(b, d, up): return up * 1, up * 1
    def b(a, up): return up * sin(2 * a)
    def a(x1, w1, up): return up * w1, up * x1
    def d(c, up): return up * (-1) * sin(c)
    def c(x2, w2, up): return up * w2, up * x2
