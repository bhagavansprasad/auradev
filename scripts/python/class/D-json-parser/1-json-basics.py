import json
 
json_input = '{ "Bone": 1, "Atwo":  { "list": [ {"item":"A"},{"item":"B"} ] } }'
 
try:
    decoded = json.loads(json_input)

    print type(json_input)
    print type(decoded)
 
    # pretty printing of json-formatted string
    print json.dumps(decoded, sort_keys=True, indent=8)
 
    print "JSON parsing example: ", decoded['Atwo']
    print "Complex JSON parsing example: ", decoded['Btwo']['list'][0]['item']
    print decoded['Btwo']
    print decoded['Btwo']['list']
    print decoded['Btwo']['list'][0]
    print json_input
 
except (ValueError, KeyError, TypeError):
    print "JSON format error"
