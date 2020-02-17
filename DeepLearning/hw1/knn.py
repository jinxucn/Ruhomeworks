#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-12 21:33:11
@LastEditTime: 2020-02-17 12:21:18
'''
import math
import numpy as np
from download_mnist import load
import operator
import time
# classify using kNN
#x_train = np.load('../x_train.npy')
#y_train = np.load('../y_train.npy')
#x_test = np.load('../x_test.npy')
#y_test = np.load('../y_test.npy')
x_train, y_train, x_test, y_test = load()
x_train = x_train.reshape(60000, 28*28)
x_test = x_test.reshape(10000, 28*28)
x_train = x_train.astype(float)
x_test = x_test.astype(float)


def kNNClassify(newInput, dataSet, labels, k):
    result = []
    newInput_squared = np.sum(newInput ** 2, axis=1)
    dataSet_squared = np.sum(dataSet ** 2, axis=1)
    distances = np.sqrt(newInput_squared[:, None]+dataSet_squared -
                        2*np.dot(newInput, dataSet.T))
    nearestKindices = np.argsort(distances)[:, :k]
    nearestKlabels = labels[nearestKindices]
    for i in range(nearestKlabels.shape[0]):
        result.append(np.argmax(np.bincount(nearestKlabels[i, :])))
    return result


start_time = time.time()
outputlabels = kNNClassify(x_test[0:10000], x_train, y_train, 10)
result = y_test[0:10000] - outputlabels
result = (1 - np.count_nonzero(result)/len(outputlabels))
print("---classification accuracy for knn on mnist: %s ---" % result)
print("---execution time: %s seconds ---" % (time.time() - start_time))
