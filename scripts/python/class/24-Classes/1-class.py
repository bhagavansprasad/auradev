class MyClass:
    name = "aura"

    def __init__(self):
        name = ""
        print "In constructure function"

    def print_msg(self):
        print("This is a message inside the class.")

    def store_data(self, data):
        self.name = data

    def get_data(self):
        return self.name

obj1 = MyClass()
obj2 = MyClass()

print obj1.name
obj1.print_msg()

obj1.store_data("Saketh")
print obj1.get_data()

obj2.store_data("Bhagavan")
print obj2.get_data()

