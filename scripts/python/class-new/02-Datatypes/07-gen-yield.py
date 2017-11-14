def myfun():
    #....
    yield 15

    #....
    yield "temp"

    #....
    yield 'a'

def createGenerator():
    mylist = range(5)
    print "mylist type :", type(mylist)
    print mylist
    for i in mylist:
        yield i*i


(a, b, c) = myfun()
print "a :%d, b :%s, c :%c" % (a, b, c)

for item in myfun():
    print item

mygenerator = createGenerator()
print type(mygenerator)

for i in mygenerator:
     print(i)
