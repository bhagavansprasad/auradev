import HTMLParser
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Found a start tag  :", tag

    def handle_endtag(self, tag):
        print "Found an end tag   :", tag

    def handle_startendtag(self, tag, attrs):
        print "Found an empty tag :", tag

    def handle_data(self, data):
        print "data  :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
#parser.feed("<html><head><title>HTML Parser - I</title></head>" +"<body><h1>HackerRank</h1><br /></body></html>")
hdata = open("t.html").readlines()
print hdata

for line in hdata:
    sp = line.find('src="http') 
    if (sp > 0):
        #print sp
        ep = line.find(' ', sp) 
        #print ep
        rurl = line[sp:ep]
        rurl = rurl.lstrip('src="').rstrip('"')
        print rurl


