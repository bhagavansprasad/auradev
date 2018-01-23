a = 5
b = 10
c = 12

'''
f = 1
for i in range (1, a+1):
	f = f * i
print ("a :%d, factorial value :%d" % (a, f))

f = 1
for i in range (1, b+1):
	f = f * i
print ("a :%d, factorial value :%d" % (b, f))

f = 1
for i in range (1, c+1):
	f = f * i
print ("a :%d, factorial value :%d" % (c, f))
'''

def factorial(n):
	f = 1
	for i in range (1, n+1):
		f = f * i
	return f



temp = factorial(a)
print ("a :%d, factorial value :%d" % (a, temp))

temp = factorial(b)
print ("b :%d, factorial value :%d" % (b, temp))

temp = factorial(c)
print ("c :%d, factorial value :%d" % (c, temp))
