from operator import add

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

def multiply(x):
    return (x*x)

def add(x):
    return (x+x)



def main():
    items = [3, 10, 15, 19, 7, 23, 25, 29]

    #Normal way of finding primes from a list
    for i in items:
        if (is_prime(i)):
            print (i),

    print ("")

    #Using 'map' of finding primes from a list
    primes = list(map(lambda x: (is_prime(x)), items))
    print ("map    :", primes)

    #Using 'filter' of finding primes from a list
    primes = list(filter(lambda x: (is_prime(x) == x), items))
    print ("filter :", primes)

    #other way of using map
    funcs = [multiply, add]
    for i in range(5):
        value = list(map(lambda x: x(i), funcs))
        print(value)
   
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print (product)

    lfun = lambda a, b: a if (a > b) else b
    print (reduce(lfun, [47, 11, 42, 102, 13]))

    exit(1)
if __name__ == '__main__':
    main()
