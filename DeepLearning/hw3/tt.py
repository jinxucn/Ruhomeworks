#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-04-08 19:17:55
@LastEditTime: 2020-04-08 19:41:01
'''

from torch.utils.data import DataLoader,TensorDataset
import numpy as np
import torch


def linear_f(x):
    y = 5 * x + np.sin(x) * x + np.random.normal(
        0, scale=1, size=x.size) # y = 5*x + x*sin(x) + noise
    return y


model = torch.nn.Sequential(
    torch.nn.Linear(4, 2),
).cuda()
# loss_fn = torch.nn.CrossEntropyLoss()
num = 30
x_train = np.linspace(0, 50, num=num)  # 从0-50生成num多个点
y_train = linear_f(x_train)
x_train = torch.Tensor(x_train)  # 转化为张量
y_train = torch.Tensor(y_train)
myset = TensorDataset(x_train,y_train)
myloader = DataLoader(dataset=myset, batch_size=1,
                      shuffle=False, num_workers=2)
if __name__ == "__main__":
    for train, labels in myloader:
        print(train)
        model(train.cuda())
