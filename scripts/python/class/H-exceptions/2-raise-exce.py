import sys

def factorial( n ):
   a = 10
   if n < 1:
      print "value error"
      #raise ValueError("Invalid Input for for factorial value!", n)
      raise Exception('This is the exception you expect to handle')
      print "No statement"
   temp = 1

   for i in range(1, n+1):
       temp *= i

       #print a/0
   return temp

n = -5

try:
    factval = factorial(n)
except ValueError as e:
    print "In ValueError Exception: ", e.args
except Exception as error:
    print('In Common Exception caught this error: ' + repr(error))
else:
    print "In else part of exception factorial value of '", n, "' is ", factval
finally:
    print "In finally part of exception value of "
    

