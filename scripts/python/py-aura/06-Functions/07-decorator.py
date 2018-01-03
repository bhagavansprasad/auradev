'''
def greet(name):
    return "hello "+name

greet_someone = greet
print greet_someone("Aura")
'''


'''
def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print greet("Aura")
'''

'''
def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "Aura"
    return func(other_name)  

print call_func(greet)
'''

'''
def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print greet()
'''

'''
def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message

greet = compose_greet_func("Aura")
print greet()
'''

def get_text(name):
    print "4. get_text function"
    return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
    print "1. p_decorate"
    
    def func_wrapper(name):
        print "2. func_wrapper"
        return "<p>{0}</p>".format(func(name))

    print "3. func_wrapper, before returning..."
    return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("Aura")
exit(1)
