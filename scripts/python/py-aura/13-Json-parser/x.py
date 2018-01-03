import json

json_file='t.json'

json_data = open(json_file)
data = json.load(json_data)

print(data[0]['Id'])


