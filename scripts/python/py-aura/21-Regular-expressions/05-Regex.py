import re

file_name = "data.txt"

with open(file_name, 'r') as fd:
    data = fd.readlines()

for line in data:
    line =  line.strip()
    match = re.findall(r'\d\d\d\d', line)
    if match:
       print (line)
