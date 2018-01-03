#json_file='a.json' 
import json
json_file = 't.json'

fd = open(json_file)
print(type(fd))

json_obj = json.load(fd)
print(type(json_obj))

print(json_obj[0]['Id'])

exit(1)
#print json.dumps(data, sort_keys=True, indent=4)

json_encoded = json.dumps(json_obj)
print(type(json_encoded))
#print json_encoded

#print json_encoded[0]['Id']
print('===============')
exit(1)
decoded_data = json.loads(json_encoded)
print(type(decoded_data))

print(decoded_data)

print(decoded_data['Id'])
exit(1)

#print "Complex JSON parsing example: ", data['mydata']['list'][1]['name']
#print "Complex JSON parsing example: ", decoded_data['mydata']['list'][0]['name']
#print "Complex JSON parsing example: ", json_encoded['mydata']['list'][0]['name']

json_data.close()
