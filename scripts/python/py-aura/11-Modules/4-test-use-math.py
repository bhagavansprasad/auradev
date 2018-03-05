#import amath
#from amath import *

from amath import is_prime
#from amath import is_prime as IS_PRIME

n = 5

#if (IS_PRIME(n)):
if (is_prime(n)):
    print("%d is %s " % (n, "Prime"))
else:
    print("%d is %s " % (n, "NOT Prime"))

