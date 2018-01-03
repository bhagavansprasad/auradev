def simple_read_few_bytes(filename):
	fd = open(filename, "r")
	data = fd.read(5)
	print(("data :%s" % data))

	fd.close()

def simple_read_twice(filename):
	fd = open(filename, "rt")

	data = fd.read(10)
	print(("1: data :%s" % data))

	data = fd.read(10)
	print(("2: data :%s" % data))

	fd.close()

def read_compleate_text_file(filename):
	fd = open(filename, "rt")
	i = 1
	while(True):
		data = fd.read(10)
		length = len(data)
		print(("%d: len :%d, %s" % (i, length, data)))

		if (length < 10):
			break
		i = i + 1

	fd.close()

def read_line_text_file(filename):
	fd = open(filename, "rt")
	i = 1
	while(True):
		data = fd.readline()
		print(("%d : len :%d, %s" % (i, len(data), data)))
		if (len(data) <= 0):
			break
		i  = i + 1

	fd.close()

def read_lines_text_file(filename):
	fd = open(filename, "rt")

	data = fd.readlines()

	fd.close()

	print(("len :%d, %s" % (len(data), data)))

	i = 1
	for line in data:
		print(("%d. %s" % (i, line)))
		i = i + 1

def file_operations_seek(filename):
	fd = open(filename, "rt")
	print(("file position :%d" % fd.tell()))

	data = fd.read(10)
	print(("file position :%d" % fd.tell()))

	fd.seek(40)
	print(("file position :%d" % fd.tell()))

	data = fd.read(10)
	print(("file position :%d" % fd.tell()))

	fd.seek(0, 0)
	print(("file position :%d" % fd.tell()))

	fd.seek(10, 0)
	print(("file position :%d" % fd.tell()))

	fd.seek(20, 1)
	print(("file position :%d" % fd.tell()))

	fd.seek(-10, 2)
	print(("file position :%d" % fd.tell()))
	
	fd.seek(0, 2)
	print(("file position :%d" % fd.tell()))
	
	fd.seek(30, 0)
	print(("file position :%d" % fd.tell()))
	
	fd.seek(-10, 1)
	print(("file position :%d" % fd.tell()))
	
	print(("Name of the file  :%s" % fd.name))
	print(("Closed or not     :%r" % fd.closed))
	print(("Opening mode      :%r" % fd.mode))

	fd.close()
	return

def write_to_file(filename):
	fd = open(filename, "r+")
	print("file position :%d" % fd.tell())

	fd.write("Hello world")
	print("file position :%d" % fd.tell())

	fd.seek(30, 0)
	print("file position :%d" % fd.tell())

	fd.write("Hello world")
	print("file position :%d" % fd.tell())

	fd.close()
	return

def write_to_binary_file(filename):
	fd = open(filename, "w+")
	a = 100
	fd.write(a)

	fd.close()
	return


def main():
	filename = "t.txt"
	#simple_read_few_bytes(filename)
	#simple_read_twice(filename)
	#read_compleate_text_file(filename)
	#read_line_text_file(filename)
	#read_lines_text_file(filename)
	#file_operations_seek(filename)
	#write_to_file(filename)
	write_to_binary_file("a.txt")
	return
	
if (__name__ == "__main__"):
	main()

