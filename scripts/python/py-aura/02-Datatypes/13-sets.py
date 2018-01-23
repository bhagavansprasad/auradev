
engineers = set(['Saketh', 'Jana', 'Vachan', 'Aura'])
print("engineers   :", engineers)

programmers = set(['Vachan', 'Sama', 'Dheer', 'Aura'])
print("programmers :", programmers)

managers = set(['Jana', 'Vachan', 'Dheer', 'Achyu'])
print("managers    :", managers)

employees = engineers | programmers | managers           # union
print("employees :", employees)

engineering_management = engineers & managers            # intersection
print("engineering_management :", engineering_management)

fulltime_management = managers - engineers - programmers # difference
print("fulltime_management :", fulltime_management)

engineers.add('Dilip')                                  # add element
print("engineers   :", engineers)

print("employees is superset of engineers :", employees.issuperset(engineers)) 
print(employees)

employees.update(engineers)         # update from another set

print(employees)
print("employees is superset of engineers :", employees.issuperset(engineers)) 


for group in [engineers, programmers, managers, employees]: 
    group.discard('Achyu')          # unconditionally remove element
    print(group)
