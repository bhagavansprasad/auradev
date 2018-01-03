from decorator07 import my_decorator


@my_decorator
def just_some_function():
    print("Wheee!")

print("2. Before calling just_some_function")
just_some_function()
