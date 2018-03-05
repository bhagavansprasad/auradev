import os
import time
import sys

from multiprocessing import Process
 
def chld_starting_fun(number):
    print("I am in '%s' function" % (sys._getframe().f_code.co_name))
    result = number * 2
    pid = os.getpid()
    time.sleep(3)
    print('-->Child: pid :%d, ppid :%d, result :%d' % (pid, os.getppid(), result))

def main():
    proc_list = []
    pid = os.getpid()

    print('-->Parent: Before Child created :pid :%d, ppid :%d' % (pid, os.getppid()))

    newproc = Process(target=chld_starting_fun, args=(5,))

    print('-->Parent: After Child created :%d' % (pid))

    proc_list.append(newproc)

    print ('-->Parent: Starting the Child process')

    newproc.start()

    print ('-->Parent: After child started, going to wait for child to terminate')

    for proc in proc_list:
        proc.join()

    print ('-->Parent: Exiting')

if (__name__ == '__main__'):
    main()
