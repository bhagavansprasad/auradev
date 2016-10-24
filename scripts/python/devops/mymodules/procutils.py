import subprocess

def check_output2(cmd):
	command = cmd.split(' ')
	return subprocess.check_output(command)