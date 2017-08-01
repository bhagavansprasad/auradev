import os
import time
import sys

from multiprocessing import Process
 
def doubler1(number):
    print "I am in '%s' function" % (sys._getframe().f_code.co_name)
    result = number * 2
    proc = os.getpid()
    print '-->proc:%d. double value is :%d' % (proc, result)

def doubler2(number):
    print "I am in '%s' function" % (sys._getframe().f_code.co_name)
    result = number * 2
    proc = os.getpid()
    print '-->proc:%d. double value is :%d' % (proc, result)

def doubler3(number):
    print "I am in '%s' function" % (sys._getframe().f_code.co_name)
    result = number * 2
    proc = os.getpid()
    print '-->proc:%d. double value is :%d' % (proc, result)

numbers = [5, 10, 15]
proc_list = [doubler1, doubler2, doubler3]
procs = []

pid = os.getpid()

print '-->Parent :%d' % (pid)

for index, number in enumerate(numbers):
    proc = Process(target=proc_list[index], args=(number,))
    procs.append(proc)
    print "index :", index
    proc.start()

time.sleep(20)
for proc in procs:
    proc.join()
