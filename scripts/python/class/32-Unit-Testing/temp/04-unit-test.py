import subprocess
cmd = ['python', 'test.py']

output = subprocess.check_output(['ls', '-1'])
print(('Have %d bytes in output' % len(output)))
print (output)

output = subprocess.check_output(cmd)
print (output)
exit(1)
#p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
out, err = p.communicate() 
#print (out)
result = out.split('\n')
for lin in result:
    if not lin.startswith('#'):
        print(lin)
