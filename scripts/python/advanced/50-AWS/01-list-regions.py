import sys
import boto
from boto import ec2

def aaws_list_regions(service_name):
	#print(ec2.regions())
	regions = ec2.get_regions(service_name)
	for region in regions:
		print(region.name)

def main():
	service_name = 'ec2'
	aaws_list_regions(service_name)
	
if (__name__ == "__main__"):
	main()
