def is_even(n):
	if (n%2 == 0):
		return True
	else:
		return False

def main():
	try:
		assert(is_even(15) == True)
	except AssertionError:
		print ("is_even returned False")
	else:
		print ("is_even returned True")

if __name__ == '__main__':
	#assert(is_even(15) == True)
	main()
