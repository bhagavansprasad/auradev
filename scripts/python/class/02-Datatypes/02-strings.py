test_str = "Aura Networks Bangalore"
print (test_str)

print "String value is :", test_str
print ("String value is :%s" % (test_str))
print ("String %s value is :" % (test_str))
print ("%s String value is :" % (test_str))

print(len(test_str))
print("Length of test_str is :%d" % (len(test_str)))

print(test_str[1])
print("First  byte :%c" % (test_str[0]))
print("Second byte :%c" % (test_str[1]))

i = 0
while (i < len(test_str)):
    print(test_str[i]),
    i += 1

print("")

for temp in test_str:
	print(temp),

print("")

test_str = "Aura Networks Bangalore"
print(test_str[2])

#test_str[2] = 'm'
print(test_str[2])
print(test_str)

#this is possible
test_str = "new test string"
print(test_str)

test_str = "Aura Networks Bangalore"
print("     :%s" % test_str)
print(" 0   :%c" % test_str[0])
print(" 1   :%c" % test_str[1])
print("-1   :%c" % test_str[-1])
print("-2   :%c" % test_str[-2])
print(" 1:6 :%s" % test_str[1:6])
print(" 1:23:%s" % test_str[1:23])
print(" 1:30:%s" % test_str[1:30])
print(" 0:30:%s" % test_str[0:30])
print(" ':' :%s" % test_str[:])
print("5:   :%s" % test_str[5:])
print("':-1':%s" % test_str[:-1])
print("-2:  :%s" % test_str[-2:])
print(test_str[::-1])
print(test_str[::])
print(test_str[13:-1])
print(test_str[:13:-1])
print(test_str[5::1])
print(test_str[5::2])
print(test_str[5::3])

name = "Saketh Ram"
age = 14
salary = 1000
height = 5.123

print "my friend", name, "age is", age, "and salary is", salary, "height is", height
print("my friend %s age is %d and salary is %d height is %f" % (name, age, salary, height))

print(name, age)
print(age * 3)
print(height * 3)
print(name * 3)
print(str(height) * 3)

s = "Aurovill"
s = "B" + s[:]
print(s)

s = "Aurovill"
s = "B" + s[2:]
print(s)

s = "Aurovill"
s = "B" + s[2:5]
print(s)

s = "Aurovill"
s = "B" + s[1:5]

tstr = "this is string example. and ..wow!!!";
print("tstr              : %s" % tstr)
print("tstr.capitalize() : %s" % tstr.capitalize())
print("tstr              : %s" % tstr)

tstr =  tstr.capitalize()
print("tstr              : %s" % tstr)
print("")

print(dir(tstr))
print(dir(""))
#print (help(tstr.capitalize))

a = 10
print(dir(a))

tstr = "this is string example. and temp...wow!!!";
print("tstr                   :%s" % tstr)
sub = "i";

print("tstr.len()             :%d" % len(tstr))
print("tstr.count(sub)        :%d" % tstr.count(sub))
print("tstr.count(sub, 4)     :%d" % tstr.count(sub, 4))
print("tstr.count(sub, 4, 10) :%d" % tstr.count(sub, 4, 10))
print("tstr.count(sub, 4, 40) :%d" % tstr.count(sub, 4, 40))

print("")

sub = "wow";
print("tstr.count(sub)        :%d" % tstr.count(sub))

sub = " ";
print("tstr.count(sub)        :%d" % tstr.count(sub))

sub = "aura";
print("tstr.count(sub)        :%d" % tstr.count(sub))

i = 0
tstr = "this is string example....wow!!!";
print("tstr                   :%s" % tstr)
suffix = "wow!!!";
prefix = "This";

print("1. :%r" % tstr.endswith(suffix))
print("2. :%r" % tstr.endswith(suffix, 5, 10))
print("3. :%r" % tstr.startswith(prefix))
print("4. :%s" % tstr.capitalize())
print("5. :%r" % tstr.capitalize().startswith(prefix))

print("")

tstr = "this is string example....wow!!!";
substr = "exam";
print("1. :%d" % tstr.find(substr))
print("2. :%d" % tstr.find(substr, 10))
print("3. :%d" % tstr.find(substr, 20))
print("4. :%d" % tstr.find("Exam"))

print("5. :%r" % tstr.index(substr))
print("6. :%r" % tstr.index(substr, 10))
#print("7. :%r" % tstr.index(substr, 20))
print("")

tstr = "THIS is string example....wow!!!"; 
print("1. :%r" % tstr.islower())
print("2. :%s" % tstr.lower())
print("3. :%r" % tstr.lower().islower())

print("")
tstr = "this is string example....wow!!!"; 
print("1. :%r" % tstr.isupper())
print("2. :%s" % tstr.upper())
print("3. :%s" % tstr.upper().capitalize())
print("4. :%r" % tstr.upper().capitalize().islower())
print("5. :%r" % tstr.upper().isupper())

print("")

tstr = "       "; 
print(tstr.isspace())

tstr = "This is string example....wow!!!";
print(tstr.isspace())

tstr = "This is string is example...is .wow!!!";
print("")
print(tstr)
print(tstr.replace("is", "was"))
print(tstr)

print("")
tstr = "This is string is example...is .wow!!!";
print("1. :%s" % tstr)
print("2. :%s" % tstr.replace("is", "was", 1))  #Number of occurences to replace
print("3. :%s" % tstr.replace("is", "was", 2))  #Number of occurences to replace
print("4. :%s" % tstr.replace("is", "was", -1)) #Number of occurences to replace
print("5. :%s" % tstr[5:].replace("is", "was")) #Number of occurences to replace
print("")

tstr = "          this is string           example....wow!!!     ";
print("1. %s" % tstr)
print("1. %d" % len(tstr))

print("2. %s" % tstr.rstrip())
print("2. %d" % len(tstr.rstrip()))

print("3. %s" % tstr.lstrip())
print("3. %d" % len(tstr.lstrip()))

print("4. %s" % tstr.strip())
print("4. %d" % len(tstr.strip()))

print("")

tstr = "88888888this is string example....wow!!!8888888888888888888888";
print(tstr)
print(tstr.rstrip('8'))
print(tstr.rstrip('8').lstrip('8'))
print(tstr.rstrip('8').lstrip('8').lstrip("th"))
print(tstr.strip('8'))

tstr = "88888888this is string example....wow!!!8888888888abc888888888888";
#output should be tstr = "this is string example....wow!!!abc";
print(tstr)
substr = "abc"
print(tstr.lstrip('8').rstrip('8').rstrip(substr).rstrip('8')+substr)
print(tstr.strip('8'))
exit(1)

#Number with tabs, single space and multiple spaces
phnum = "	      970 2096 756   	       "
print(phnum)
print(phnum.split())
print(phnum.split()[1])
phnum = "".join(phnum.split())
print(phnum)

print("")
tstr = "Line1-ab cdef \nLine2-abc\nLine,4-abcd";
print(tstr)
print(tstr.split())
print(tstr.split(' ', 1))
print(tstr.split(' ', 2))

print("")
email = "bhagavanprasad@gmail.com"
print(email)
print(email.split('@'))

username = email.split('@')[0]
dname = email.split('@')[1]
print(username)
print(dname)

username,dname = email.split('@')
print(username)
print(dname)
exit(1)

