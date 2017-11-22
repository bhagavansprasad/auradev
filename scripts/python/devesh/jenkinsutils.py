import requests
import httplib
# from requests.auth import HTTPDigestAuth


class JenkinsBuild(object):
    def __init__(self, jsondata):
        self.data = jsondata

    @property
    def url(self):
        return self.data['url']

    @property
    def building(self):
        return self.data['building']


class JenkinsAPI(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.mount('http://',
                           requests.adapters.HTTPAdapter(max_retries=5))
        # self.session.auth = HTTPDigestAuth('admin', 'jnjnuh')
        self.jurl = "http://192.168.1.253:8082"

    def request(self, url):
        r = self.session.get(url)
        if r.status_code in [httplib.OK, httplib.CREATED, httplib.NOT_FOUND]:
            return r
        return None

    def json_api_request(self, url):
        url = "http://192.168.1.253:8082/job/%s/api/json" % (url)
        r = self.request(url)
        if r is None:
            return {}

        return r.json()

    def json_api_request2(self, build):
        url = "%s/job/%s/api/json" % (self.jurl, build)
        r = self.request(url)
        if r is None:
            return {}
        build = JenkinsBuild(r.json())
        return build

    # http://192.168.1.253:8082/job/simple-job/build?token=mypass
    def dobuild(self, jobname):
        url = "%s/job/%s/build?token=mypass" % (self.jurl, jobname)
        print url
        self.request(url)


j = JenkinsAPI()
job = j.json_api_request('caller-job/1')
print job['url']
build = JenkinsBuild(job)
print build.url
print build.building
if build.building:
    print "This job is running"
else:
    print "This job is completed"

build2 = j.json_api_request2('caller-job/1')
if build2.building:
    print "This job is running"
else:
    print "This job is completed"

# trigger build
job = JenkinsAPI()
job.dobuild('simple-job')

# get latest builds
job = j.json_api_request('simple-job')
print job['builds'][0]
