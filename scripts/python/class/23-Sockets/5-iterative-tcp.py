#!/usr/bin/env python

import socket

#TCP_IP = '127.0.0.1'
TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))

s.listen(5)

while(1):
    nfd, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = nfd.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        data = "server response" + data
        nfd.send(data.upper())  # echo
    nfd.close()
