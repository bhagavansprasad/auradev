#!/usr/bin/env python

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

i = 1
while (i < 30):
	s.send(MESSAGE+str(i))
	data = s.recv(BUFFER_SIZE)
	print data
	i += 1
	time.sleep(1)

s.close()

print "received data:", data
