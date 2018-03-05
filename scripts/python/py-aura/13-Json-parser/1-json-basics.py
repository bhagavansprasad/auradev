import json
 
json_obj = { "Birds": "Parrot", "Animals":  { "Wild": [ {"Lion":"Asian"},{"Tiger":"BengalTiger"} ] } }

#print (json_obj["Animals"]["Wild"][0]["Lion"])

print(type(json_obj))
print (json_obj)
print(json.dumps(json_obj, sort_keys=True, indent=8))
print(json_obj["Birds"])
print(json_obj["Animals"])

json_obj = { "Birds": "Parrot", "Animals":  { "Wild": [ {"Lion":"Asian"},{"Tiger":"BengalTiger"} ] } }
json_str ='{ "Birds": "Parrot", "Animals":  { "Wild": [ {"Lion":"Asian"},{"Tiger":"BengalTiger"} ] } }'
print (type(json_obj))
print (type(json_str))

try:
    njson_obj = json.loads(json_str)
    print(type(njson_obj))
 
    print(njson_obj["Bird"])
    # pretty printing of json-formatted string
    print(json.dumps(njson_obj, indent=4))

    print("njson_obj['Animals']                      :", njson_obj['Animals'])
    print("njson_obj['Animals']['Wild']              :", njson_obj['Animals']['Wild'])
    print("njson_obj['Animals']['Wild'][0]           :", njson_obj['Animals']['Wild'][0])
    print("njson_obj['Animals']['Wild'][0]['Lion']   :", njson_obj['Animals']['Wild'][0]['Lion'])
    exit(1)
 
except (ValueError, KeyError, TypeError):
    print ("JSON format error")

pos2coin =  { 
    (1, 1) : { "ccolor" : "w", "coin" : "K", "pos":(1, 1) }, #White King
    (1, 2) : { "ccolor" : "b", "coin" : "k", "pos":(1, 2) }, #Black King
}

coin2pos = {
    "K" : (1, 1),
    "k" : (1, 2),
}

print (pos2coin)
pos2coin.update({(1, 1):{"coin": "Q", "pos":(1, 1)}})
pos2coin[1, 1]["coin"] = "Q"
print (pos2coin)
print (coin2pos)

