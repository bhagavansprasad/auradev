def foo(bar):
    return bar + 1

print("1. %s" % foo)
print("2. %d" % foo(2))
print("3. %s" % type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

print("4. %d" % call_foo_with_arg(foo, 3))
