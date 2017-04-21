#!/usr/bin/env python
import httplib
import urlparse


def send_http_request(url):
    scheme, server, path, query, fragment = urlparse.urlsplit(url)

    print "scheme :", scheme
    print "server :", server
    print "path   :", path
    print "query  :", query
    print "fragment :", fragment
    
    if scheme == 'http':
        ConnClass = httplib.HTTPConnection
    elif scheme == 'https':
        ConnClass = httplib.HTTPSConnection
    else:
         print 'scheme error'
         exit(1)

    conn = ConnClass(server)
    try:
        conn.request('GET', path, headers={'Host': server})
        response = conn.getresponse()
        ''' 
        print "resp, status :", response.status
        print "resp  reason :", response.reason
        print "msg          :", response.msg
        ''' 
        if response.status != 200:
            print "error in status"

        data = response.read()
        print data

        return (response, response.status, data)

    finally:
        conn.close()

    
url = "http://www.airtel.in/smartbyte-s/page.html"

(response, retcode, data) = send_http_request(url)

print "resp, status :", response.status
print "resp  reason :", response.reason

if (retcode != 200):
    print "msg          :", response.msg
    print data
else:
    print "Error in request"

#get_redirected_url(data)

exit(1)

conn = httplib.HTTPConnection("www.airtel.in")
conn.request("GET", "/smartbyte-s/page.html")
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data

message = response.msg
#print "response.url :", response.url
print "getheaders :", response.getheaders
print "msg        :", response.msg
#print "Location   :", response.msg['Location']
print "Connection :",  message['Connection']

