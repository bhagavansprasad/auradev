import getpass
import sys
import telnetlib

HOST = "localhost"
#user = raw_input("Enter your remote account: ")
user = "bhagavan"
password = "jnjnuh"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls -l\n")
tn.write("exit\n")

data =  tn.read_all()
print data
print type(data)
