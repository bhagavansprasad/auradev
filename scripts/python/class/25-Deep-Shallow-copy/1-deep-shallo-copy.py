d1 = [10, 20, 30, 40, 50]
print "d1    :", d1     #10, 20, 30, 40, 50
print "d1[3] :", d1[3]  #40

d2 = d1
print "d2    :", d2     #10, 20, 30, 40, 50
print "d2[3] :", d2[3]  #40

d1[3] = 80

print "d1    :", d1     #10, 20, 30, 80, 50
print "d1[3] :", d1[3]  #80

print "d2    :", d2     #10, 20, 30, 40, 50
print "d2[3] :", d2[3]  #40


d2[0] = 90
print "d1    :", d1     #10, 20, 30, 80, 50
print "d2    :", d2     #90, 20, 30, 40, 50


print "id(d1) :", id(d1)
print "id(d2) :", id(d2)

d2 = list(d1)

print "id(d1) :", id(d1)
print "id(d2) :", id(d2)

exit(1)
