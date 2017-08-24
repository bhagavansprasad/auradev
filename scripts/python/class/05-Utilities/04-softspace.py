import sys
print "hello",
sys.stdout.softspace=0
print "world",
print "!"

for i in range(1, 6):
    sys.stdout.softspace=0
    print i,
