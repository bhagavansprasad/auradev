import getpass
import sys
import telnetlib

user = "git"
password = "jnjnuh"

fd = open(sys.argv[1], "r")
list_of_servers = fd.readlines()
print list_of_servers
fd.close()

for server in list_of_servers:
    server = server.rstrip('\n')
    tn = telnetlib.Telnet(server)

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
    print "Got total"
    tn.write("cat t.txt\n")
    tn.write("exit\n")
    print "=============="
    data =  tn.read_all()
    print data
    print "=============="


'''
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

    data =  tn.read_eager()
    print data
    tn.read_until("~$ ")
    tn.write("ls -l" + "\n")
    data =  tn.read_eager()
    print data

    tn.read_until("mount.sh")
    print "reading_all..."
    data =  tn.read_all()
    print "data ", data
'''
