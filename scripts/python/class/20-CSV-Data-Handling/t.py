import csv

i = 0

with open('data.csv') as f:
    data = [list(line) for line in csv.reader(f)]

'''
for row in data:
    print ("%d. %s" % (i, row))
    i = i + 1
'''

'''
print data[3]
if (data[3][1] == "slde"):
    print data[3][3]
else:
    print data[3][2]
'''


for row in data:
    if (row[1] == "slide"):
        print row
    i = i + 1
