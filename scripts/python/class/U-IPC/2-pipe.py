import os
import time

def child(pipeout):
  bottles = 10
  while True:
    bob = "bottles of beer"
    otw = "on the wall"
    take1 = "Take one down and pass it around"
    store = "Go to the store and buy some more"

    if bottles > 0:
      values =  (bottles, bob, otw, bottles, bob, take1, bottles - 1,bob,otw)
      verse = "%2d %s %s,\n%2d %s.\n%s,\n%2d %s %s.\n" % values
      os.write(pipeout, verse)
      bottles -= 1
      time.sleep(1)
    else:
      bottles = 9
      values =  (bob, otw, bob, store, bottles, bob,otw)
      verse = "No more %s %s,\nno more %s.\n%s,\n%2d %s %s.\n" % values
      os.write(pipeout, verse)
      time.sleep(1)

def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        os.close(pipein)
        child(pipeout)
    else:
        os.close(pipeout)
        counter = 1
        pipein = os.fdopen(pipein)
        while True:
            print 'verse %d' % (counter)
            for i in range(4):
                verse = pipein.readline()[:-1]
                print '%s' % (verse)
            counter += 1
            print
            time.sleep(1)

parent()

