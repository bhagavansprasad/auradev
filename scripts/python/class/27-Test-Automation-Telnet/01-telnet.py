import sys
import telnetlib

#HOST = "127.0.0.1"
HOST = "192.168.1.38"
user = "bhagavan"
password = "jnjnuh"
cmd = "ls -l"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
print "Prompted login"

tn.write(user + "\n")
print ("Sent username :%s" % (user))

tn.read_until("Password: ")
print "Prompted Password"

if password:
    tn.write(password + "\n")

print ("Sent password :%s" % ("*************"))

tn.read_until(":~$ ")

print ("Got Shell prompt")

'''
tn.write(cmd + "\n")

print ("Sent command :%s" % (cmd))

data =  tn.read_eager()
print data

tn.read_until("total ")
print "Got total "
tn.write("cat t.txt\n")
tn.write("exit\n")
print "=============="
data =  tn.read_all()
print data
print "=============="
'''

ps_cmd = "ps -Al"
service = "myp"
tn.write(ps_cmd + "\n")

print ("Sent command :%s" % (ps_cmd))
tn.read_until("CMD")

data =  tn.read_eager()
#print data

tn.write("exit\n")

data =  tn.read_all()
print ("==========")
#print (data)

if (data.find(service) > 0):
	print ("Service %s is ***Running***" % (service))
else:
	print ("Service %s is ***NOT Running***" % (service))

print ("==========")

