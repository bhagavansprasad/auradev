import subprocess

print ('\npopen3:')
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )

print (proc)
print (proc.pid)
print (proc.stdout)
print (proc.stderr)
print (dir(proc))
exit(1)
stdout_value, stderr_value = proc.communicate('through stdin to stdout')
print (stdout_value)
print ('\tpass through:', repr(stdout_value))
print ('\tstderr      :', repr(stderr_value))
