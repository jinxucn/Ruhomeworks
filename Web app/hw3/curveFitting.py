#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-03-23 14:14:29
@LastEditTime: 2020-03-26 17:51:54
'''
import numpy as np
# import matplotlib.pyplot as plt
import random


def curfit(y, alpha=0.005, beta=2, M=9):
    xt = np.array(range(1, len(y) + 2))[:, None]
    xt = xt.astype(np.float64)

    def phi(x):
        return np.asarray([x**i for i in range(M+1)]).T.reshape(len(x), M+1)

    def S(x):
        temp = alpha * np.identity(M + 1) + beta*phi(x).T.dot(phi(x))
        return np.linalg.inv(temp)

    def mean(x, t):
        return beta*np.matmul(phi(x), np.matmul(S(x[0:-1]), np.matmul(phi(x[0:-1]).T, t)))

    def variance(x):
        temp = []
        for xi in phi(x[0:-1]):
            temp.append(np.sqrt(1/beta+xi.dot(S(x[0:-1]).dot(xi.T))))
        return temp

    return mean(xt, y), variance(xt)


if __name__ == "__main__":
    names = ['NVDA', 'AMD', 'BABA', 'KO', 'DIS',
             'AMZN', 'BILI', 'NTES', 'GOOG', 'INTC']
    with open('./result.csv', "a+") as f:
        f.write('name,absError,relativeError\n')
    for name in names:
        with open("./datasets/{}.csv".format(name), "r") as f:
            raw = []
            f.readline()
            for line in f.readlines():
                raw.append(float(line.split(',')[2]))
        # train = np.asarray(raw)
        # M_min = 0
        # rss_min = float('inf')
        # for M in range(4, 14):
        #     m, v = curfit(train, M=M)
        #     rss = sum(np.power(m[0:-1]-train, 2))
        #     if rss < rss_min:
        #         rss_min = rss
        #         M_min = M
        #         mean = m
        #         variance = v

        # N_index = random.sample(range(50, 200), 10)
        # abs_mean_error = sum(abs(mean[N_index] - train[N_index])) / 10
        # relative_error = sum(
        #     abs(mean[N_index] - train[N_index])/mean[N_index])/10
        # print(abs_mean_error, relative_error)
        # print(name, M_min)
        # x = [i for i in range(len(train))]
        # plt.figure("CURVE FITTINT "+name+" M="+str(M_min))
        # plt.scatter(x, train, s=50, edgecolors='y', facecolor="none")
        # plt.plot(x, mean[0:-1])
        # plt.fill_between(x, mean[0:-1] - variance,
        #                  mean[0:-1] + variance, color="pink", alpha=0.5)

        abs_mean_error = []
        relative_error = []
        for i in range(15):
            N = random.randint(200, 250)

            train = np.asarray(raw[0:N])
            rss_min = float('inf')
            for M in range(4, 14):
                m, v = curfit(train[0:N - 1], M=M)
                rss = sum(np.power(m[0:-1]-train[0:N-1], 2))
                if rss < rss_min:
                    rss_min = rss
                    # M_min = M
                    mean = m
                    variance = v

            abs_mean_error.append(abs(train[-1]-mean[-1]))
            relative_error.append(abs(train[-1]-mean[-1])/train[-1])
        abs_mean_error = sum(abs_mean_error)/len(abs_mean_error)
        relative_error = sum(relative_error) / len(relative_error)
        print(abs_mean_error, relative_error)

        with open('./result.csv', "a+") as f:
            f.write(str(name)+','+str(abs_mean_error) +
                    ','+str(relative_error) + '\n')
