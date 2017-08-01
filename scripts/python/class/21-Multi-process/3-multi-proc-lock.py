import os
import time
from multiprocessing import Process, Lock

my_global_variable = 0

def printer(item, lock):
    global my_global_variable    # Needed to modify global copy of globvar
    print '%d.%8s Before Modifying global data :%d' % (os.getpid(), item, my_global_variable)
    print '%d.%8s Locking critical section' % (os.getpid(), item)
    lock.acquire()
    print '%d.%8s Locking Success' % (os.getpid(), item)
    try:
        for i in range(1,4):
            print '%d.%8s **** In critical section...%d' % (os.getpid(), item,  i)
            time.sleep(1)
        my_global_variable += 1
        print '%d.%8s Out of critical section...' % (os.getpid(), item)
    finally:
        print '%d.%8s Before Unlock, global data :%d' % (os.getpid(), item, my_global_variable)
        lock.release()
        print '%d.%8s After  Unlock, global data :%d' % (os.getpid(), item, my_global_variable)
 
lock = Lock()
items = ['tango', 'foxtrot', 'aura']

#multiprocessing.log_to_stderr()
#logger = multiprocessing.get_logger()
#logger.setLevel(logging.INFO)

for item in items:
    p = Process(target=printer, args=(item, lock))
    p.start()
