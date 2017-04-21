import os

print "parent ", os.getpid()

retval =  os.system("python test.py")

print hex(retval)
