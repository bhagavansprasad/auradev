import getpass
import sys
import telnetlib

HOST = "127.0.0.1"
user = "bhagavan"
password = "jnjnuh"
#user = raw_input("Enter your remote account: ")

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
print "after login"
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    print "after Password"
    tn.write(password + "\n")

tn.read_until("~$ ")

tn.write("ls -l\n")
data =  tn.read_eager()
print data

tn.read_until("mount.sh")
print "Got mount.sh"
tn.write("cat mount.sh\n")
tn.write("exit\n")
print "=============="
data =  tn.read_all()
print dir(tn)

print "=============="
print data.find("mount.sh")
print type(data)


