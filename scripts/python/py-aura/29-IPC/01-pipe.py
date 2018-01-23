import os
import time


def child(wfd):
  count = 1
  print("-->C: In Child")
  while True:
      buff = "Child writing message :%d\n" % count
      count += 1
      print("C: going to sleep before write")
      time.sleep(2)
      print("C: After sleep and before write")
      retval = os.write(wfd, buff)
      print("C : write retval", retval)
      if (count == 5):
          retval = os.write(wfd, "bye")
          print("C : write retval", retval)
          print("Child exiting...")
          time.sleep(1)
          break

def parent(rfd):
    print("-->P: In parent")
    counter = 1
    rfd = os.fdopen(rfd)
    while True:
        print("P. Before reading...")
        sbuff = rfd.readline()[:]
        print('P: received :%s' % (sbuff))

        if (len(sbuff) <= 0):
            break

        if (sbuff == "bye"):
            print("Parent exiting...")
            break;
def main():
	rfd, wfd  = os.pipe()

	if os.fork() == 0:
		os.close(rfd)
		child(wfd)
	else:
		os.close(wfd)
		parent(rfd)

	return

if (__name__ == '__main__'):
	main()
