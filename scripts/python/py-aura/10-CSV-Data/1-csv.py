#!/usr/bin/python
import csv

def open_file_by_name(filename):
	fd = 0
	try:
		fd = open('data.csv', 'rt')
	except IOError as e:
		print ("I/O error({0}): {1}".format(e.errno, e.strerror))
		#print "%d %s" % (e.errno, e.strerror)
		exit(1)

	return fd

def close_file_by_fd(fd):
	fd.close()

def read_sample_data_from_csv(fd):
	fdata = csv.reader(fd)
	print ("fdata type :", type(fdata))

	print (next(fdata))
	print (next(fdata))
	print ("")

def dump_data_from_csv_file(filename):
	data_list = []

	fd = open_file_by_name(filename)
	fdata = csv.reader(fd)

	for row in fdata:
		print (row)
		data_list.append(row)

	print ("")

	print (data_list)

	print ("-" * 20)
	for row in data_list:
		print (row)

	print ("-" * 20)

	close_file_by_fd(fd)


def get_data_by_csv_file(filename):
	data_list = []

	fd = open_file_by_name(filename)

	fdata = csv.reader(fd)

	for row in fdata:
		print (row)
		data_list.append(row)

	close_file_by_fd(fd)

	return (data_list)


def operate_csv_data(data_list):

	print ("data_list[0] :", data_list[0])
	print ("data_list[1] :", data_list[1])

	print (data_list[0][0])
	print (data_list[1][0])

	if  (int(data_list[0][0]) > int(data_list[1][0])):
		t = data_list[0]
		data_list[0] = data_list[1]
		data_list[1] = t

	print ("-" * 20)
	print ("data_list[0] :", data_list[0])
	print ("data_list[1] :", data_list[1])

	print ("-" * 20)
	for row in data_list:
		print (row)

def main():
	filename = "data.csv"

	fd = open_file_by_name(filename)
	read_sample_data_from_csv(fd)
	close_file_by_fd(fd)

	dump_data_from_csv_file(filename)

	dlist = get_data_by_csv_file(filename)
	operate_csv_data(dlist)
	return

if (__name__ =='__main__'):
	main()

