#!/usr/bin/python
import csv
import sys

#with open('data.csv') as f:
    #data=[tuple(line) for line in csv.reader(f)]

with open('users-data.csv') as f:
    data_list = [list(line) for line in csv.reader(f)]

'''
print data_list
print data_list[0]
print data_list[0][0]
print data_list[6][4]
'''

for user_info in data_list:
    print user_info
    print user_info[4]
exit(1)
