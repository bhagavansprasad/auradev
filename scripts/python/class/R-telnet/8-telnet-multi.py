import json
import telnetlib
import time
import sys

def my_debug_print (debug):
    print "\t" + debug

def print_output(data):
    my_debug_print ("----------")
    for line in data.split('\n'):
        my_debug_print(line)
    my_debug_print ("----------")

def start_service_by_name(host, username, password, service):
    '''
    print "host     :", host
    print "username :", username
    print "password :", password
    print "serivce  :", service
    print "host     :", host
    '''

    telnet = telnetlib.Telnet(host)
    print "Telnetting to server '%s' success..." % host

    telnet.read_until("login: ")
    telnet.write(str(username) + '\n')

    telnet.read_until("Password: ")
    telnet.write(str(password) + "\n")
    data = telnet.read_until("~$")
    my_debug_print ("Logging into server '%s' is successful..." % host)

    my_debug_print ("Checking '%s' status..." % service)
    telnet.write("service apache2 status\n")
    data = telnet.read_until("*")
    data = telnet.read_very_eager()
    #print "service status :'%s'" % data
    if (data.find("not") > 0):
        my_debug_print("Service '%s' is not running..." % service)
        my_debug_print("Trying to start service...")
        telnet.write("sudo service apache2 start\n")
        telnet.read_until("[sudo] password ")
        data = telnet.read_very_eager()

        telnet.write(str(password)+'\n')
        data = telnet.read_until("*")
        time.sleep(5)
        data = telnet.read_very_eager()

        if (data.find("failed") > 0):
            my_debug_print ("Service start failed, reason...")
            print_output(data)
        else:
            my_debug_print( "Service start SUCCESS")
    else:
        my_debug_print("Service '%s' is already running..." % service)


    telnet.write("exit\n")


with open('servers.json') as data_file:    
    data = json.load(data_file)

#print(data[0])

for server in data:
    start_service_by_name(server['system_name'], server['username'], server['password'],  server['service'])
    print ""
