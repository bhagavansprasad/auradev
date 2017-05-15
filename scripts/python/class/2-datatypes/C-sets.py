my_set = {1, 2, 3, 8, 4}
print (type(my_set))
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = set([1,2,3,2])
print(my_set)

a = {}
print(type(a))

a = set()
print(type(a))

my_set = {1, 2, 3}
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([2,3,4])
print(my_set)

my_set.update([4,5], {1,6,8})
print(my_set)

print ""
my_set = {1, 3, 4, 5, 6}
print(my_set)

my_set.discard(3)
print(my_set)

my_set.remove(6)
print(my_set)

my_set.discard(2)
print(my_set)

#my_set.remove(2)
print(my_set)

print ""
my_set = set("HelloWorld")
print(my_set)

print(my_set.pop())

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)

print ""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print "A ", A
print "B ", B

print(A | B)
print A.union(B)
print B.union(A)

print(A & B)
print A.intersection(B)
print B.intersection(A)

print ""
print(A - B)
print A.difference(B)

print(B - A)
print B.difference(A)

print ""
print(A ^ B)
print A.symmetric_difference(B)

print(B ^ A)
print B.symmetric_difference(A)
print ""
