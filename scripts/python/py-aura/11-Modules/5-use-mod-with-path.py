import sys
sys.path.append('/home/bhagavan/training/scripts/python/py-aura/11-Modules/mod-lib')
import fact
import amath


n = 5
t = fact.factorial(5)
print(("Factorial value of %d is %d" % (n, t))) 

print("sys.path :", sys.path)
print(dir(amath))

