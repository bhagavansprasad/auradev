import json
 
json_input = '{ "Birds": "Parrot", "Animals":  { "Wild": [ {"Lion":"Asian"},{"Tiger":"BengalTiger"} ] } }'
 
try:
    decoded = json.loads(json_input)

    print type(json_input)
    print type(decoded)
 
    # pretty printing of json-formatted string
    print json.dumps(decoded, sort_keys=True, indent=8)
 
    print "JSON parsing example        :", decoded['Animals']
    print "Complex JSON parsing example:", decoded['Animals']['Wild']
    print "Complex JSON parsing example:", decoded['Animals']['Wild'][0]
    print "Complex JSON parsing example:", decoded['Animals']['Wild'][0]['Lion']
    exit(1)
 
except (ValueError, KeyError, TypeError):
    print "JSON format error"
