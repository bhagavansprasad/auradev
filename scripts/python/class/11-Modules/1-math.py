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

def is_odd(n):
    return (n%2)

def is_even(n):
    return (n%2)


n = 10
if (is_prime(n)):
    print n, "Prime"
else:
    print n, "NOT Prime"

if (is_even(n) == 0):
    print n, "EVEN"
else:
    print n, "ODD"

if (is_odd(n) != 0):
    print n, "EVEN"
else:
    print n, "ODD"



