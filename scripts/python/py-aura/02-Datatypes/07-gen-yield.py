def test_fun1():
    #....
    #a = ?
    #....
    #....
    #b = ?
    #....
    #c = ?

    return (5, 10, 20)

def test_fun2():

    #....
    # return (5)
    yield 5

    #....

    # return (10)
    yield 10

    #....

    # return (20)
    yield 20
    print ("")


def gen_yield_basic():
    #....
    yield 15

    #....
    yield "temp"

    #....
    yield 'a'

def createGenerator():
    mylist = list(range(5))
    print("mylist type :", type(mylist))
    print(mylist)

    for i in mylist:
        yield i*i

def fib(n):
    pre, cur, nxt, i = -1, 1, 0, 1

    while (i <= n): 
        prev = cur
        cur =  nxt
        nxt = prev + cur
        yield cur
        i = i + 1

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

def get_primes_without_yield(input_list):
    result_list = list()

    for element in input_list:
        if (is_prime(element)):
            result_list.append(element)

    return result_list

def get_primes_with_yield(input_list):
    for element in input_list:
        if is_prime(element):
            yield element

def main():
    (a, b, c) = test_fun1()
    print("a :%d, b :%d, c :%d" % (a, b, c))

    (a, b, c) = test_fun2()
    print("a :%d, b :%d, c :%d" % (a, b, c))

    (a, b, c) = gen_yield_basic()
    print("a :%d, b :%s, c :%c" % (a, b, c))

    tlist = list(gen_yield_basic())
    print (tlist)

    gen_obj = gen_yield_basic()
    print (type(gen_obj))

    for item in gen_yield_basic():
        print(item)

    mygenerator = createGenerator()
    print(type(mygenerator))
    for i in mygenerator:
        print(i)

    flist = list(fib(10))
    print(flist)

    num_list = [2, 5, 7, 8, 11, 15, 23, 29]
    print (num_list)
    result = get_primes_without_yield(num_list)
    print(result)
    print("type of result ", type(result))

    result = get_primes_with_yield(num_list)
    print(list(result))

    return

if (__name__ == '__main__'):
    main()
