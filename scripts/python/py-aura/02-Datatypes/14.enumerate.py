prog_lagn = ['Python', 'C-Lang', 'Java']
enums_lagn = enumerate(prog_lagn)
print(type(enums_lagn))
print(list(enums_lagn))

enums_lagn = enumerate(prog_lagn, 10)
print(list(enums_lagn))

print("")
prog_lagn = ['Python', 'C-Lang', 'Java']

for item in prog_lagn:
  print(item)

for item in enumerate(prog_lagn):
  print(item)

print("")
for i, temp in enumerate(prog_lagn):
  print(i, temp)

print("")
for i, item in enumerate(prog_lagn, 999):
  print(i, item)
exit(1)
