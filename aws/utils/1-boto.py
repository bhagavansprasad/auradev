import boto
from boto import ec2
connection=ec2.connect_to_region("ap-south-1")
reservations=connection.get_all_instances();
 
for reservation in reservations:
 for instances in reservation.instances:
    print instances
    print dir(instances)
    print instances.state_reason
    print instances.state_reason['message']
    print instances.ip_address

    print instances.tags
    #print "%s \t \t %s" % (instances.tags['Name'], instances.ip_address) 
