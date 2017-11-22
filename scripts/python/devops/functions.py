def add(a, b=10, c=None):
	if type(a) == str:
		return a + str(b)
	
	if c is None:
		return a + b
	else:
		return a + b + c
	

#print add(3, 4)
#print add("dd", 55)
#print add(3,c=4)
#print add(a=2, b=3,c=4)

def add2(*args):
	t=0
	for i in args:
		t =  t + i
	print t

#add2(1,2,3,4,5,6)

def add3(*args, **kargs):
	print args
	print kargs
	if True:
		if True:
			if True:
				a = [3,4]
	return [0, "ss"]

(returnval, output) =  add3(1,2,3,4, a=7, b=8)
a = 5
b = 7
c =100
d = []
(a, b, d) = (b, a, c)




