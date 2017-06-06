import os
import time


def child(pipeout):
  count = 1
  print "-->C: In Child"
  while True:
      verse = "Child writing message :%d\n" % count
      count += 1
      print "C: going to sleep before write"
      time.sleep(5)
      print "C: After sleep and before write"
      retval = os.write(pipeout, verse)
      print "C : write retval", retval
      if (count == 10):
          retval = os.write(pipeout, "bye\n")
          print "C : write retval", retval
          print "Child exiting..."
          time.sleep(1)
          break

def parent():
    print "-->P: In parent"
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        print "-->P: After fork"
        os.close(pipein)
        child(pipeout)
    else:
        os.close(pipeout)
        counter = 1
        pipein = os.fdopen(pipein)
        while True:
             print "P. Before reading..."
             sbuff = pipein.readline()[:-1]
             print 'P: received :%s' % (sbuff)
             if (sbuff == "bye"):
                 print "Parent exiting..."
                 break;
parent()
print ""

