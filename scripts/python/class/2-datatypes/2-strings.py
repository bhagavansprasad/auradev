test_str = "Aura Networks Bangalore"

print test_str

for byte in test_str:
	print byte,

print ""
print len(test_str)

test_str = "Aura Networks Bangalore"

# String is immutable 
#print test_str[2]
#test_str[2] = 'm'

#this is possible
test_str = "new test string"

exit(1)
for byte in test_str:
	print byte,



i = 0
while (i < len(test_str)):
    print test_str[i], 
    i += 1

print ""

print test_str[0]
print test_str[1]
print test_str[-1]
print test_str[-2]
print test_str[1:6]
print test_str[1:23]
print test_str[1:30]
print test_str[::-1]

s1 = "Hello Aura Networks"
s2 = "Python Training"

print "string1 :", s1
print "string2 :", s2
print s1[0]
print s1[-1]
print s1[-2]
print s1[6:10]
print s1[11:30]+"11234"


test = "abcd"
print test[4:6]


name = "Saketh Ram"
age = 13
salary = 1000
height = 5.123

#print "name ", name, "age ", age, 
print "my friend %s age is %d and salary is %d height is %f" % (name, age, salary, height)
print name, age
print name * 3
#name[0] = 'x'

s = "Aurovill"
#s[0] = 'B' #error #immutable

s = "B" + s[:]
print s

s = "B" + s[2:]
print s

s = "B" + s[2:5]
print s


s = "B" + s[1:5]
print s


str = "this is string example. and temp...wow!!!";
print "str.capitalize() : ", str.capitalize()
print str

str =  str.capitalize()
print str
print ""

print dir(s)

print str
sub = "i";
print "str.len() :", len(str)
print "str.count(sub) : ", str.count(sub)
print "str.count(sub, 4) : ", str.count(sub, 4)
print "str.count(sub, 4, 10) : ", str.count(sub, 4, 10)
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)

sub = "wow";
print "str.count(sub) : ", str.count(sub)

sub = " ";
print "str.count(sub) : ", str.count(sub)

print ""
print str


i = 0
str = "this is string example....wow!!!";
print str
suffix = "wow!!!";
prefix = "This";

print "1. ", str.endswith(suffix)
print "2. ", str.endswith(suffix, 5, 7)
print "3. ", str.startswith(prefix)
print "4. ", str.capitalize()
print "5. ", str.capitalize().startswith(prefix)

print ""


str = "this is string example....wow!!!";
substr = "exam";
print "1. ", str.find(substr)
print "2. ", str.find(substr, 10)
print "3. ", str.find(substr, 20)
print "4. ", str.index(substr, 10)
print ""


str = "THIS is string example....wow!!!"; 
print str.islower()
print str.lower()
print str.lower().islower()

str = "this is string example....wow!!!";
print str.islower()
print str.upper()
print str.upper().capitalize()
print str.upper().capitalize().islower()
print str.upper().isupper()

print ""

str = "       "; 
print str.isspace()

str = "This is string example....wow!!!";
print str.isspace()


str = "This is string is example...is .wow!!!";
print ""
print str
print str.replace("is", "was")
print str

str = "This is string is example...is .wow!!!";
print str
print str.replace("is", "was", 1) #Number of occurences to replace
print str.replace("is", "was", 2) #Number of occurences to replace
print ""

#Number with tabs, single space and multiple spaces
phnum = "	      99020 96 75  0   	       "
phnum = "".join(phnum.split())
print phnum

str = "     this is string           example....wow!!!     ";
print str,
print "xxxx"
print str.rstrip()
print str.lstrip()
print "xxxx"
print str.strip(),

print ""

str = "88888888this is string example....wow!!!8888888888888888888888";
print str
print str.rstrip('8')
print (str.rstrip('8')).lstrip('8')
print (str.rstrip('8')).lstrip('8').lstrip("th")

str = "88888888this is string example....wow!!!8888888888abc888888888888";
#output should be str = "this is string example....wow!!!abc";
print str
substr = "abc"
print str.lstrip('8').rstrip('8').rstrip(substr).rstrip('8')+substr
print type(str.lstrip('8').rstrip('8').rstrip(substr).rstrip('8')+substr)


print ""
str = "Line1-ab cdef \nLine2-abc\nLine4-abcd";
print str

print str.split()
print type(str.split())
print str.split(' ', 1 )
print str.split(' ', 2 )


print ""
print ""
email = "bhagavansprasad@gmail.com"
print email
print email.split('@')

username = email.split('@')[0]
dname = email.split('@')[1]
print username
print dname

username,dname = email.split('@')
print username
print dname
exit(0)


print ""
str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print str.splitlines()
print str.splitlines(0)
print str.splitlines(1)
print str.splitlines(4)
print str.splitlines(5)

str = "Line1-ab cdef     Line2-abc Line4-abcd";
print str
print str.split(' ')
print str.split()
print len(str.split(' '))

exit(1);
