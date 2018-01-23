import threading
from threading import Thread, current_thread
import time
import os

def t_entry_func_print_time(timeout):
    count = 1

    while count < 5:
        print("%d. %s, tid :%s" % (count, current_thread(), current_thread().getName()))
        time.sleep(1)
        count += 1

    print("%d. %s, tid :%s exiting..." % (count, current_thread(), current_thread().getName()))

def main():
    print("Proces pid :", os.getpid())

    print("Thread count ",  threading.active_count())

    try:
        myt1 = threading.Thread(name="T1", target=t_entry_func_print_time, args=(1,))
        myt1.start()
    except:
        print ("Error: unable to start thread")
        exit(1)

    print("Thread count ",  threading.active_count())
    print ("I am parent process waiting for Thread to join...")
    myt1.join()

if (__name__ == '__main__'):
    main()
