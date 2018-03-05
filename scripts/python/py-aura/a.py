def is_prime(number):
	if (number < 0):
		return False

	for i in range(2, number):
		if (number % i == 0):
			return False

	return True

n = 10
x = 2
c = 1

while (c <= n):
	t = is_prime(x)
	if (t == True):
		print("%d. prime number :%d" % (c, x))
		c = c + 1
	x = x + 1
