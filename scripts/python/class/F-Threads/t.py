import threading
import time
import sys
import os

def my_print():
    i = 0

    print("Cartman lives: {0}".format(i))

    while True:
        print "T :", i
        i += 1
        time.sleep(1)

print "Before creating thread..."
myt1 = threading.Thread(name='cartman', target=my_print)
myt1.setDaemon(False)
print "After creating thread..."
myt1.start()

j = 0
while (j < 100):
    print "P :", j
    j += 1

