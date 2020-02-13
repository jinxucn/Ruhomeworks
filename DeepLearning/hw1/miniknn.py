#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-12 21:33:19
@LastEditTime : 2020-02-13 18:27:56
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.use('Agg')


# load mini training data and labels
mini_train = np.load('knn_minitrain.npy')
mini_train_label = np.load('knn_minitrain_label.npy')

# randomly generate test data
mini_test = np.random.randint(20, size=20)
mini_test = mini_test.reshape(10, 2)


# Define knn classifier
def kNNClassify(newInput, dataSet, labels, k):
    result = []
    ########################
    # Input your code here #
    ########################

    ####################
    # End of your code #
    ####################
    return result


outputlabels = kNNClassify(mini_test, mini_train, mini_train_label, 4)

print('random test points are:', mini_test)
print('knn classfied labels for test:', outputlabels)

# plot train data and classfied test data
train_x = mini_train[:, 0]
train_y = mini_train[:, 1]
fig = plt.figure()
plt.scatter(train_x[np.where(mini_train_label == 0)],
            train_y[np.where(mini_train_label == 0)], color='red')
plt.scatter(train_x[np.where(mini_train_label == 1)],
            train_y[np.where(mini_train_label == 1)], color='blue')
plt.scatter(train_x[np.where(mini_train_label == 2)],
            train_y[np.where(mini_train_label == 2)], color='yellow')
plt.scatter(train_x[np.where(mini_train_label == 3)],
            train_y[np.where(mini_train_label == 3)], color='black')

test_x = mini_test[:, 0]
test_y = mini_test[:, 1]
outputlabels = np.array(outputlabels)
plt.scatter(test_x[np.where(outputlabels == 0)],
            test_y[np.where(outputlabels == 0)], marker='^', color='red')
plt.scatter(test_x[np.where(outputlabels == 1)],
            test_y[np.where(outputlabels == 1)], marker='^', color='blue')
plt.scatter(test_x[np.where(outputlabels == 2)], test_y[np.where(
            outputlabels == 2)], marker='^', color='yellow')
plt.scatter(test_x[np.where(outputlabels == 3)], test_y[np.where(
            outputlabels == 3)], marker='^', color='black')

# save diagram as png file
plt.savefig("miniknn.png")
