import os

print "parent ", os.getpid()

retval =  os.system("python test.py")

print hex(retval)

if (retval == 0):
    print "Child process exited"
else:
    print "Child process exited with ERROR"


