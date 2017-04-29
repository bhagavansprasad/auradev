fd = open("t.txt", "r")

print "file position ", fd.tell()

data = fd.read(10);
print data
print "file position ", fd.tell()

print ""

data = fd.read(10);
print data
print "file position ", fd.tell()

fd.seek(40)
print "file position ", fd.tell()

data = fd.read(10);
print data
print "file position ", fd.tell()

fd.seek(0, 0)
print "file position ", fd.tell()

fd.seek(10, 0)
print "file position ", fd.tell()

fd.seek(-10, 2)
print "file position ", fd.tell()

print "Name of the file  :", fd.name
print "Closed or not     :", fd.closed
print "Opening mode      :", fd.mode
print "Softspace flag    :", fd.softspace

print "---"
fd.seek(0, 0)
print "file position ", fd.tell()

data = fd.read(10);
print data
print "file position ", fd.tell()

fd.seek(-1, 1)
print "file position ", fd.tell()
data = fd.read(10);
print data
print "file position ", fd.tell()

fd.close()
