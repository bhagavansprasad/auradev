def test_fun1(my_function):
    print("-->I am in test_fun1!")

    def inner_fun1():
        print("-->I am in inner_fun1!, before calling my_function")
        my_function()
        print("-->I am in inner_fun1!, After  calling my_function")

    return inner_fun1


def test_fun2():
    print("-->I am in test_fun2!")


just_some_function = test_fun1(test_fun2)
just_some_function()
