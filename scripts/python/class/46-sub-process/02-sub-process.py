import subprocess

print ('\nwrite:')
proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE,)
print (proc)

#proc.communicate('\tstdin: to stdin\n')
