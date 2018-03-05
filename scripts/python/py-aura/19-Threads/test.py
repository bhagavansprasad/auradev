import os
import sys

print("child pid :", os.getpid())

#sys.exit(5)
#status = connect_to_server("xxxxx")
status = -5

if (status < 0):
	sys.exit(-1)
else:
	sys.exit(0)
'''
'''
