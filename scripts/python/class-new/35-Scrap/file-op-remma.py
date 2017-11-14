file_object=open("reema.txt",'r')
app1=file_object.read()
len(app1)
print len(app1)
print app1
print app1[2:4]
a=app1[2:4]
b="mango"
c=app1[4:7]
print c
d=a+b+c
print d
file_object.close()
