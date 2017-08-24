#!/usr/bin/env python
import socket
import time

sip_addr = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.connect((sip_addr, TCP_PORT))

sockfd.send(MESSAGE)

data = sockfd.recv(BUFFER_SIZE)

print data

time.sleep(1)

sockfd.close()
