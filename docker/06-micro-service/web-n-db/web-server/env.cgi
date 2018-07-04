#!/usr/bin/python
import os

print "Content-type: text/html\r\n\r\n";

with open("/proc/self/cgroup", 'r') as descriptor:
    file_content = descriptor.readlines()

print "<br>%s" % file_content
print "<br>%s" % file_content[0]
print "<br>%s" % file_content[0].split('/')[-1]

print "<font size=+1>Environment</font>";
for param in os.environ.keys():
  print "<br>%20s: %s" % (param, os.environ[param])



