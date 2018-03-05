import os

print("Parent ", os.getpid())

retval =  os.system("python test.py")

print("retval :", hex(retval))

if (retval == 0):
    print("Child process exited Gracefully ")
else:
    print("Child process exited with ERROR")


