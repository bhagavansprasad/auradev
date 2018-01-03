import threading
from threading import Thread, current_thread
import time

def print_hai(timeout):
	while(True):
		print ("T1: Hai")
		time.sleep(1)

def print_hello(timeout):
	while(True):
		print ("T2 : Hello")
		time.sleep(1)

def main():

	myt1 = threading.Thread(name="T1", target=print_hai, args=(1,))
	myt1.start()

	myt2 = threading.Thread(name="T2", target=print_hello, args=(2,))
	myt2.start()

	print(("Thread count ",  threading.active_count()))
	print ("I am parent process waiting for Thread to join...")
	myt1.join()
	myt2.join()


if (__name__ == '__main__'):
	main()


