class A:
    def f(self):
        print("A: function f")
        return self.g()

    def g(self):
        print("A: function g")
        return 'X'

class B(A):
	#g function ambigute function, because it is also available in base class
    def g(self):
        print("B: function g")
        return 'Y'

obj1 = A()
print(obj1.f())
print ("")

print(obj1.g())
print ("")

obj2 = B()
print(obj2.g())
print ("")

print(obj2.f())
print ("")
exit(1)
