from lxml.html import parse
doc = parse('http://www.airtel.in/smartbyte-s/page.html').getroot()
for div in doc.cssselect('a'):
    print '%s: %s' % (div.text_content(), div.get('src'))
