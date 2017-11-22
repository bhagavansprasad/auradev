#01-sm.py sum a b  
#01-sm.py diff a b  
#01-sm.py prod a b  
#01-sm.py div a b  

#example
#01-sm.py sum  10 20   --> 30
#01-sm.py diff 20 10   --> 10
#01-sm.py prod  5 10   --> 50
#01-sm.py div   30 5   --> 6

import sys

def get_sum(a, b):
	return a + b

def get_difference(a, b):
	return a - b

def get_product(a, b):
	return a * b

def get_divident(a, b):
	return a / b

def main(argv):
	i = 0

	if (len(argv) < 4):
		print ("Invalid or Insufficient arguments")
		print ("Usage:  python <a.py> <sum/diff/prod/div> <value 1> <value 2>")
		print ("Example:python 01-sm-genaral.py add 10 20")
		exit(1)

	print ("")
	a = int(argv[2])
	b = int(argv[3])

	'''
	for args in (argv):
		print ("%d.  %s" % (i, argv[i]))
		i = i + 1
	'''
	if (argv[1] == "add"):
		t = get_sum(a, b)
		print (t)
	elif (argv[1] == "diff"):
		t = get_difference(a, b)
		print (t)
	elif (argv[1] == "prod"):
		t = get_product(a, b)
		print (t)
	elif (argv[1] == "div"):
		t = get_divident(a, b)
		print (t)
	else:
		print ("Invalid command")

	return
	
if (__name__ == "__main__"):
	main(sys.argv)
