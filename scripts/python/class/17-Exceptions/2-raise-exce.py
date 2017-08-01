import sys

def factorial( n ):
   a = 10
   temp = 1

   if n < 0:
      print "value error"
      raise ValueError("Invalid Input for factorial value!", n)
      #raise Exception('Invalid Input for factorial value!')
      print "No statement"

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
    

