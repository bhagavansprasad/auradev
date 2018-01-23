#!/usr/bin/env python
import http.client
import urllib.parse

conn = http.client.HTTPConnection("localhost")
conn.request("GET", "/index.html")

response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)

message = response.msg
#print "response.url :", response.url
print("getheaders :", response.getheaders)
print("msg        :", response.msg)
print("Location   :", response.msg['Location'])
print("Connection :", message['Connection'])

scheme, netloc, path, query, fragment = urllib.parse.urlsplit(response.msg['Location'])
print("scheme :", scheme)
print("netloc :", netloc)
print("path   :", path)
print("query  :", query)
print("fragment :", fragment)

conn.close()

