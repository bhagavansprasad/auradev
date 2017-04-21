''' 
# or better yet...

def get_primes(input_list):
    return (element for element in input_list if is_prime(element))
''' 

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

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append(element)

    return result_list

num_list = [2, 5, 7, 8, 11, 15, 23, 29]

result = get_primes(num_list)
print result


