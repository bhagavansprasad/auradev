f = open('a.txt', 'r')
lines = f.readlines()
print len(lines)
#for line in lines:
#	print line

with open('a.txt', 'r') as f:
	for line in f:
		print line


f = open('b.txt', 'a')
f.writelines('abc from script\nsecond line')
f.writelines('abc from script\nsecond line')
f.close()
