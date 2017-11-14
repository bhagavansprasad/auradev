
fd = open("t.txt", 'r+')
print "Open success"

fd.seek(150, 0)
print "file position ", fd.tell()

print dir(fd)

fd.write("Hello world")

fd.seek(-11, 2)
print "file position ", fd.tell()
fd.write("Hello world")

fd.close()

with open("t.txt", 'r') as fd:
    file_content = fd.readlines()

print file_content
fd.close()

for row in file_content:
    print row

exit(1)


