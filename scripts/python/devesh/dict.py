emp = {"Yogesh" : 1000, "Bhagavan": 50000}
#print emp["Yogesh"]

for name in emp:
	print "%s salary=%s" % (name,emp[name])
	
emp = {
	"Yogesh": {"City": "Bangalore", "mobile":989898, "vehicles": ["car1", "bike1"]},
}

emp["User2"] = {"city":"Mysore"}

emp["Yogesh"]["vehicles"][0] = "Alto"
print emp["Yogesh"]["vehicles"][0]
print emp["Yogesh"]["vehicles"]
