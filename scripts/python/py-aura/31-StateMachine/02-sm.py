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

def get_dividend(a, b):
	return a / b

state_machine = {
	"sum"  : get_sum,
	"diff" : get_difference,
	"prod" : get_product,
	"div"  : get_dividend
}

def print_help():
	print ("Invalid or Insufficient arguments")
	print ("Usage:  python <a.py> <sum/diff/prod/div> <value 1> <value 2>")
	print ("Example:python 01-sm-genaral.py add 10 20")

def main(argv):
	i = 0
	print ("")

	if (len(argv) < 4):
		print_help()
		exit(1)

	print("argv[1] :%s" % argv[1])
	print("argv[2] :%s" % argv[2])
	print("argv[3] :%s" % argv[3])

	a = int(argv[2])
	b = int(argv[3])

	t = state_machine[argv[1]](a, b)

	print (t)

	return
	
if (__name__ == "__main__"):
	main(sys.argv)
