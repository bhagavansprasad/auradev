'''
def hello_function_10():
	fd = open("t.txt", "r")
	data = fd.read(10)
	print (data)
	fd.close()


def hi_function_20():
	print ("Hi world")

	fd = open("t.txt", "r")
	data = fd.read(10)
	print (data)

	data = fd.read(10)
	print (data)

	fd.close()



hello_function_10()
hi_function_20()
'''

fd = open("t.txt", "r")
data = fd.read(10)
print (data)
fd.close()


