#!/usr/bin/python
import csv
import sys

fd = 0

try:
    fd = open('data.csv', 'rt')
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    #print "%d %s" % (e.errno, e.strerror)
    exit(1)


data_list = []

#print fd.read(50)

reader = csv.reader(fd)

print "reader type :", type(reader)
print next(reader)
print next(reader)
print reader.next()


for row in reader:
    print row
    #print "row type :", type(row), "row[0] type :", type(row[0]), row[0], "row[3] type :", type(row[3]), row[3]
    data_list.append(row)

print "data_list :", data_list

print ("-" * 20)
for row in data_list:
    print row

print ("-" * 20)
exit(1)
print data_list
print data_list[0]
print data_list[1]
print ("-" * 20)
exit(1)

print data_list[0][0]
print type(data_list[0][0])
print int(data_list[0][0])
print type(int(data_list[0][0]))

if  (int(data_list[0][0]) > int(data_list[1][0])):
    t = data_list[0]
    data_list[0] = data_list[1]
    data_list[1] = t

print data_list[0]
print data_list[1]

fd.close()


