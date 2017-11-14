tA = (123, 'abcdef')
tB = (345, 'abb')

print("")

print(tA[0])
print(type(tA[0]))

print(tA[0]+5)
print(tA[1]*5)
print(str(tA[0])[0])
print(tA[1][0])

tA = (123, '283')
print("First tuple length : ",  len(tA))

tA = ('1', '98346', 99999)
print("tA :", tA)
print(dir(tA))
print("Max value element tA: ", max(tA))
print("min value element : ", min(tA))

tC = tB + tuple('823')
print(tC)

tB = tB + tuple("823")
print(tB)

print("")
tlist = [123, 'xyz', 'zara', 'abc'];
ttuple = tuple(tlist)
print("Tuple elements : ", ttuple)

tA = ('1', 98346)
#tA[0] = 100;
#tA.append(4)

#del tA;
print("tA  :", tA)

tC = tB + tA + tB + (2, 3, 4, 5)
print("tC  :", tC)

tC = tC + tA

temp = (10, 20)
a, b = temp
print (a)
print (b)

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia)
(name, surname, b_year, movie, m_year, profession, b_place) = julia

print(name, surname)

print("")
months = (' ', 'January','February','March','April','May','June', 'July','August','September','October','November','December')
print("months :", months)

print("")
x = 8
print(months[x])
print(len(months))

#months.sort()
print("months :", months)
exit(1)
