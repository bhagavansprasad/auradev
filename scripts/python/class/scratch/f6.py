temp = ord('a')
print '%c %d' % (temp, temp)

temp = temp + 1
print '%c %d' % (temp, temp)

print temp

temp = ord('a')
i = 0
while(i < 26):
    print '%c %d' % (temp+i, temp+i)
    i += 1
