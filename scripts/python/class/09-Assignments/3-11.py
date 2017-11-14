n = 5

for i in range (1, n+1):

	for j in range (1, i):
		print(' ', end='') #3
		#print ' ',         #2.7
	
	for j in range (1, n+2-i):
		print(j, end='')
		#print('%d' % j, end=' ')
		#print j,

	print ("")
