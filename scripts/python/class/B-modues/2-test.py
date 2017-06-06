import mymath
#from mymath import is_prime, is_even, is_odd
#from mymath import *

n = 5

if (mymath.is_prime(n)):
    print n, "Prime"
else:
    print n, "NOT Prime"

if (mymath.is_even(n) == 1):
    print n, "EVEN"
else:
    print n, "ODD"

if (mymath.is_odd(n) == 1):
    print n, "EVEN"
else:
    print n, "ODD"


