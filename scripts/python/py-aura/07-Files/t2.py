def read_10_bytes():
	fd = open("t.txt", "r")

	data = fd.read(10)
	print (data)

	fd.close()

def read_20_bytes():
	fd = open("t.txt", "r")

	data = fd.read(10)
	print (data)

	data = fd.read(10)
	print (data)

	fd.close()

def read_file_content():
	dlen = 5

	fd = open("t.txt", "r")

	while(dlen == 5):
		data = fd.read(5)
		dlen = len(data)
		print(("len :%d, data :%s" % (dlen, data)))

	fd.close()


read_10_bytes()
read_20_bytes()
read_file_content()

