import json

'''
servers_list = [ 
 {
   "system_ip": "localhost",
   "username": "bhagavan",
   "password": "jnjnuh"
 },
 {
   "system_ip": "192.168.1.1",
   "username": "bhagavan",
   "password": "jnjnuh"
 },
 {
   "system_ip": "127.0.0.1",
   "username": "bhagavan",
   "password": "jnjnuh"
 }
]
print servers_list
print servers_list[0]
print servers_list[0]["system_ip"]
print servers_list[0]["username"]
print servers_list[0]["password"]

for system in servers_list:
    print system["system_ip"]
    print system["username"]
    print system["password"]

'''

with open('servers.json') as data_file:    
    data = json.load(data_file)

#print(data[0])

for server in data:
    print server['system_ip'], server['username'], server['password'],  server['service']
    print ""
