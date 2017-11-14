n = 5
i = j = k = 0

              i  j
a = [6, 8, 2, 9, 4]
a = [2, 8, 6, 9, 4]
a = [2, 6, 8, 9, 4]
a = [2, 4, 8, 9, 6]
a = [2, 4, 6, 9, 8]
a = [2, 4, 6, 8, 9]

t = a[j]
a[j] = a[i]
a[i] =  t

print "Before sorting..."
while(i < n):
    print a[i], " ",
    i = i + 1
print ""


exit(1)
