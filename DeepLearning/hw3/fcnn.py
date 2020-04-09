#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-04-07 12:43:23
@LastEditTime: 2020-04-07 23:09:47
'''

import pickle
import numpy as np


def load():
    with open("mnist.pkl", 'rb') as f:
        mnist = pickle.load(f)
    return mnist["training_images"], mnist["training_labels"], mnist["test_images"], mnist["test_labels"]


# x_train, y_train, x_test, y_test = load()
# x_train = x_train.reshape(60000, 28*28)
# x_test = x_test.reshape(10000, 28*28)
# x_train = x_train.astype(float)
# x_test = x_test.astype(float)

step_size = 1e0


def relu(Z):
    return np.maximum(0, Z)


def relu_backward(dA, Z):
    dZ = np.array(dA, copy=True)
    dZ[Z <= 0] = 0
    return dZ


def softmax(x):
    row_max = x.max(axis=1, keepdims=True)
    normal_x = x - row_max
    exp_x = np.exp(normal_x)
    return exp_x/exp_x.sum(axis=1, keepdims=True)


# def loss(sm_x, lables):


x = np.random.randn(11, 784)*100
w1 = np.random.randn(784, 200)*0.1
b1 = np.random.randn(11, 200)*0.1
print(x.shape)

h1 = x.dot(w1)+b1
h1 = relu(h1)
print(h1.shape)


w2 = np.random.randn(200, 50)*0.1
b2 = np.random.randn(11, 50)*0.1

h2 = h1.dot(w2) + b2
h2 = relu(h2)
print(h2.shape)

w_out = np.random.randn(50, 10) * 0.1
b_out = np.random.randn(11, 10) * 0.1
out = h2.dot(w_out) + b_out

# out = np.array([[1, 2, 3, 4], [-3, 2, 3, 1]])
predict = softmax(out)
# labels = np.array([5, 2, 1, 5, 0, 1, 3, 6, 7, 9])
# labels = np.eye(11)[labels]
# dL = predict - labels
# print(dL)
labels = np.array([5, 2, 1, 5, 0, 1, 3, 6, 7, 9, 4])
dL = predict

dL[range(11), labels] -= 1
# dL /= x.shape[0]

dw_out = h2.T.dot(dL)
db_out = dL
dh2 = dL.dot(w_out.T)
w_out -= step_size * dw_out
b_out -= step_size * db_out

dw2 = h1.T.dot(dh2)
db2 = dh2
dh1 = dh2.dot(w2.T)
w2 -= step_size * dw2
b2 -= step_size * db2



a = {}
a['a'] = np.array([[1, 3], [2, 4], [3, 5]])
print(a['a'])
back(a)
print(a['a'])
# print(dL)
