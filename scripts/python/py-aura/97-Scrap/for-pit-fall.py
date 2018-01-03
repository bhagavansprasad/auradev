'''
global k
k = 6
print (id(k))
for j in range(1, k):
	k = int(k - 1)
	print (id(k))
	print (j)

print (range(10))
'''

n = 5
k = n 
for i in range(1, n+1):
	for j in range(1, k+1):
		print (j, end='')
	print ("")
	k = k - 1
