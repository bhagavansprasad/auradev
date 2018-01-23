#!/usr/bin/python
import csv
import sys

def create_tuple_from_csv(filename):
	with open(filename) as fd:
		data=[tuple(line) for line in csv.reader(fd)]

	for row in data:
		print(row)

	print("")
	fd.close()

def create_list_from_csv(filename):
	with open(filename) as fd:
		data=[list(line) for line in csv.reader(fd)]

	fd.close()

	for row in data:
		print(row)

def main():
	filename = "data.csv"
	create_tuple_from_csv(filename)
	create_list_from_csv(filename)
	print("")

if (__name__ =='__main__'):
	main()

	
