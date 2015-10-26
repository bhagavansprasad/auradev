import nltk   
from urllib import urlopen

url = "http://www.airtel.in/smartbyte-s/page.html"
html = urlopen(url).read()    
raw = nltk.clean_html(html)  
print(raw)
