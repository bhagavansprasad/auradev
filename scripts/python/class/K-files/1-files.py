fd = open("t.txt", "r")
print "Name of the file  :", fd.name
print "Closed or not     :", fd.closed
print "Opening mode      :", fd.mode
print "Softspace flag    :", fd.softspace

data = fd.read(10);

print data

print "file position ", fd.tell()

fd.close()
