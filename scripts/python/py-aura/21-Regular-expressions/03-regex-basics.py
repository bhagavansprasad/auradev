import re

'''
metacharacters
    . ^ $ * + ? { } [ ] \ | ( )

re.match()
re.search()
re.findall()
re.split()
re.sub()
re.compile()
'''

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "Aura Networks June 24")
if match:
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group(0)))
    print("Month     : %s" % (match.group(1)))
    print("Day       : %s" % (match.group(2)))
else:
    print("The regex pattern does not match. :(")
print("")

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "Aura Networks June 24 Bangalore 30")
if match:
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group(0)))
    print("Month     : %s" % (match.group(1)))
    print("Day       : %s" % (match.group(2)))
else:
    print("The regex pattern does not match. :(")
print("")


print ("==========")
regex = r"([a-zA-Z]+) (\d+)"
s1 = "June 24, August 9, Dec-12"
print("1. search -- '%s' -- '%s' " % (regex, s1))
match = re.search(regex, s1)
if match:
    print ("match ", match)
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match: %s" % (match.group(0)))
    print("Month     : %s" % (match.group(1)))
    print("Day       : %s" % (match.group(2)))
else:
    print("The regex pattern does not match. :(")
print("")

regex = r"[a-zA-Z]+ \d+"
s1 = "June 24, August 9, Dec-12"
print("findall -- '%s' -- '%s' " % (regex, s1))
matches = re.findall(regex, s1)
for match in matches:
    print("Full match: %s" % (match))
print("")


regex = r"([a-zA-Z]+ \d+)"
s1 = "June 24, August 9, Dec-12"
print("findall -- '%s' -- '%s' " % (regex, s1))
matches = re.findall(regex, s1)
for match in matches:
    print("Match month: %s" % (match))

print("")

regex = r"([a-zA-Z]+) (\d+)"
s1 = "June 24, August 9, Dec-12"
print("findall -- '%s' -- '%s' " % (regex, s1))
matches = re.findall(regex, s1)
for match in matches:
    print("Match month :",  (match))

print("")


regex = r"([a-zA-Z]+) \d+"
s1 = "June 24, August 9, Dec 12"
print("finditer -- '%s' -- '%s' " % (regex, s1))
matches = re.finditer(regex, s1)
for match in matches:
    print("Match at index: %s, %s" % (match.start(), match.end()))
exit(1)
