import sys

class Error(Exception):
   pass

class MyException(Error):
   print "Raised when the input value is too small"
   pass

def factorial( n ):
   if n < 1:
      raise MyException("Invalid Input for factorial value!")
   temp = 1

   for i in range(1, n+1):
       temp *= i
    
   return temp

n = 5
try:
    factval = factorial(n)
except MyException as e:
    print "In Exception block: ", e.args
else:
   print "factorial value of '", n, "' is ", factval

    


