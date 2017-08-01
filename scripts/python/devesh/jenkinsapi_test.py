import requests
import time
session = requests.Session()
session.mount('http://',
              requests.adapters.HTTPAdapter(max_retries=1))
r = session.get("http://192.168.1.254:8081/job/validation4/api/json")
d = r.json()
#print d
#print d['builds'][-1]['url']
#print d['fullDisplayName']
#print d['url']
#r = session.get("http://192.168.1.254:8081/job/validation4/build")
#time.sleep(10)
r = session.get("http://192.168.1.254:8081/job/validation4/api/json?depth=1")
d = r.json()
#print d
print d['builds'][0]['url']
print d['builds'][0]['building']
