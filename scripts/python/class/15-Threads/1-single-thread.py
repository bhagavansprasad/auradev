import thread
import time
import os

def print_time(tname, timeout):
   count = 0

   while count < 5:
      time.sleep(1)
      print "%d. %s, ident :%d" % (count, time.ctime(time.time()), thread.get_ident())
      count += 1

#print_time();

#print dir(thread)

# Create one thread as follows
print "Proces pid :", os.getpid()

try:
   thread.start_new_thread(print_time, ("T1", 1, ))
   thread.start_new_thread(print_time, ("T2", 1, ))
except:
   print "Error: unable to start thread"

print "I am parent process going to pass..."
while 1:
   pass
