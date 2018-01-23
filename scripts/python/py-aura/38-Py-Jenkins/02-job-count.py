import jenkins

server = jenkins.Jenkins('http://admin:jnjnuh@localhost:8080')
print (server.jobs_count())
