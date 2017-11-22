import boto
import boto.ec2
import boto.ec2.cloudwatch

boto.set_stream_logger('foo')
ec2 = boto.connect_ec2(debug=2)

#conn = boto.ec2.cloudwatch.connect_to_region(region_name)
region_name = 'ap-south-1'
ec2con = boto.ec2.cloudwatch.connect_to_region(region_name)
#ec2con =     ec2.           connect_to_region("us-west-1")  
for obj in dir(ec2con):
	print (obj)

snap = ec2con.get_all_snapshots(['snap-3b82a650'])[0]
print(snap.id)
print(snap.volume_id)
print(snap.status)
print(snap.start_time)
print(snap.owner_id)
print(snap.volume_size)
print(snap.description)
