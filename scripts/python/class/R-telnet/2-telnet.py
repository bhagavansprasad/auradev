import getpass
import sys
import telnetlib

user = "bhagavan"
password = "jnjnuh"

fd = open(sys.argv[1], "r")
list_of_servers = fd.readlines()
print list_of_servers

print dir(telnetlib)

for server in list_of_servers:
    server = server.rstrip('\n')
    print "server :%s, username :%s, pass :%s" % (server, user, password)

    tn = telnetlib.Telnet(server)
    tn.read_until("login: ")
    print "after login"
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        print "after Password"
        tn.write(password + "\n")

    tn.read_until("~$ ")
    tn.write("ls -l\r\n")
    data =  tn.read_very_eager()
    print data
    #print "reading_all..."
    #data = tn.read_all()
    #print data
    sys.stdout.flush()


