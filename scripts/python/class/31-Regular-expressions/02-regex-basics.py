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
match = re.search(regex, "June 24")
if match:
    print "Match at index %s, %s" % (match.start(), match.end())
    print "Full match: %s" % (match.group(0))
    print "Month     : %s" % (match.group(1))
    print "Day       : %s" % (match.group(2))
else:
    print "The regex pattern does not match. :("


print ""

regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec-12")
for match in matches:
    print "Full match: %s" % (match)

print ""

regex = r"([a-zA-Z]+ \d+)"
matches = re.findall(regex, "June 24, August 9, Dec12")
for match in matches:
    print "Match month: %s" % (match)

print ""

regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    print "Match at index: %s, %s" % (match.start(), match.end())
exit(1)
