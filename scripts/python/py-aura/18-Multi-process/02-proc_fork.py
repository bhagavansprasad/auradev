import os
import time

def parent_fun():
	while(1):
		print("P:Pid :%d, Ppid :%d" % (os.getpid(), os.getppid()))
		time.sleep(1)

def child_fun():
	while(1):
		print("C:Pid :%d, Ppid :%d" % (os.getpid(), os.getppid()))
		time.sleep(1)

def main():
	print ("Hello world")

	print("my process id pid :%d, ppid :%d" % (os.getpid(), os.getppid()))

	print ("Before fork")
	time.sleep(3)

	pid = os.fork()

	if (pid == 0):
		child_fun()
	else:
		parent_fun()

	print ("After fork...this statement will never print")

if (__name__ == '__main__'):
    main()
