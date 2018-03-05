import os

#on gracefull termination retval is 0
retval = os.system("ls")
print("ls  : retval :", hex(retval))
print("ls  : retval :", retval)

print ("")

#non zero otherwise
retval = os.system("lss")
print("lss : retval :", hex(retval))
print("lss : retval :", retval)
