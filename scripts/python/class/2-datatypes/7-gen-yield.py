
'''
def myfun():
    return 5

my_list= [10,20,30]

for item in my_list:
    print item

'''

def myfun():
    yield 15
    yield "temp"
    yield 'a'
for item in myfun():
    print item



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
