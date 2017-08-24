#!/usr/bin/env python
import socket


TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20 



sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.bind((TCP_IP, TCP_PORT))

sockfd.listen(5)

conn, addr = sockfd.accept()
print 'Connection address:', addr

data = conn.recv(BUFFER_SIZE)
print "received data:", data

conn.send(data.upper())  # echo

conn.close()
