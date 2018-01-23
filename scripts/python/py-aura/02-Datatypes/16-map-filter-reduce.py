from operator import add
from functools import reduce

def import_modules_dynamically():
	moduleNames = ['sys', 'os', 're', 'unittest']
	print(moduleNames)
	modules = map(__import__, moduleNames) 

	i = 0
	while (i < len(moduleNames)):
		print (modules[i])
		i = i + 1
		
	return


def is_prime(num):
	i = 2
	flag = 1

	while (i < num):
		if (num % i == 0):
			flag = 0
			break
		i += 1

	if (flag ==  1):
		return num
	else:
		return 0

def list_all_primes(items):
	#Normal way of finding primes from a list
	print("Basic  :", end=' ')
	for i in items:
		if (is_prime(i)):
			print(i, end=' ')
			#print("")

	print ("")
	
def list_all_primes_with_map(items):
	#Using 'map' of finding primes from a list
	primes = list([(is_prime(x)) for x in items])
	print("map    :", primes)

def list_all_primes_with_filter(items):
	#Using 'filter' of finding primes from a list
	primes = list([x for x in items if (is_prime(x) == x)])
	print("filter :", primes)

def use_of_map():
	#other way of using map
	funcs = [multiply, add]
	for i in range(5):
		value = list([x(i) for x in funcs])
		print(value)

def use_of_reduce():
	product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
	print (product)

	lfun = lambda a, b: a if (a > b) else b
	print(reduce(lfun, [47, 11, 42, 102, 13]))


def multiply(x):
	return (x*x)

def add(x):
	return (x+x)



def main():
	items = [3, 10, 15, 19, 7, 23, 25, 29]
	list_all_primes(items)

	list_all_primes_with_map(items)

	list_all_primes_with_filter(items)

	use_of_map()

	use_of_reduce()
	return

	import_modules_dynamically()

	exit(1)

if __name__ == '__main__':
	main()

