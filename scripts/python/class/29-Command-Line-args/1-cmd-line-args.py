import sys

n = 5
for i in range (1, n+1):
	print (i), 

print ""

print ("argv       :", sys.argv)
print ("argv[0]    :", sys.argv[0])
print ("argv[1]    :", sys.argv[1])
print ("args count :", len(sys.argv))

n = int(sys.argv[1])

for i in range (1, n+1):
	print (i), 

print ("")
for i, args in enumerate(sys.argv):
    print ("argv[%d]: %s" % (i, args))

fd = open(sys.argv[2], "r")
data = fd.readlines()
print data 
exit(1)

for server in data:
    print server
