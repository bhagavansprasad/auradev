import os
import re
_replace_re = re.compile("foo")
ftypes = "\.py$"

def port_file(filename):
	tempfile = filename + ".temp"

	try:
		target = open(tempfile, "w")

	except IOError as err:
		print ("File Open failed errno :%d, message :%s, filename:%s" % (err.errno, err.strerror, tempfile))
		return -1	

	try:
		source = open(filename, "r")

	except IOError as err:
		print ("File Open failed errno :%d, message :%s, filename:%s" % (err.errno, err.strerror, filename))
		return -1	

	'''
	for line in source:

	line = _replace_re.sub("print(", line)
	target.write(line)
	os.rename(tempfile, file)
	'''


def list_all_files_recursively(path):
	for dirpath, dirnames, filenames in os.walk("./"):
		for filename in filenames:
			if (re.search(ftypes, filename)):
				filename = os.path.join(dirpath, filename)
				print (filename)
				port_file(filename)

if (__name__ == '__main__'):
	list_all_files_recursively("./")


	

