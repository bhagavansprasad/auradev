fd = open("data.txt", 'r+')
fdata = fd.readlines()
print fdata

inspos = 5
insword = "Docker"
wcount = 0
bcount = 0

for (lindex, line) in enumerate(fdata):
    tline = line.rstrip()

    temp = len(tline.split())
    print temp, ":", tline
	
    wcount = wcount + temp
    if (wcount >= inspos):
        break
    bcount = bcount + len(line)

'''
print "inspos :", inspos
print "wcount :", wcount
print "bcount :", bcount
print "line   :", line
print "lindex :", lindex
'''

wcount = wcount - temp
i = 0
while(wcount < inspos):
    while (line[i] == ' '):
        i += 1
    while (line[i] != ' '):
        i += 1
    wcount += 1

bcount += i+1
fd.seek(bcount, 0)

fd.write(insword)
fd.write(line[i:])
for line in fdata[lindex+1:]:
    fd.write(line)
