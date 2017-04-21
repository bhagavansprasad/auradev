import sys
import os
import time

print "child ", os.getpid()
time.sleep(5)
sys.exit(5)
