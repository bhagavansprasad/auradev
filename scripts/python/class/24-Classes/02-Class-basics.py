class MyClass:
    name = "xxxxxx"
    x = 0
    y = 0

    def __init__(self):
        self.name = ""
        self.x = 1
        self.y = 1
        print "1. In constructure function"

    def print_data(self):
        print("2. This is a message inside the class.")
        print self.name

    def store_data(self, data):
        self.name = data

    def get_data(self):
        return self.name

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print "3. ", obj1.name

obj1.store_data("Saketh")
print "4. ", obj1.get_data()
print "5. ", obj1.name

print "6. ", obj2.get_data()
print "7. ", obj2.name

obj2.store_data("Bhagavan")
print "8. ", obj2.get_data()
print "9. ", obj2.name
print "10. ", obj1.name
print "11. ", obj2.name
print "12. ", obj3.name

