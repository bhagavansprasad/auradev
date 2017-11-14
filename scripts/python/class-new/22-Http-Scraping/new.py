import httplib
import time

url = "www.airtel.in"

conn = httplib.HTTPConnection(url)
conn.request("GET", "/smartbyte-s/page.html")
response = conn.getresponse()

print "status :", response.status
print "reason :", response.reason

data = response.read()
print "data :", data
print type(data)

sub_str_spos = data.find('src="http:')
print "sub_str_spos :", sub_str_spos

sub_str_epos = data.find(' ', sub_str_spos)
print "sub_str_epos :", sub_str_epos

print data[sub_str_spos:sub_str_epos]

print data[sub_str_spos:sub_str_epos].rstrip('src=')

'''
print "resp, status :", response.status
print "resp  reason :", response.reason
print "retcode      :", retcode
'''
