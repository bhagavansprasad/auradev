class Person():
	name = None
	age = None
	def __init__(self, n, a, sex="Male"):
		self.name = n
		self.age = a
		self.sex = sex
	
	def __str__(self):
		return self.name

	def desc(self):
		print "This person name is " + self.name
		print "This person age is " + str(self.age)

p = Person('Yogesh', 30)
p2 = Person('Sam', 55)
#p.name = 'Yogesh'
#p.age = 30

print p

print p.name
print p.age

p2.name = 'Sam'
p2.age = 35

print p2.name
print p2.age


p.desc()
p2.desc()
#print p

ppl = [Person("a",3), Person("b",4)]
print ppl[0].name