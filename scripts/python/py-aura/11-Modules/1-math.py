def is_prime(n):
    i = 2

    while (i < n):
        if (n % i == 0):
            return 0
        i += 1

    return 0

def main():
    n = 17
    if (is_prime(n) == 1):
        print("%d is %s" % (n, "Prime"))
    else:
        print("%d is %s" % (n, "NOT Prime"))

if (__name__ == "__main__"):
    main()

