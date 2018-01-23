#!/usr/bin/python
import csv
import sys

def get_csv_data(filename):
	with open(filename, "rt") as fd:
		data=[list(line) for line in csv.reader(fd)]

	fd.close()

	return data

def count_http_req_by_ret_code(cdata, retcode):
	count = 0
	first_row = 0
	for row in cdata:
		if (first_row == 0): #ignore title/header row
			first_row = 1
			continue

		if ((int(row[5])) == retcode):
			count = count + 1
			print("%-16s %-5s %-4s" % (row[0], row[4], row[5]))
	
	print (count)

def main():
	filename = "web-req-data.csv"
	cdata = get_csv_data(filename)

	count_http_req_by_ret_code(cdata, 200)
	print("")

	count_http_req_by_ret_code(cdata, 400)
	print("")

if (__name__ =='__main__'):
	main()

	
