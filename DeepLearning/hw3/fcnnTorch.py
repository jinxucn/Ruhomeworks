#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-04-08 14:18:58
@LastEditTime: 2020-04-08 23:10:30
'''
import pickle
from torch.utils.data import DataLoader, TensorDataset
from time import perf_counter
import torch


def load():
    with open("mnist.pkl", 'rb') as f:
        mnist = pickle.load(f)
    return mnist["training_images"], mnist["training_labels"], mnist["test_images"], mnist["test_labels"]


# load data, and transform to tensor, and put in cuda
x_train, y_train, x_test, y_test = load()
x_train = x_train.reshape(60000, 28*28)
x_test = x_test.reshape(10000, 28*28)
x_train = torch.from_numpy(x_train.astype(float)).float()
x_test = torch.from_numpy(x_test.astype(float)).float().cuda()
y_train = torch.from_numpy(y_train).long()
y_test = torch.from_numpy(y_test).long().cuda()

# hyperparameters
leanring_rate = 0.02
epochs = 10
batch_size = 128

# specify model using nn.Sequential, and put in cuda
model = torch.nn.Sequential(
    torch.nn.Linear(784, 200),
    torch.nn.ReLU(),
    torch.nn.Linear(200, 50),
    torch.nn.ReLU(),
    torch.nn.Linear(50, 10),
    torch.nn.Softmax(dim=1)
).cuda()
# initialize optimizer, using mini-batch SGD
optimizer = torch.optim.SGD(model.parameters(), lr=leanring_rate)
# specify loss function is cross-entropy loss, and put in cuda
loss_fn = torch.nn.CrossEntropyLoss().cuda()
# initialize Dataset and DataLoader for seperating batches
trainingSet = TensorDataset(x_train, y_train)
loader = DataLoader(
    dataset=trainingSet,
    batch_size=batch_size,
    shuffle=True,
    num_workers=2,
)
if __name__ == "__main__":

    start = perf_counter()  # strat time
    for i in range(1, epochs+1):
        correct = 0
        for train, label in loader:
            # load data and put into cuda
            train, label = train.cuda(), label.cuda()
            # for each batch refresh the gradient
            optimizer.zero_grad()
            # predict, forward one batch
            predict = model(train)
            # sum up correct in each batch
            correct += (torch.argmax(predict, 1) ==
                        label).sum().float().cpu().numpy()
            # accuracy.append(
            #     ((torch.argmax(predict, 1) == label).sum().float()/len(label)).cpu().numpy())
            # calculate loss
            loss = loss_fn(predict, label)
            # backward one batch with autograd
            loss.backward()
            # update the weights and bias
            optimizer.step()
        print("epoch: {:2d}, training accuracy: {:.2f} %".format(
            i, correct/len(y_train)*100))
    # synchronize threads, wait until all branch threads finished
    torch.cuda.synchronize()
    # end time
    end = perf_counter()
    # predict testing set
    predict = model(x_test)
    # calculate accuracy
    accuracy = ((torch.argmax(predict, 1) == y_test).sum().float() /
                len(y_test)).cpu().numpy()
    print("testing accuracy: {:.2f} %, runtime: {:.1f} s".format(
        accuracy*100, end - start))
