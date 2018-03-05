
''' 
def is_prime(num):
    i = 2
    flag = 1
    while (i < num):
        if (num % i == 0):
            flag = 0
            break
        i += 1

    if (flag ==  1):
        return 1
    else:
        return 0
''' 

''' 
#0 incase of NOT PRIME, 1 otherwise
def is_prime(num):
    i = 2
    flag = 0
    while (i < num):
        if (num % i == 0):
            flag += 1
        i += 1

    if (flag > 0):
        return 0
    else:
        return 1
''' 

def is_prime(n):
    i = 2
	#print ("")

    for i in range(2, n):
		#print ("")
        if (n % i == 0):
			#print ("")
            return 0
		#print ("")

	#print ("")
    return 1

m = 25
t = is_prime(m)
if t ==  1:
    print "Number ", m, "is a PRIME"
else:
    print "Number ", m, "is a NOT PRIME"

m = 12
n = 25
o = 17
t = is_prime(n)
if (t ==  1):
    print "Number ", n, "is a PRIME"
else:
    print "Number ", n, "is a NOT PRIME"

t = is_prime(o)
if (t ==  1):
    print "Number ", o, "is a PRIME"
else:
    print "Number ", o, "is a NOT PRIME"

exit(1)
