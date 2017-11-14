import smtplib
import datetime

fromaddr = "pyscript@foreman.auradev.com"
toaddrs  = "bhagavan@foreman.auradev.com"
subject  = "Demo of email sending"

header = ("From: %s\r\nTo: %s\r\nSubject:%s\r\n\r\n" % (fromaddr, toaddrs, subject))
data = "This is a mail from me, with information about sending email from pythong script"

print "header  :", header
print "data :", data

header = header + data

print "Message length is " + repr(len(header))

server = smtplib.SMTP('localhost')

server.set_debuglevel(1)

server.sendmail(fromaddr, toaddrs, header)
server.quit()
