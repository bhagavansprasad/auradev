str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print("-" * 10)
print("str :", str)
print("-" * 10)
print("empty :", str.splitlines())
print("0 ", str.splitlines(0))
print("1 ", str.splitlines(1))
print("4 ", str.splitlines(4))
print("5 ", str.splitlines(5))
str = "Line1-ab cdef     Line2-abc Line4-abcd";
print("-" * 10)
print("str :", str)
print("single space :", str.split(' '))

exit(1)
name = ["aura Networks"]
print(name)
print(type(name))
name[0] = name[0].upper()
print(name)
