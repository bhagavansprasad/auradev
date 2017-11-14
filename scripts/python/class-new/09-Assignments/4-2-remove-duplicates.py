n = 10
i = j = k = 0
#              i  j
a = [1, 6, 3, 4, 5, 2, 9, 5, 3, 2]
#a = [1, 6, 3, 3, 3, 2, 3, 3, 3, 3]

print "Before removing duplicates..."
while(i < n):
    print a[i], " ",
    i = i + 1
print ""

i = 0
while(i < n):
    j = i + 1
    while(j < n):
        if (a[i] == a[j]):
            k = j + 1
            while(k < n):
                a[k-1] = a[k]
                k = k + 1
            n = n -1
            j = j - 1
        j = j + 1
    i = i + 1

print "After removing duplicates..."
i = 0
while(i < n):
    print a[i], " ",
    i = i + 1
print ""
