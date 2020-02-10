#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-02-07 15:46:39
@LastEditTime : 2020-02-10 13:59:22
'''

from time import perf_counter


def fastest3sum(data):
    count = 0
    for i in range(len(data)):      # use two local index to go over the array in the secondary loop
        j = i + 1                   # j goes from the left side to the right
        k = len(data) - 1           # k goes from the right side to the left
        while j < k:                #until they meet
            if data[i] + data[j] + data[k] > 0:     # if it's too big
                k -= 1                              # find a smaller one
            elif data[i] + data[j] + data[k] < 0:   # if too small
                j += 1                              # find a greater one
            else:                                   # deal with duplicate data
                jsame = 1
                ksame = 1
                while j + jsame < k and data[j] == data[j + jsame]:
                    jsame += 1
                while k - ksame > j and data[k] == data[k - ksame]:
                    ksame += 1
                count += jsame * ksame
                j += jsame
                k -= ksame
    return count


if __name__ == "__main__":
    '''
    Test data is generated by np.random.randint(low,high,len)
    Runtest print out the total number of matches and the runtime
    '''
    sizes = [128, 512, 1024, 4096, 8192, 16384]
    for size in sizes:
        a = []
        with open('./data/{}int.txt'.format(size), 'r') as f:
            for line in f.readlines():
                a.append(int(line))
        a.sort()
        print('{:5d}'.format(size), end=' ')
        tstart =  perf_counter()
        print('{} matches'.format(fastest3sum(a)), end=' ')
        endtime =  perf_counter()
        print('takes {:.3f} ms'.format(1000*(endtime - tstart)))
