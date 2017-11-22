import httplib
import socket

airtelurl = "http://www.airtel.in/smartbyte-s/page.html"

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

ipaddr = socket.gethostbyname('www.aitel.in')
print ipaddr

httpServ = httplib.HTTPConnection(ipaddr, 80)
httpServ.connect()

httpServ.request('GET', "/smartbyte-s/page.html")

response = httpServ.getresponse()
if response.status == httplib.OK:
    print "Output from HTML request"
    printText (response.read())

httpServ.close()

'''
httpServ.request('GET', '/cgi_form.cgi?name=Brad&quote=Testing.')

response = httpServ.getresponse()
if response.status == httplib.OK:
    print "Output from CGI request"
    printText (response.read())

httpServ.close()
'''
