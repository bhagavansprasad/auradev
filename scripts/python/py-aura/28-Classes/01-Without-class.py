a = 10

def get_data():
    global a
    return a

def set_data(n):
	global a

	if (n < 0):
		return False
	a = n
	return a

def dump_data():
    global a
    print("a :%d" % a)

def increment_data(n):
    global a
    a = a + n
    return a

def main():
	#print (a)
	print("data :%d" % get_data())

	#a = a + 10
	increment_data(10)
	print("data :%d" % get_data())

	#a = a + 20
	increment_data(20)
	dump_data()

	print("data :%d" % get_data())
	set_data(100)
	print("data :%d" % get_data())

	set_data(-10)
	print("data :%d" % get_data())
	return

if (__name__ == "__main__"):
	main()
