import os
import time
import sys

from multiprocessing import Process
 
def doubler1(number):
    print(("I am in '%s' function" % (sys._getframe().f_code.co_name)))
    result = number * 2
    proc = os.getpid()
    print(("-->proc:%d. double value is :%d" % (proc, result)))

def doubler2(number):
    print(("I am in '%s' function" % (sys._getframe().f_code.co_name)))
    result = number * 2
    proc = os.getpid()
    print(('-->proc:%d. double value is :%d' % (proc, result)))

def doubler3(number):
    print(("I am in '%s' function" % (sys._getframe().f_code.co_name)))
    result = number * 2
    proc = os.getpid()
    print(('-->proc:%d. double value is :%d' % (proc, result)))

def main():
    numbers = [5, 10, 15]
    entry_func_list = [doubler1, doubler2, doubler3]
    proc_list = []

    pid = os.getpid()

    print(('-->Parent :%d' % (pid)))

    for index, number in enumerate(numbers):
        proc = Process(target=entry_func_list[index], args=(number,))
        proc_list.append(proc)
        proc.start()

    for proc in proc_list:
        t = proc.join()
        print(help(proc.join))
        print (t)

    print('-->Parent :%d, exiting...' % (pid))

if (__name__ == '__main__'):
    main()
