import threading
from threading import Thread, current_thread
import time

def t_entry_func_print_time():
    count = 0

    print("%d. %s, tid :%s" % (count, current_thread(), current_thread().getName()))

    while (count <= 10):
        print("%d. %s, tid :%s" % (count, current_thread(), current_thread().getName()))
        count += 1
        time.sleep(1)


def main():
	print("Before creating thread...")
	myt1 = threading.Thread(name='T1', target=t_entry_func_print_time)
	myt2 = threading.Thread(name='T2', target=t_entry_func_print_time)
	myt1.setDaemon(False)
	myt2.setDaemon(True)
	print("After creating thread...")
	myt1.start()
	myt2.start()

	print("main process ends")

if (__name__ == '__main__'):
	main()
