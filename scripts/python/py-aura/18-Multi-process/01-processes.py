import os
import time

print ("Hello world")

print("my process id pid :%d, ppid :%d" % (os.getpid(), os.getppid()))

print ("Before fork")
time.sleep(3)

os.fork()

print ("After fork")
time.sleep(3)

while(1):
    print("Pid :%d, Ppid :%d" % (os.getpid(), os.getppid()))
    time.sleep(1)
