import thread
import os
import time
from multiprocessing import Process, Lock

my_global_variable = 0
tcount = 0

def printer(item, delay, lock):
    global my_global_variable 
    global tcount
    tcount += 1
    print '%d.%8s Before Modifying global data :%d' % (os.getpid(), item, my_global_variable)
    print '%d.%8s Locking critical section' % (os.getpid(), item)
    lock.acquire()
    print '%d.%8s Locking Success' % (os.getpid(), item)
    try:
        for i in range(1,4):
            print '%d.%8s **** In critical section...%d sec, global_data :%d' % (os.getpid(), item,  i, my_global_variable)
            time.sleep(1)
            my_global_variable += 1
        print '%d.%8s Out of critical section...' % (os.getpid(), item)
    finally:
        print '%d.%8s Before Unlock, global data :%d' % (os.getpid(), item, my_global_variable)
        lock.release()
        print '%d.%8s After  Unlock, global data :%d' % (os.getpid(), item, my_global_variable)
        tcount -= 1
 
lock = Lock()
items = ['ganga', 'kaveri', 'penna']
i = 0
new_threads_list = []

for tname in items:
    #p = Process(target=printer, args=(item, lock))
    #p.start()
	try:
		nthread = thread.start_new_thread(printer, (tname, i, lock) )
		new_threads_list.append(nthread) 
		i += 1
	except:
		print "Error: unable to start thread"

#while (tcount > 0):
#while (True):
	#pass

c = raw_input("Type something to quit.")

print "Main process exiting"
