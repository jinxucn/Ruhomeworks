#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-04-21 14:39:50
@LastEditTime: 2020-04-21 16:16:54
'''

import socket
import threading
import time
import sys

filenames = ['test1.txt', 'test2.txt']


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


def readfile(filename):
    res = None
    if filename in filenames:
        with open(filename, 'rb') as f:
            res = f.read(1024)
    return res


def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))
    conn.send(('Hi, Welcome to the server!').encode())
    while 1:
        data = conn.recv(1024).decode()
        time.sleep(0.1)
        try:
            cmd = data[0: data.index(' ')]
        except ValueError:
            if data in ('exit', 'EXIT'):
                cmd = 'exit'
            else:
                cmd = None
        if cmd in ('get', 'GET'):
            name = data[data.index(' ')+1: len(data)]
            res = readfile(name)
            if not res:
                conn.send('file does exist'.encode('utf-8'))
            else:
                conn.send(res)
        elif cmd in ('BOUNCE', 'bounce'):
            if data.index(' ') + 1 == len(data):
                conn.send(' '.encode('utf-8'))
            else:
                res = data[data.index(' ')+1: len(data)]
                conn.send(res.encode('utf-8'))
        elif cmd == 'exit':
            if len(data) <= 5:
                print('normal exit')
            else:
                code = data[data.index(' ')+1:len(data)]
                print('exit:', code)
            conn.send('connection closed'.encode('utf-8'))
            conn.close()
            return
        else:
            conn.send('cmd invalid'.encode('utf-8'))

    conn.close()


if __name__ == '__main__':
    socket_service()
    # print(readfile('test1.txt'))
