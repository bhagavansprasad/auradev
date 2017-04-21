import threading
import time
import sys
import os

def kenny(num=0):
    if num > 3:
        # print("Kenny dies now...")
        # raise SystemExit #Kenny will die, but Cartman will live forever
        # sys.exit(1) #Same as above

        print("Kenny dies and also kills Cartman!")
        os._exit(1)
    while True:
        print("Kenny lives: {0}".format(num))
        time.sleep(1)
        num += 1
        kenny(num)

def cartman():
    i = 0
    while True:
        print("Cartman lives: {0}".format(i))
        i += 1
        time.sleep(1)

if __name__ == '__main__':
    daemon_kenny = threading.Thread(name='kenny', target=kenny)
    daemon_cartman = threading.Thread(name='cartman', target=cartman)
    daemon_kenny.setDaemon(True)
    daemon_cartman.setDaemon(True)

    daemon_kenny.start()
    daemon_cartman.start()
    daemon_kenny.join()
    daemon_cartman.join()
