import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('http://www.airtel.in/smartbyte-s/page.html')
soup = BeautifulSoup(page)

x = soup.body.find('src', attrs={'class' : 'container'}).text
