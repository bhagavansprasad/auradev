import thread
import time
import os

x = 10
# Define a function for the thread
def print_time( threadName, delay):
   global x
   count = 0

   while count < 5:
      time.sleep(delay)
      count += 1
      print "%d. %s: %s, x: %d" % (count, threadName, time.ctime(time.time()), x)
      x += 1

# Create two threads as follows
print "Proces pid :", os.getpid()
try:
   thread.start_new_thread( print_time, ("T1", 1, ) )
   thread.start_new_thread( print_time, ("T2", 2, ) )
except:
   print "Error: unable to start thread"

print "I am parent process going to exit..."
while 1:
   pass
