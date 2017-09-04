import pygit2
import psycopg2

#To print module path
print dir(pygit2)
print "file",     pygit2.__file__
print "name ",    pygit2.__name__
print "package ", pygit2.__package__
print "path ",    pygit2.__path__
print "version ", pygit2.__version__
print "build   ", pygit2._build 
print "other ",   pygit2._libgit2


print "time",     psycopg2.__file__
