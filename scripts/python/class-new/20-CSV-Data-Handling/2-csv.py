#!/usr/bin/python
import csv
import sys

#with open('data.csv') as f:
    #data=[tuple(line) for line in csv.reader(f)]

with open('data.csv') as f:
    data=[list(line) for line in csv.reader(f)]

print (data)
for row in data:
    print row
