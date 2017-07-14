import threading
import time

def worker():
    print 'Worker'
    time.sleep(5)
    print 'Worker'
    return

items = ['ganga', 'kaveri', 'penna']
i = 0
threads = []
for i in range(4):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
print threads

print "Parent I am also exiting"
