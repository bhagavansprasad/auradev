items1 = [1, 2, 3, 4, 5, 6]
items1.append(7)


def desc_numtype(items):
    print "numtype for %s" % (items)
    for item in items:
        if item % 2 == 0:
            print "Even number= " + str(item)
        else:
            print "Odd number= " + str(item)

desc_numtype(items1)
desc_numtype([6, 7])
items1.remove(2)
items1.remove(7)

print items1[0]
