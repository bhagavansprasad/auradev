import re

print "Get the first digit:"
p = re.compile('\d+')
result = p.match("1sdfdsg")
print result.group()

result = p.match("22sdfdsg")
print result.group()
result = p.match("55sdfdsg")
print result.group()

# returns "None" on no-match
result = p.match("sdfdsg")
if result:
    print result.group()

print "match in between:"
p = re.compile('\d+')
result = p.search("sd4444fdsg")
print result.group()
print result.start()
print result.end()

print "match a-z first occurance:"
p = re.compile('[a-z]+')
result = p.search("999 sd4444fdsg")
print result.group()

print "match a-z all occurance:"
p = re.compile('[a-z]+')
for result in p.finditer("999 sd4444fdsg"):
    print result.group()

print "match word:"
p = re.compile(r'\bclass\b', re.I)
result = p.search("999 Class 4444fdsg")
print result.group()


print "use pattern with match:"
result = re.search(r'\bclass\b', "999 class 4444fdsg")
print result.group()

print "search at the end:"
result = re.search(r'\d+$', "999 class 4444fdsg555")
print result.group()

print "Search for diffrent strings:"
result = re.search(r'am.*here', "I am Yogesh here")
print result.group()
for result in p.finditer("I am Yogesh here"):
    print result.group()

print "Search for special char:"
# \, ., *, $, ^, | [] {}
result = re.search('\\\\', "\\ ss")
print result.group()

print "match occurance:"
# \, ., *, $, ^, | [] {}
result = re.search('\d{3}', "3454326")
print result.group()

print "Search for ip:"
result = re.search(r'\d+\.\d+.[1-4][5-9][1-9]\.\d+', " sdgfsd  192.168.267.253  sdgsd")
print result.group()

print "Use findall:"
result = re.findall('.*?(\d{3})', "sss3454326 ddd234 fff235 dfg")
print result

print "search and replace:"
p = re.compile(r'\bclass\b', re.I)
result = p.sub('school', "999 class 4444fdsg555")
print result
