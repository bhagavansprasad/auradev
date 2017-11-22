import sys
import boto
from boto import ec2

#def caliculate_uptime(launch_time):
def aaws_list_instances(region_name):
	connection=ec2.connect_to_region(region_name)
	reservations=connection.get_all_instances();

	print ("")
	i = 1
	for reservation in reservations:
		for instance in reservation.instances:
			#uptime = caliculate_uptime(instance.launch_time)
			print ("%3d. %-30s %-30s %-30s %-30s" % (i, instance.tags['Name'], instance.state, instance.launch_time, instance.ip_address) )
			i = i + 1

def main():
	region_name = 'ap-south-1'
	aaws_list_instances(region_name)
	
if (__name__ == "__main__"):
	main()
