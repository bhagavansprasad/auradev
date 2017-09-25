import os
import time


'''
print 'pid %d' % (os.getpid())
time.sleep(5)

while(True):
    print 'pid %d' % (os.getpid())
exit(1)
'''

'''
os.fork()

print 'pid %d' % (os.getpid())
time.sleep(5)

while(True):
    print 'pid %d' % (os.getpid())
exit(1)
'''


'''

retval = os.fork()

if retval == 0:
    print 'I am Child  pid :%d, retval :%d' % (os.getpid(), retval)
else:
    print 'I am Parent pid :%d, retval :%d' % (os.getpid(), retval)

print "This is common statement"
time.sleep(2)
'''

def child_process(rfd):
    while(1):
        print 'I am Child   pid :%d, rfd :%d' % (os.getpid(), rfd)
        time.sleep(1)

def parent_process(wfd):
    while(1):
        print 'I am Parent  pid :%d, wfd :%d' % (os.getpid(), wfd)
        time.sleep(1)

    
pipein, pipeout = os.pipe()

if os.fork() == 0:
    child_process(pipeout)
else:
    parent_process(pipein)

time.sleep(2)
