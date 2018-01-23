class A:
    def f(self):
        print("A: function f")
        return self.g()

    def g(self):
        print("A: function g")
        return 'A'

class B(A):
    def g(self):
        print("B: function g")
        return 'B'

a = A()
b = B()
print(a.f())
print ("")

print(a.g())
print ("")

print(b.f())
print ("")

print(b.g())
