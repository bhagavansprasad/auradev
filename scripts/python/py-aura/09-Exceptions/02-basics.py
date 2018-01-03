'''
# catch all exceptions
try:
    ...
except:
	...

# catch just one exception
try:
    ...
except IOError:
    ...

# catch one exception and provide the exception object
try:
    ...
except IOError as errobj:
    ...

# catch more than one exception
try:
    ...
except (IOError, ValueError) as errobj:
    ...
'''

'''
#It is possible to have more than one except statements with one try.
try:
    ...
except IOError, errobj:
    print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
    sys.exit(1)
except FormatError, e:
    print >> sys.stderr, "File is badly formatted (%s): %s" % (str(e), filename)
    sys.exit(1)

#except with else
try:
    ...
except IOError, e:
    print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
    sys.exit(1)
else:
    print "successfully opened the file", filename


#except with finally
try:
    ...
except IOError, e:
    print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
    sys.exit(1)
else:
	...
finally:
    delete_temp_files()
	

#Exception is raised using the raised keyword.
raise Exception("error message")
'''


#what is the output
try:
    print(" a")
    raise Exception("UDE message")
except:
    print(" b")
else:
    print(" c")
finally:
    print(" d")

print("")

#what is the output
try:
    print(" a")
except:
    print(" b")
else:
    print(" c")
finally:
    print(" d")

print("")
#what is the output
def f():
    try:
        print(" a")
        raise Exception("doom")
        return
    except TypeError:
        print(" b")
    else:
        print(" c")
    finally:
        print(" d")

f()
exit(1)
