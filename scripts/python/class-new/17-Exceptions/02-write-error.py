#!/usr/bin/python

try:
   fd = open("uses.csv", "r")
   fd.write("Writing to file")
   fd.close()
   print "I am in try block"

except IOError as err:
#except IOError:
    #print ("File Open failed errno :%d, message :%s" % (err.errno, err.strerror))
    print err.args
    #print ("File write failed")

else:
   print "Success in opeing file"

finally:
    print "I am in finally block"
