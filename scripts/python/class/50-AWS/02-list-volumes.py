import boto
import sys
from boto import ec2

def list_valumes(region_name):
	try:
		connection=ec2.connect_to_region(region_name)
		volumes=connection.get_all_volumes()
		print ("ID, name, status")
		for volume in volumes:
			print ("%-30s %-30s %-30s" % (volume.id, volume.tags["Name"], volume.status))

	except:
		print ('Some Error occurred :')
		print (sys.exc_info())

def main():
	region_name = 'ap-south-1'
	list_valumes(region_name)
	
if (__name__ == "__main__"):
	main()
