n = 10
i = j = k = 0

a = [1, 6, 3, 4, 5, 2, 9, 5, 3, 2]
#a = [1, 6, 3, 3, 3, 2, 3, 3, 3, 3]

print("Before removing duplicates...")
print (a)

i = 0
while(i < n):
    j = i + 1
    while(j < n):
        if (a[i] == a[j]):
            a[j] = 0 
        j = j + 1
    i = i + 1

print("After removing duplicates...")
print (a)
