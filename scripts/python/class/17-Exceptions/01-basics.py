a = [10, 20, 30]
print((a[0]))

tstr = "Aura Networks"

try:
	print((a[3]))
except IndexError:
	print ("I got exception")

print((a[1]))

print((tstr[1]))

try:
	print((tstr[20]))
except IndexError:
	print ("Index error while reffering string")

try:
	print((a[3]))
except (TypeError, IndexError) as e:
	print (e)
	print ("Type error")
