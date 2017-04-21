import threading
import time
import sys
import os

def my_print():
    i = 0

    print("Cartman lives: {0}".format(i))
    i += 1
    time.sleep(1)

myt1 = threading.Thread(name='cartman', target=my_print)
myt1.start()
myt1.join()
