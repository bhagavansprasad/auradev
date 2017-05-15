#json_file='a.json' 
import json
json_file='t.json'

json_data=open(json_file)
print type(json_data)

data = json.load(json_data)
print type(data)

#print json.dumps(data, sort_keys=True, indent=4)

json_encoded = json.dumps(data)
print type(json_encoded)
#print json_encoded

print '==============='
decoded_data = json.loads(json_encoded)
print type(decoded_data)
exit(1)

print decoded_data

#print "Complex JSON parsing example: ", data['mydata']['list'][1]['name']
#print "Complex JSON parsing example: ", decoded_data['mydata']['list'][0]['name']
#print "Complex JSON parsing example: ", json_encoded['mydata']['list'][0]['name']

json_data.close()
