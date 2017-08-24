a = 10

def get_data():
    global a
    print "a :", a
    return a

def set_data(n):
    global a
    print "a :", a
    a = n
    return a

def dump_data():
    global a
    print "a :", a

def increment_data(n):
    global a
    a = a + n
    print "a :", a

def fun1():
    t = get_data()
    print "data :", t
    set_data(10)

def fun2():
    print "data :", get_data()
    increment_data(100)
    print "data :", get_data()

def fun3():
    dump_data()

fun1()
fun2()
print "data :", get_data()
increment_data(10)
print "data :", get_data()
increment_data(20)
fun3()
print "data :", get_data()


