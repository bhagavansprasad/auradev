def p_dec(fun):
    def wrapper_func(name):
        return "<p>%s</p>" % fun(name)
    return wrapper_func

@p_dec
def get_text(name):
    return "hello %s" % name


w_f = p_dec(get_text)
print w_f("Yogesh")
print get_text("Meghana")

# with class
class mydeco():
    def __init__(self, f):
        self.f = f 
        self.s = "hi"

    def __call__(self, name):
        print "start"
        self.f(name)
        print "end", self.s

@mydeco
def mytest(name):
    print "mytest", name

mytest("yogi")

print "demo of class with args"
# with class and args
class mydeco_args():
    def __init__(self, arg1):
        self.arg1 = arg1
        print arg1

    def __call__(self, f):
        def warp(name):
            print "start"
            f(name)
            print "end", self.arg1
        return warp    

@mydeco_args("chandana")
def mytest2(name):
    print "mytest", name

mytest2("sss")

