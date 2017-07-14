#!/usr/bin/python
try:
   filehandle = open("use.csv", "r")
   #filehandle.write("Writing to file")
   #filehandle.close()
   print "I am in try block"

except IOError:
   print "Error: Writing error"

else:
   print "Success in opeing file"

finally:
    print "I am in finally block"
