import time
import os

i = 0
while True:
    print '-->%d. i :%d' % (os.getpid(), i)
    i += 1
    time.sleep(1)
