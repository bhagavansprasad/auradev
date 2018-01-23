#json_file='a.json' 
import json
json_file = 't.json'

fd = open(json_file)
print(type(fd))

json_obj = json.load(fd)

print(type(json_obj))
print(json_obj[0]['Id'])
print (json.dumps(json_obj, sort_keys=True, indent=4))

json_decoded = json.dumps(json_obj)
print(type(json_decoded))
print (json_decoded)

#print (json_decoded[0]['Id'])
print('===============')
encoded_data = json.loads(json_decoded)

print(type(encoded_data))
print(encoded_data)
print(encoded_data[0]['Id'])
exit(1)

#print "Complex JSON parsing example: ", data['mydata']['list'][1]['name']
#print "Complex JSON parsing example: ", decoded_data['mydata']['list'][0]['name']
#print "Complex JSON parsing example: ", json_encoded['mydata']['list'][0]['name']

json_data.close()
