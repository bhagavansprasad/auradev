import os
import sys
import json

from os.path import isfile, isdir

def func_exit():
	sys.exit()


#if isfile('a.txt'):
#	print "yes, file exists"
file = "c:\\dd\\gg\\a.txt"
#print os.path.basename(file)
#print os.path.dirname(file)

#func_exit()
#print "don't print this"

f = open ('person.json')
data = json.load(f)
print data[0]['name']
print data[0]['age']
print data[0]['mobiles'][0]
print data[1]['name']





