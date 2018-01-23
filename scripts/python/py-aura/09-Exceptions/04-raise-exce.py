def factorial( n ):
   a = 10
   temp = 1

   if (n < 0):
      raise ValueError("Invalid Input for factorial function!", n)
      #raise Exception('Invalid Input for xxxxxxxxxxxx factorial value!')
      print ("")

   for i in range(1, n+1):
       temp *= i

       #print a/0
   return temp


def main():
	n = -5
	factval = 0

	try:
		factval = factorial(n)

	except ValueError as e:
		print("In ValueError Exception: ", e.args)

	except Exception as error:
		print(('In Common Exception caught this error: ', error.args))

	else:
		print("In else part of exception factorial value of %d is %d '" % ( n, factval))

	finally:
		print("In finally part of exception factorial value of '", n, "' is ", factval)
    

if (__name__ == "__main__"):
	main()
