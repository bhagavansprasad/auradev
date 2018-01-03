def read_file_content():
	i = 1
	dlen = 30

	fd = open("t.txt", "r")

	while(dlen == 30):
		data = fd.read(30)
		dlen = len(data)
		print(("%d. len :%d, data :%s" % (i, dlen, data)))
		i = i + 1

	fd.close()


def main():
	read_file_content()


if (__name__ == "__main__"):
	main()
