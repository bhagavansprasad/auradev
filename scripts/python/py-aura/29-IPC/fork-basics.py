import os
import time

def single_process():
	print ('pid %d' % (os.getpid()))
	time.sleep(2)

	while(True):
		print ('pid %d' % (os.getpid()))
		time.sleep(1)

def new_process():
	os.fork()

	print ('pid %d' % (os.getpid()))
	time.sleep(5)

	while(True):
		print ('pid %d' % (os.getpid()))

def new_process_parent_n_child():
	retval = os.fork()

	if (retval == 0):
		print ('I am Child  pid :%d, retval :%d' % (os.getpid(), retval))
	else:
		print ('I am Parent pid :%d, retval :%d' % (os.getpid(), retval))

	print ("This is common statement pid :%d" % (os.getpid()))
	time.sleep(2)

def child_process(rfd):
    while(1):
        print ('I am Child   pid :%d, rfd :%d' % (os.getpid(), rfd))
        time.sleep(1)

def parent_process(wfd):
    while(1):
        print ('I am Parent  pid :%d, wfd :%d' % (os.getpid(), wfd))
        time.sleep(1)

def parent_n_child_in_loop():
	pipein = 0
	pipeout = 0
	#pipein, pipeout = os.pipe()

	if (os.fork() == 0):
		child_process(pipeout)
	else:
		parent_process(pipein)

	time.sleep(2)

def main():
	#single_process()
	#new_process()
	#new_process_parent_n_child()
	parent_n_child_in_loop()
	return

if (__name__ == '__main__'):
	main()

