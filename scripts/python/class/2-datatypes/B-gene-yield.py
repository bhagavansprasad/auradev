def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, number-1, 2):
            if number % current == 0: 
                return False
        return True
    return False

def get_primes(number):
	i = 1
	while(i < number):
		if is_prime(i):
			yield i
		i += 1

my_gen_primes = get_primes(30)
#for item in get_primes(30):
    #print item
for item in my_gen_primes:
    print item



