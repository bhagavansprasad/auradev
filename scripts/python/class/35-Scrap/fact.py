m = 7
n = 5
o = 8
f = 1

'''
for i in range(1, m+1):
    f = f * i

print ("Factorial value of m:", f)

f = 1
for i in range(1, n+1):
    f = f * i
print ("Factorial value of m:", f)

f = 1
for i in range(1, o+1):
    f = f * i
print ("Factorial value of m:", f)
'''

def my_factrorial(a):
	f = 1
	i = 1
	for i in range(1, a+1):
		f = f * i
	#print ("Factorial value :", f)
	return f

#n is prime     return 1
#n is not prime return 0
def is_prime(n):
'''
 ...
 ...
 ...
 ...
'''


temp  = my_factrorial(m)
print ("Factorial value :", temp)

temp = my_factrorial(n)
print ("Factorial value :", temp)

temp = my_factrorial(o)
print ("Factorial value :", temp)


temp = is_prime(11)
if (temp == 1)
	print ("Prime")
else:
	print ("Not Prime")




'''
'''

'''
f = 1
for i in range(1, m+1):
    f = f * i
print ("Factorial value of :'%d' is :'%d'" % (m, f))

f = 1
for i in range(1, o+1):
    f = f * i
print ("Factorial value of :'%d' is :'%d'" % (o, f))
'''




'''
def find_factorial_value(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    print f

a = 7
b = 5
find_factorial_value(a)
find_factorial_value(b)
find_factorial_value(10)
'''


'''
def find_factorial_value(n):
    f = 1
    for i in range(1, n+1):
        f = f * i

    return f

a = 7
b = 5
x = find_factorial_value(a)
print x

y = find_factorial_value(b)
print ("Factorial value of :'%d' is :'%d'" % (b, y))

z = find_factorial_value(10)
print ("Factorial value of :'%d' is :'%d'" % (10, z))
'''
