from sets import Set

engineers = Set(['Saketh', 'Jana', 'Vachan', 'Aura'])
print engineers

programmers = Set(['Vachan', 'Sama', 'Dheer', 'Aura'])
print programmers

managers = Set(['Jana', 'Vachan', 'Dheer', 'Achyu'])
print managers


employees = engineers | programmers | managers           # union
print employees


engineering_management = engineers & managers            # intersection
print engineering_management

fulltime_management = managers - engineers - programmers # difference
print fulltime_management

engineers.add('Dilip')                                  # add element
print engineers 

print "employees issuperset of engineers", employees.issuperset(engineers) 
print employees
employees.update(engineers)         # update from another set
print employees
print "employees issuperset of engineers", employees.issuperset(engineers) 


for group in [engineers, programmers, managers, employees]: 
    group.discard('Achyu')          # unconditionally remove element
    print group
