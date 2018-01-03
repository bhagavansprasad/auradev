from jenkinsapi import jenkins
jurl = "http://127.0.0.1:8080"
uname = "admin"
psw = "jnjnuh"
job = "test1"
j = jenkins.Jenkins(ci_jenkins_url, username=username, password=token)
j = Jenkins(jurl, username=uname, password=psw, requester=CrumbRequester(username=uname, password=psw, baseurl='https://myjenkins'))
#j = Jenkins('https://myjenkins', username='willi', password='passvoid', requester=CrumbRequester(username='willi', password='passvoid', baseurl='https://myjenkins'))

print ("++++++++++")
print (j)
print ("++++++++++")

if __name__ == "__main__":
    j.build_job(job)
