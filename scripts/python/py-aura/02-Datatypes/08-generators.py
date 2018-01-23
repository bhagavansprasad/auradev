import sys

def main():
	ylist = [x*x for x in range(3)]
	print(type(ylist))
	print(ylist)

	ylist = [x+1 for x in range(3)]
	print(ylist)

	ylist = [x-1 for x in range(3)]
	print(ylist)

	print({'x':x-1 for x in range(10,20)})

	t = [x for x in range(10,20)]
	print (t)

	t = [str(x) for x in range(10,20)]
	print (t)

	t = ["aura"+str(x) for x in range(10,20)]
	print (t)

	t = {'aura'+str(x):x-1 for x in range(10,20)}
	print (t)
	return

if (__name__ == '__main__'):
    main()
