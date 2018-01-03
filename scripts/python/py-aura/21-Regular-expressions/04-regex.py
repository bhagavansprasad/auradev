import re
result = re.search("cat", "A cat and a rat can't be friends.")
print(result.group())
print(result.start())
print(result.end())


if re.search("cow", "A cat and a rat can't be friends."):
    print("Found")
else:
    print("Not Found")

print("*" * 5)

regex = r"[cr]at"
result = re.search(regex, "A cat and a rat can't be friends.")
print("start :%d, end :%d" % (result.start(), result.end()))
print(result.group())

print("*" * 5)

regex = ".at"
result = re.search(regex, "A abcd cat and a rat can't be friends at.")
print("start :%d, end :%d" % (result.start(), result.end()))
print("group :", result.group())

print("*" * 5)

regex = r".at"
result = re.findall(regex, "A cat and a rat can't be tempmat friends.")
print(result)
exit(1)

