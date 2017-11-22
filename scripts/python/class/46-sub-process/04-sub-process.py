import sys
import subprocess

#cmd = ['python', 'test.py']
cmd = ['ls -l']

cmd = subprocess.Popen( cmd, 
						shell=True, 
						stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE,
						universal_newlines=True)
for line in cmd.stdout:
	print (line)
	'''
    columns = line.decode().split()
    if columns:
        print(columns[-1])
	'''
