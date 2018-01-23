def is_prime(n):
    i = 2

    while (i < n):
        if (n % i == 0):
            break
        i += 1

    if (i == n):
        return 1
    else:
        return 0

def main():
	n = 29
	if (is_prime(n) == 1):
		print(("%d is %s" % (n, "Prime")))
	else:
		print(("%d is %s" % (n, "NOT Prime")))

if (__name__ == "__main__"):
	main()



