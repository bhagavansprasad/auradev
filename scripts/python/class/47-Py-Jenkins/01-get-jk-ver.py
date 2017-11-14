import jenkins

#server = jenkins.Jenkins('http://localhost:8080', username='admin', password='jnjnuh')
server = jenkins.Jenkins('http://127.0.0.1:8080', username='admin', password='jnjnuh')
user = server.get_whoami()
print (user)
#version = server.get_version()
#print('Hello %s from Jenkins %s' % (user['fullName'], version))
