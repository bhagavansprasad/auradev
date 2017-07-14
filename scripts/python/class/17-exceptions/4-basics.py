# catch all exceptions
try:
    ...
except:

# catch just one exception
try:
    ...
except IOError:
    ...

# catch one exception, but provide the exception object
try:
    ...
except IOError as e:
    ...

# catch more than one exception
try:
    ...
except (IOError, ValueError) as e:
    ...


#It is possible to have more than one except statements with one try.
try:
    ...
except IOError, e:
    print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
    sys.exit(1)
except FormatError, e:
    print >> sys.stderr, "File is badly formatted (%s): %s" % (str(e), filename)

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
finally:
    delete_temp_files()

#Exception is raised using the raised keyword.
raise Exception("error message")


#what is the output
try:
    print "a"
    raise Exception("UDE message")
except:
    print "b"
else:
    print "c"
finally:
    print "d"

#what is the output
try:
    print "a"
except:
    print "b"
else:
    print "c"
finally:
    print "d"


#what is the output
def f():
    try:
        print "a"
        raise Exception("doom")
        return
    except:
        print "b"
    else:
        print "c"
    finally:
        print "d"

f()
