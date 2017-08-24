def is_prime(n):
    i = 2

    for i in range(2, n):
        if (n % i == 0):
            return 0

    return 1


n = 29
t = is_prime(n)
print "t :", t
if (t ==  1):
    print "Number ", n, "is a PRIME"
else:
    print "Number ", n, "is a NOT PRIME"

