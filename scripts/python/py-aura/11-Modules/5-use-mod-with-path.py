import sys
sys.path.append('/home/bhagavan/training/scripts/python/py-aura/11-Modules/mod-lib')
import amath

n = 5

if (amath.is_prime(n)):
    print("%d is %s " % (n, "Prime"))
else:
    print("%d is %s " % (n, "NOT Prime"))

print("sys.path :", sys.path)
print(dir(amath))

