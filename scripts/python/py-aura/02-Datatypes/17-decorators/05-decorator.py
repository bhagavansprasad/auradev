def my_decorator(some_function):
	print ("In my_decorator function")

	def wrapper():

		print("Something is happening before some_function() is called.")

		some_function()

		print("Something is happening after some_function() is called.")

	print ("Returning from my_decorator function")
	return wrapper


def just_some_function():
	print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()
