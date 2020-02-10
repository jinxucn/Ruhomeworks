#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-10 11:48:46
@LastEditTime : 2020-02-10 12:59:47
'''
import numpy as np
from scipy.optimize import curve_fit


q1size = np.array([8, 32, 128, 512, 1024, 4096, 4196, 8192])
q1niave = np.array([0, 0, 31.25, 2109.38, 17062.5,
                    1124015.63, 1215734.38, 9034207.23])
q1smart = np.array([0, 0, 15.62, 406.25, 1812.5,
                    35343.75, 39203.13, 155703.13])


q2size = np.array([8, 32, 128, 512, 1024, 4096, 8192])
q2qf = np.array([3.13, 12.22, 48.12, 188.55, 386.26, 1503.79, 2659.27])
q2qu = np.array([0.23, 0.2, 0.31, 0.52, 0.89, 3.47, 14.1])
q2wqu = np.array([0.24, 0.22, 0.3, 0.61, 1.02, 3.81, 7.97])


def N3(x, a, b):
    return a+b*np.power(x, 3)


def N2logN(x, a, b):
    return a+b*np.power(x, 2)*np.log(x)


def N2(x, a, b):
    return a + b * np.power(x, 2)


def NlogN(x, a, b):
    return a+b*x*np.log(x)


if __name__ == '__main__':
    popt, pcov = curve_fit(N3, q1size, q1niave)
    print('Naive 3 sum :' + str(popt))
    popt, pcov = curve_fit(N2logN, q1size, q1smart)
    print('Smart 3 sum :' + str(popt))
    popt, pcov = curve_fit(N2, q2size, q2qf)
    print('Quick Find :' + str(popt))
    popt, pcov = curve_fit(N2, q2size, q2qu)
    print('Quick Union :' + str(popt))
    popt, pcov = curve_fit(NlogN, q2size, q2wqu)
    print('Weighted Quick Union :' + str(popt))
