# Program to show the use of lambda functions

double = lambda x: x * 2
print(double(5))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

print ""

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print map(lambda x,y:x+y, a, b)
print map(lambda x,y,z : x+y+z, a,b,c)
print map(lambda x,y,z : x+y-z, a,b,c)
exit(1)
