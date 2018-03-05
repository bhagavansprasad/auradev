import os
import time
import sys

from multiprocessing import Process
 
def doubler1(number):
    print("I am in '%s' function" % (sys._getframe().f_code.co_name))
    result = number * 2
    proc = os.getpid()
    print('-->proc:%d. double value is :%d' % (proc, result))

def doubler2(number):
    print("I am in '%s' function" % (sys._getframe().f_code.co_name))
    result = number * 2
    proc = os.getpid()
    print('-->proc:%d. double value is :%d' % (proc, result))

def doubler3(number):
    print("I am in '%s' function" % (sys._getframe().f_code.co_name))
    result = number * 2
    proc = os.getpid()
    print('-->proc:%d. double value is :%d' % (proc, result))

def main():
	proc_list = []

	pid = os.getpid()

	print('-->Parent :%d' % (pid))

	proc1 = Process(target=doubler1, args=(10,))
	proc2 = Process(target=doubler2, args=(15,))
	proc3 = Process(target=doubler3, args=(20,))

	proc_list.append(proc1)
	proc_list.append(proc2)
	proc_list.append(proc3)

	proc1.start()
	proc2.start()
	proc3.start()

	for proc in proc_list:
		proc.join()
	print('-->Parent :%d, exiting...' % (pid))

if (__name__ == '__main__'):
    main()
