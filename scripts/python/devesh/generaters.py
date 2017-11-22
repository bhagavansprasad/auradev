import sys

ylist = [x*x for x in range(3)]
print ylist
ylist = [x+1 for x in range(3)]
print ylist
ylist = [x-1 for x in range(3)]
print ylist

print {'x':x-1 for x in range(10,20)}


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
    print(i)

print "for bigger list"
def firstn(n):
    num, nums = 0, []
    while num < n:
        #nums.append(num)
        yield num 
        num += 1
sum_of_first_n = sum(firstn(1000000))
print sum_of_first_n
   
# Using the generator pattern (an iterable)
class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self
    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()
            

print "1. ", firstn(100)
sum_of_first_n = sum(firstn(1000000))
print "2. ", sum_of_first_n
