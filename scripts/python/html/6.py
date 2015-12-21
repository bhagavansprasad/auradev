from bs4 import BeautifulSoup
import urllib
import socket
import datetime

fp = open('/home/bhagavan/airtel/airtel_usage.csv','a')
searchurl = "http://www.airtel.in/smartbyte-s/page.html"
r = urllib.urlopen(searchurl).read()
soup = BeautifulSoup(r, "lxml")

frame = soup.find_all("iframe")
#print (frame)
#print (str(frame))
new_str =str(frame)
#print (new_str)
#print new_str.find("src=", 0, len(new_str))
start = new_str.find("src=", 0, len(new_str)) + len("src=") + 1
#print start
end = new_str.find('"', start) 
#print end
new_url = new_str[start:end]
r = urllib.urlopen(new_url).read()
soup = BeautifulSoup(r, "lxml")

frame = soup.find("div", class_="detail")
#print (frame)

#print frame.find('span')
result = str(frame)

start = result.find("<span>", 0, len(result)) + len("<span>")
end = result.find("</span>", start, len(result)) 
#print start
#print end
data_avbl = result[start:end-len(" GB")]
print data_avbl
start = end + len("</span>")
end = result.find("</span>", start, len(result)) + len("</span>")
start = end 
start = result.find("<span>", start, len(result)) + len("<span>")
end = result.find("</span>", start, len(result)) 
#print start
#print end
days_left = result[start:end-len(" day(s)")]
#print "data avalable :%s" % data_avbl
#print "days left     :%s" % days_left
#print "2.--------------"

str_date = datetime.datetime.now().strftime("%d-%m-%Y")
str_time = datetime.datetime.now().strftime("%H:%M")
print "%s\t%s\t%s\t%s" % (str_date, str_time, data_avbl,  days_left)
final =  "%s, %s, %s, %s\n" % (str_date, str_time, data_avbl,  days_left)

fp.write(final) # python will convert \n to os.linesep
fp.close()
