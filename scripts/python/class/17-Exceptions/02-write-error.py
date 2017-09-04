#!/usr/bin/python
import sys

try:
   filehandle = open("usrs.csv", "r")
   filehandle.write("Writing to file")
   filehandle.close()
   print "I am in try block"

except IOError as err:
    #print ("File Open failed errno :%d, message :%s" % (err.errno, err.strerror))
    print err.args


else:
   print "Success in opeing file"

finally:
    print "I am in finally block"
