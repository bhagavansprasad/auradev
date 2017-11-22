import threading
from threading import Thread, current_thread
import time
import os

gdata = 0

def t_entry_func_print_time(delay):
    global gdata
    count = 1

    while count < 5:
        print "%d. %s, tid :%s, gdata :%d" % (count, current_thread(), current_thread().getName(), gdata)
        time.sleep(delay)
        count += 1
        gdata = gdata + 2

    print "%d. %s, tid :%s, gdata :%d exiting" % (count, current_thread(), current_thread().getName(), gdata)

def main():
    print "Proces pid :", os.getpid()

    print "Thread count ",  threading.active_count()

    try:
        myt1 = threading.Thread(name="T1", target=t_entry_func_print_time, args=(1,))
        myt1.start()

        myt2 = threading.Thread(name="T2", target=t_entry_func_print_time, args=(2,))
        myt2.start()
    except:
        print "Error: unable to start thread"
        exit(1)

    print "Thread count ",  threading.active_count()
    print "I am parent process waiting for Thread to join..."
    myt1.join()
    myt2.join()

if (__name__ == '__main__'):
    main()
