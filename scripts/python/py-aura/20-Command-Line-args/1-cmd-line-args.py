import sys

n = 5
for i in range (1, n+1):
	print ("%3d" % (i), end=''), 

print ("")

print ("argv       :", sys.argv)
print ("args count :", len(sys.argv))
print ("argv[0]    :", sys.argv[0])
print ("argv[1]    :", sys.argv[1])

n = int(sys.argv[1])
print (n)

for i in range (1, n+1):
	print ("%3d" % (i), end=''), 

print ("")

for i, args in enumerate(sys.argv):
    print ("argv[%d]: %s" % (i, args))

fd = open(sys.argv[2], "r")
data = fd.readlines()
print (data)

for temp in data:
    print (temp)

exit(1)
