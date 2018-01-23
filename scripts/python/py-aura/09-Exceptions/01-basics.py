def common_default_error():
	a = [10, 20, 30]
	print ("")
	print(a[0])

	print(a[3])

	print ("Statement at end of function")

def common_error():
	a = [10, 20, 30]
	print ("")
	print(a[0])

	try:
		print(a[3])
	except:
		print ("I got exception")
		print ("Second statement in exception block")
	
	print ("Statement at end of function")

def index_error():
	a = [10, 20, 30]
	print ("")
	print(a[0])

	try:
		print(a[3])
	except IndexError:
		print ("I got exception")
		print ("Second statement in exception block")

	print ("Statement at end of function")

def index_error_strings():
	tstr = "Aura Networks"
	print ("")

	print(tstr[0])

	try:
		print(tstr[20])
		tstr[0] = 'a'

	except TypeError:
		print ("Strings are immutable...")
		return

	except IndexError:
		print ("Index error while reffering string")

	print ("Statement at end of function")

def index_error_with_args():
	tstr = "Aura Networks"
	print ("")
	try:
		tstr[0] = 'a'
		print(tstr[20])

	except (TypeError, IndexError) as errobj:
		print ("the error message is :", errobj)
		exit(1)

def main():
	#common_default_error()
	#common_error()
	#index_error()
	#index_error_strings()
	index_error_with_args()
	return()

if (__name__ == "__main__"):
	main()

