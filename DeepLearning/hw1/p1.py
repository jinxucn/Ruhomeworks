#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-12 21:37:54
@LastEditTime : 2020-02-13 18:22:36
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

train_data = np.array([
    [0, 1, 0], [0, 1, 1], [1, 2, 1], [1, 2, 0],
    [1, 2, 2], [2, 2, 2], [1, 2, -1], [2, 2, 3],
    [-1, -1, -1], [0, -1, -2], [0, -1, 1], [-1, -2, 1]])

train_label = np.array([0]*4+[1]*4+[2]*4)

test_data = np.array([1, 0, 1])


def kNNClassify(newInput, dataSet, labels, k):
    # newInput_squared = np.sum(newInput ** 2,axis=1)
    # dataSet_squared = np.sum(dataSet ** 2, axis=1)
    # distances = np.sqrt(newInput_squared+dataSet_squared -
    #                     2*np.dot(newInput, dataSet.T))
    distances = np.sum((train_data-test_data)**2, axis=1)
    nearestKindices = np.argsort(distances)[:k]
    nearestKlabels = labels[nearestKindices]
    return np.argmax(np.bincount(nearestKlabels)), dataSet[nearestKindices]


if __name__ == '__main__':
    k = 2
    label, neighbors = kNNClassify(test_data, train_data, train_label, k)
    print('k: {}, class: {}'.format(k, label))
    print('nearest {} points are \n{}'.format(k, neighbors))
    fig = plt.figure('KNN classifier')
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(train_data[:4, 0], train_data[:4, 1],
               train_data[:4, 2], c='r', marker='o')
    ax.scatter(train_data[4:8, 0], train_data[4:8, 1],
               train_data[4:8, 2], c='y', marker='o')
    ax.scatter(train_data[8:12, 0], train_data[8:12, 1],
               train_data[8:12, 2], c='b', marker='o')
    ax.scatter(test_data[0], test_data[1], test_data[2],
               c=('r', 'y', 'b')[label], marker='*')
    ax.scatter(neighbors[:, 0], neighbors[:, 1],
               neighbors[:, 2], c='k', marker='x', s=50)
    ax.set_xlim3d(-1, 2)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(-2, 3)
    plt.savefig('q1.png')
    plt.show()
