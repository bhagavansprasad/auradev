def myfun():
    #....
    yield 15

    #....
    yield "temp"

    #....
    yield 'a'

(a, b, c) =  myfun()
print a, b, c

for item in myfun():
    print item

print item
'''
'''



'''
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()
print type(mygenerator)

for i in mygenerator:
     print(i)
'''
