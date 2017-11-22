#!/usr/bin/env python
import skew
from skew.arn import ARN
arn = ARN()
services=arn.service.choices()
services.sort()
#services=["route53", "iam"]
print('Enumerating all resources in the following services: ' + ' '.join(services) + '\n')
for service in services:
  #skipping global services because the API endpoint fails due to it being a global service. Bug that needs fixing.
  if service == "iam" or service == "route53":
    print(service)  
    print('Skipping global services')
    #uri = 'arn:aws:' + service + '::*:*/*'
    #arn = skew.scan(uri)
    #for i in arn:
    #  print(i.arn)
  else:
    print('******' + service + '******')
    uri = 'arn:aws:' + service + ':*:*:*/*'
    arn = skew.scan(uri)
    for i in arn:
      print(i.arn)
