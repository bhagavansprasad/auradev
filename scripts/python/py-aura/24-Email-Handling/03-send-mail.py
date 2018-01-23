import smtplib

fromaddr = "pyscript@foreman.auradev.com"
toaddrs  = "bhagavan@foreman.auradev.com, git@foreman.auradev.com"
subject  = "Build status"
textfile = "t.txt"

with open(textfile) as fp:
    data = fp.readlines()

msg = ("From: %s\r\nTo: %s\r\nSubject:%s\r\n\r\n" % (fromaddr, toaddrs, subject))

msg = msg + "".join(data)

print (msg)
print ("Message length is " + repr(len(msg)))

server = smtplib.SMTP('localhost')

server.set_debuglevel(1)

server.sendmail(fromaddr, toaddrs, msg)
server.quit()
