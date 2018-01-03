fd = open("t.txt", "r")
data = fd.read(10)
print (data)
fd.close()
