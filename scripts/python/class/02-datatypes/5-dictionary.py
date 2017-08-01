'''
<student>
    <name> aura </name>
    <class> 5 </class>
    <marks> 
        <s1> 45 </s1>
        <s1> 40 <s1>
    </marks>
</student>
<student>
    <name> aura </name>
    <marks> 234 </marks>
    <marks> 234 </marks>
    <marks> 234 </marks>
</student>
'''

'''
student_data = {
        student[
            {"name":"aura",
            "class":5,
            "marks":[
                {"s1":45},
                {"s2":40}
                ]
            },
            {"name":"temp",
            "class":5,
            "marks":[
                {"s1":45},
                {"s2":40}
                ]
            },
            ]
        }
'''

#json

symbol_to_name = {
	"H": "hydrogen",
	"He": "helium",
	"Li": "lithium",
	"C": "carbon",
	"O": "oxygen",
	"N": "nitrogen",
        "P": "phosp"
}

print symbol_to_name
print symbol_to_name.keys()
print symbol_to_name.values()
print symbol_to_name.values()[0]
print symbol_to_name.values()[0][0]
print symbol_to_name.items()

print symbol_to_name["C"]
print symbol_to_name["O"]

print "O" in symbol_to_name, "U" in symbol_to_name
print "o" in symbol_to_name

if ("O" in symbol_to_name):
    print "Symbol is available"

if ("U" in symbol_to_name):
    print "Symbol is available"
else:
    print "Symbol is NOT available"

print "oxygen" in symbol_to_name

print symbol_to_name.get("P", "The item 'P' Not available")
print symbol_to_name.get("C", "Not available")
print symbol_to_name.update( {"P": "phosphorous", "S": "sulfur"} )
print symbol_to_name
del symbol_to_name['C']
print symbol_to_name
#print symbol_to_name["C"]

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'phone': ['9902000000', '900000000']}
print "dict['Name']: ",  dict['Name']
print "dict['Age']: ",   dict['Age']
print "dict['Class']: ", dict['Class']
print "dict['phone']: ", dict['phone']
print "dict['phone']: ", dict['phone'][1]
print "dict['phone']: ", dict['phone'][0][0]

print "dict['Age']  : ", type(dict['Age'])
print "dict['Class']: ", type(dict['Class'])
print "dict['phone']: ", type(dict['phone'])
print "dict['phone']: ", type(dict['phone'][0])
print "dict['phone']: ", type(dict['phone'][0][0])

print dict
print type(dict)
print dir(dict)

atomic_number_to_name = {
    1: "hydrogen",
    6: "carbon",
    7: "nitrogen",
    8: "oxygen",
}

print atomic_number_to_name
print atomic_number_to_name[1]
print atomic_number_to_name[8]

nobel_prize_winners = {
    (1979, "physics"): ["Glashow", "Salam", "Weinberg"],
    (1962, "chemistry"): ["Hodgkin"],
    (1984, "biology"): ["McClintock"],
}
print nobel_prize_winners[(1979, "physics")]

states = {
    'Andhra Pradesh': 'AP',
    'Karnataka': 'KA',
    'Telangana': 'TS',
    'Tamilnadu': 'TN',
    'Gujarath': 'GJ',
    'Maharashtra': 'MH'
}

cities = {
    'MH': 'Mumbai',
    'AP': 'Amaravathi',
    'TS': 'Hyderabad',
    'TN': 'Chennai',
    'KA': 'Benguluru'
}

print states
print cities

states['Odisha'] = 'OR'
cities['OR'] = 'Bhuvaneswar'
cities['GJ'] = 'Ahemadabad'

print states
print cities

print '-' * 10
print "MH State has: ", cities['MH']
print "OR State has: ", cities['OR']

print '-' * 10
print "Karnataka's abbreviation is: ", states['Karnataka']
print "Maharashtra's abbreviation is: ", states['Maharashtra']

# do it by using the state then cities dict
print '-' * 10
print "Maharashtra has: ", cities[states['Maharashtra']]
print "Gurarath has: ",    cities[states['Gujarath']]

print '-' * 10
for state, abbrev in states.items():
    print "'%s' is abbreviated '%s'" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "'%s' has the city '%s'" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "'%s' state is abbreviated '%s' and has city '%s'" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Kerala')
#print states['Kerala']
print state

if not state:
    print "Sorry, no Kerala."

# get a city with a default value
city = cities.get('KR', 'Does Not Exist')
print "The city for the state 'KR' is: %s" % city

print type(city)

my_dict = {'Name': 'Aura', 'Age': 5, 'Location': 'Bangalore'}

print "my_dict['Name']: ", my_dict['Name']
print "my_dict['Age']: ", my_dict['Age']

print my_dict

my_dict['Name'] = 'saketh'
my_dict['Age'] = 15

print my_dict

del my_dict['Name'];

print my_dict

my_dict['Name'] = 'Vachan';

print my_dict

my_dict.clear();   

print my_dict

del my_dict ;     
#print my_dict

# empty dictionary
my_dict = {}
print my_dict

# dictionary with mixed keys
my_dict = {'name': 'Aura', 1: [2, 9, 7, 4, 3]}
print my_dict['name']
print my_dict[1][0]
print my_dict[1][0:3]
print my_dict[1][0:3][1]

print type(my_dict[1])

for value in my_dict[1]:
    print value,

print " "

customers = [
             {"uid":1,"name":"Vachan"},
             {"uid":2,"name":"Ram"},
             {"uid":3,"name":"Saketh"},
            ]

print customers

for cust in customers:
    print cust["uid"], cust["name"]

for cust in customers:
    cust["password"]="123456"

print customers
exit(1)

