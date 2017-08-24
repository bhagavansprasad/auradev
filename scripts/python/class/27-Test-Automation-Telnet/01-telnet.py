import getpass
import sys
import telnetlib

HOST = "127.0.0.1"
user = "git"
password = "jnjnuh"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
print "Received login"

tn.write(user + "\n")

tn.read_until("Password: ")
print "Received Password"

if password:
    tn.write(password + "\n")

tn.read_until("~$ ")

tn.write("ls -l\n")
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


