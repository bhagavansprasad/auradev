import json
 
json_obj = { "Birds": "Parrot", "Animals":  { "Wild": [ {"Lion":"Asian"},{"Tiger":"BengalTiger"} ] } }
print(type(json_obj))

print((json_obj["Birds"]))
print((json_obj["Animals"]))

json_str = '{ "Birds": "Parrot", "Animals":  { "Wild": [ {"Lion":"Asian"},{"Tiger":"BengalTiger"} ] } }'
print (type(json_obj))

try:
	njson_obj = json.loads(json_str)
	print(type(njson_obj))
 
	# pretty printing of json-formatted string
	print(json.dumps(njson_obj, sort_keys=True, indent=4))

	print(("njson_obj['Animals']                      :", njson_obj['Animals']))
	print(("njson_obj['Animals']['Wild']              :", njson_obj['Animals']['Wild']))
	print(("njson_obj['Animals']['Wild'][0]           :", njson_obj['Animals']['Wild'][0]))
	print("njson_obj['Animals']['Wild'][0]['Lion']   :", njson_obj['Animals']['Wild'][0]['Lion'])
 
except (ValueError, KeyError, TypeError):
    print ("JSON format error")
