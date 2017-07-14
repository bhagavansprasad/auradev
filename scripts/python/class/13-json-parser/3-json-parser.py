#json_file='a.json' 
import json
json_file='t.json'

json_data = open(json_file)
print type(json_data)

data = json.load(json_data)
print type(data)

print data[0]['Id']

exit(1)
#print json.dumps(data, sort_keys=True, indent=4)

json_encoded = json.dumps(data)
print type(json_encoded)
#print json_encoded

#print json_encoded[0]['Id']
print '==============='
exit(1)
decoded_data = json.loads(json_encoded)
print type(decoded_data)

print decoded_data

print decoded_data['Id']
exit(1)

#print "Complex JSON parsing example: ", data['mydata']['list'][1]['name']
#print "Complex JSON parsing example: ", decoded_data['mydata']['list'][0]['name']
#print "Complex JSON parsing example: ", json_encoded['mydata']['list'][0]['name']

json_data.close()
