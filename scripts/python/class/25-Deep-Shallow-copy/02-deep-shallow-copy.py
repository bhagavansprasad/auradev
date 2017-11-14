a = 2
print(('id(2) =', id(2)))
print(('id(a) =', id(a)))
print("")

a = a + 1
print(('id(2) =', id(2)))
print(('id(a) =', id(a)))
print(('id(3) =', id(3)))
print("")

b = 2
print(('id(2) =', id(2)))
print(('id(b) =', id(b)))
print("")

b = b + 1
print(('id(3) =', id(3)))
print(('id(a) =', id(a)))
print(('id(b) =', id(b)))
exit(1)

