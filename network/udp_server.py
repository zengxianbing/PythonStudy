__author__ = 'xianbing'
# -*- coding: utf-8 -*-

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999))
print 'Bind UDP on 999....'
while True:
    data,addr=s.recvfrom(1024)
    print 'Received from %s:%s.'%addr
    s.sendto('Hello,%s!'%data,addr)