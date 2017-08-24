import sys

print sys.argv
print sys.argv[0]
print len(sys.argv)
print "sys type  :", type(sys)
print "argv type :", type(sys.argv)

for args in sys.argv:
    print args

fd = open(sys.argv[1], "r")
list_of_servers = fd.readlines()

print list_of_servers 

for server in list_of_servers:
    print server
exit(1)

