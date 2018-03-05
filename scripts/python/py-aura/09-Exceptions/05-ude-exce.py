import sys

class Error(Exception):
   pass

class MytestException(Error):
   print("Raised when the input value is less than 0")

def factorial( n ):
   if n < 0:
      raise MytestException("Invalid Input for factorial value!")
   temp = 1

   for i in range(1, n+1):
       temp *= i
    
   return temp

def main():
	n = -5
	factval = 0

	try:
		factval = factorial(n)
	except MytestException as e:
		print("In Exception block: ", e.args)
	else:
		print("factorial value of '", n, "' is ", factval)
 
if (__name__ == "__main__"):
	main()

