__author__ = 'xianbing'
# -*- coding: utf-8 -*-

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

for data in ['Michael','Tracy','Sarah']:
    s.sendto(data,('127.0.0.1',9999))
    print s.recv(1024)
s.close()
