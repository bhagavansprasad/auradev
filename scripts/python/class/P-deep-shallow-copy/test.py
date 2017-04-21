a = [10,20,30, 40]

print "a     :", a
print "id(a) :", id(a)

b = a

print "b     :", b
print "id(b) :", id(b)

a[2] = 100
print "a     :", a
print "id(a) :", id(a)

print "b     :", b
print "id(b) :", id(b)
