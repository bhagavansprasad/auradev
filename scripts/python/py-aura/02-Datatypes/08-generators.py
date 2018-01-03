import sys

mygenr = (x*x for x in range(5))

print(type(mygenr))
for i in mygenr:
   print((i), end=' ')

print("")
ylist = [x*x for x in range(3)]
print(type(ylist))
print(ylist)

ylist = [x+1 for x in range(3)]
print(ylist)

ylist = [x-1 for x in range(3)]
print(ylist)

print({'x':x-1 for x in range(10,20)})

def createGenerator():
    mylist = list(range(3))
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
    print(i)

print("for bigger list")
def firstn(n):
    num, nums = 0, []
    while num < n:
        #nums.append(num)
        yield num 
        num += 1
sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

