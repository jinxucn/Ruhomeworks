#!/usr/bin/env python
# coding=utf-8
'''
@Author: Jin X
@Date: 2020-04-21 14:46:44
@LastEditTime: 2020-04-21 16:17:47
'''

import socket
import sys


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 6666))
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024).decode())
    while 1:
        cmd = ''
        while cmd == '':
            cmd = input('please input cmd: ')
        s.send(cmd.encode())
        data = s.recv(1024).decode()
        print(data)
        if data == 'connection closed':
            break
    s.close()


if __name__ == '__main__':
    socket_client()
