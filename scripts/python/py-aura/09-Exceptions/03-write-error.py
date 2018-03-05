#!/usr/bin/python
def sample1():
	try:
		fd = open("users.csv", "r")
		fd.write("Writing to file")
		fd.close()
		print("I am in try block")

	except IOError as err:
		print ("Got execption because of some reason...")

	else:
		print("Success in opeing file")

	finally:
		print("I am in finally block")
	print ("")

def sample2():
	try:
		fd = open("users.csv", "r")
		fd.write("Writing to file")
		fd.close()
		print("I am in try block")

	except IOError as err:
		print ("Got execption because of bellow reason...")
		print (err)
		print (err.args)
	else:
		print("Success in opeing file")

	finally:
		print("I am in finally block")

	print ("")

def sample3():
	try:
		fd = open("user.csv", "r")
		fd.close()
		print("I am in try block")

	except IOError as err:
		print ("File Open failed errno :%d, message :%s" % (err.errno, err.strerror))
		print(err.args)
	else:
		print("Success in opeing file")

	finally:
		print("I am in finally block")

	print ("")

def main():
	#sample1()
	#sample2()
	#sample3()
	return


if (__name__ == "__main__"):
	main()
