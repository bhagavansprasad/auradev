#!/usr/bin/python 

with open("/proc/self/cgroup", 'r') as descriptor:
    file_content = descriptor.readlines()

print file_content
print file_content[0]
print file_content[0].split('/')[-1]


