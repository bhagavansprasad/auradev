import boto
boto.set_stream_logger('boto')
s3 = boto.connect_s3()
