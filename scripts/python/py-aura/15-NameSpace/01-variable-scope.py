#!/usr/bin/python
'''
def outer_function():
	b = 20
	print("outer_function a :%d" % a)
	print("outer_function b :%d" % b)
	print("")
	def inner_func():
		c = 30
		print("inner_func a :%d" % a)
		print("inner_func b :%d" % b)
		print("cinner_fun c :%d" % c)
		print ("")
	inner_func()
	#print("outer_function c :%d" % c)

a = 10
outer_function()
print("global a :%d" % a)
print ("")
#print("global b :%d" % b)
#print("global c :%d" % c)

'''

'''
def outer_function():
	a = 20
	b = 20
	print("outer_function a :%d" % a)
	print("outer_function b :%d" % b)
	print ("")
	def inner_function():
		a = 30
		c = 30
		print("inner_func a :%d" % a)
		print("inner_func b :%d" % b)
		print("inner_func c :%d" % c)
		print ("")

	inner_function()
	print("outer_function a :%d" % a)
	print ("")
     
a = 10
outer_function()
print("global a :%d" % a)
'''

'''
def outer_function():
	global a
	a = 20
	def inner_function():
		global a
		a = 30
		print("inner_func a :%d" % a)

	inner_function()
	print("outer_func a :%d" % a)
     
a = 10
outer_function()
print ("global a : %d" % a)
'''

'''
def outer_function():
	a = 20
	print("outer_func a :%d" % a)

	def inner_function():
		nonlocal a
		a = 30
		print("inner_func a :%d" % a)

	inner_function()
	print("outer_func a :%d" % a)

a = 10
outer_function()
print('global a is :%d' % a)
'''
