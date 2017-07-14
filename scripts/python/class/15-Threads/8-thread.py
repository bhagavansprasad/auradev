import threading
from threading import Thread, current_thread
import time
import os

def print_time():
   count = 0
   while count < 1:
      count += 1
      print "In thread :", count, threading
      print current_thread()
      print current_thread().getName()
      time.sleep(1)

print "Proces pid :", os.getpid()
try:
   print dir(threading)
   myt1 = threading.Thread(name='aura1', target=print_time)
   myt2 = threading.Thread(name='aura2', target=print_time)

   myt1.start()
   myt2.start()

   print dir(myt1)

   print "Thread count ", threading.active_count()
   print "current Thread", threading.current_thread()
   print "current Thread", threading.currentThread()

   myt1.join()
   myt2.join()
except:
   print "Error: unable to start thread"

print "I am parent process going to exiting..."
