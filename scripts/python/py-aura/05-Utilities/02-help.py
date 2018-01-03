import sys
import boto

def import_modules_dynamically():
	moduleNames = ['sys', 'os', 're', 'unittest']
	print(moduleNames)
	modules = map(__import__, moduleNames) 

	i = 0
	while (i < len(moduleNames)):
		print (modules[i])
		i = i + 1
	return


def print_modpath(modname):
	print("Module :%s" % modname)
	module = __import__(modname)

	print("file    :%s" %  module.__file__)
	print("name    :%s" %  module.__name__)
	print("package :%s" %  module.__package__)

help_table = {
	"modpath" : print_modpath
}

def dump_help():
	print("Usage....")
	print("\tpython 02-help.py modpath <module name>")
	print("\tEx: python 02-help.py modpath boto")
	return -1

def main(argv):
	argc = len(argv)
	if( argc < 3):
		return dump_help()

	help_table[argv[1]](argv[2])
	#import_modules_dynamically()

if (__name__ == "__main__"):
	main(sys.argv)
