#!/usr/bin/python
try:
   filehandle = open("uses.csv", "r")
   filehandle.write("Writing to file")
   filehandle.close()
   print "I am in try block"
except IOError:
   print "Error: Writing error"
   print filehandle.read()

#else:
   #print "Success in writint into file"
finally:
    print "I am in finally block"
