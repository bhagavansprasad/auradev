import f2

myStorage = f2.useMyVars(0) # initialze class and properties

for i in range(0,10):
    print "Hello, "
    f2.print_world()
    myStorage.setMyVar(i)
    f2.inc_gMyVar()

print "Display class property myVar:", myStorage.getMyVar()
print "Display global variable gMyVar:", f2.get_gMyVar()
