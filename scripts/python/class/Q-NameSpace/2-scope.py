'''
def outer_function():
    b = 20
    def inner_func():
        c = 30

a = 10

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
outer_function()
print('a =',a)

'''

def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
outer_function()
print('a =',a)
