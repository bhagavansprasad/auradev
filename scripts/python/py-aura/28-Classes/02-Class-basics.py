class MyClass:
	name = "abcdexxx"
	x = -1 
	y = 0

	def __init__(self):
		print("In constructure function")
		self.name = None
		self.x = -1
		self.y = 0 

	def __del__(self):
		print("In destructure function")
		self.name = None
		self.x = -1
		self.y = 0 

	def my_constructer(self, data, a, b):
		print("In set_data function in class")
		self.name = data
		self.x = a
		self.y = b

	def dump_data(self):
		print("In dump_data function in class")
		print (name)

	def set_data(self, data):
		print("In set_data function in class")
		self.name = data

	def get_data(self):
		print("In get_data function in class")
		return (self.name, self.x, self.y)

	def increment_data(self, n):
		self.x = self.x + n
		return self.x 

def main():
	obj1 = MyClass()
	print("%s %d %d" % obj1.get_data())
	return

	obj1.my_constructer("", -1, 0)
	print("%s %d %d" % obj1.get_data())

	obj1.set_data("Ramesh")
	print("%s %d %d" % obj1.get_data())


if (__name__ == "__main__"):
	main()

