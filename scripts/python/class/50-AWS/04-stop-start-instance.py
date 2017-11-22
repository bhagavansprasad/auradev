import sys
import boto
from boto import ec2

#def caliculate_uptime(launch_time):

def aaws_list_all_running_instances(region_name):
	conn=ec2.connect_to_region(region_name)
	reservations = conn.get_all_reservations(filters={'instance-state-name': 'running'})

	for reservation in reservations:
		for instance in reservation.instances:
			print(instance.id, instance.instance_type)


def aaws_get_first_instance_id(region_name):
	conn=ec2.connect_to_region(region_name)
	reservations=conn.get_all_instances();

	print ("")
	i = 1
	for reservation in reservations:
		for instance in reservation.instances:
			return instance.id

def aaws_start_instance_by_id(region_name, inst_id):
	conn = ec2.connect_to_region(region_name)
	conn.start_instances(instance_ids=inst_id)


def aaws_stop_instance_by_id(region_name, inst_id):
	conn = ec2.connect_to_region(region_name)
	conn.stop_instances(instance_ids=inst_id)

#def caliculate_uptime(launch_time):
def aaws_list_instances(region_name):
	conn = ec2.connect_to_region(region_name)
	reservations = conn.get_all_instances();

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
	inst_id = aaws_get_first_instance_id(region_name)
	aaws_stop_instance_by_id(region_name, inst_id)
	aaws_start_instance_by_id(region_name, inst_id)
	aaws_list_instances(region_name)
	aaws_list_all_running_instances(region_name)
	
if (__name__ == "__main__"):
	main()
