# Module: f2.py
# Example 1: functions to store and retrieve global variables

gMyVar = 0

def print_world():
    print "World!"

def get_gMyVar():
    return gMyVar # no need for global statement 

def inc_gMyVar():
    global gMyVar
    gMyVar += 1 
