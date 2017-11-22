import pygit2
from pygit2 import Repository

repo = Repository('/opt/git/amath.git')

status = repo.status()
for filepath, flags in status.items():
    if flags != GIT_STATUS_CURRENT:
        print "Filepath %s isn't clean" % filepath

'''
index = repo.index
print index.read()
sha = index['amath/src/amath.c'].sha 
print sha
blob = repo[sha]  
print blob
'''

'''
repo = pygit2.Repository("/opt/git/amath.git")

for commit in repo.walk(sha, GIT_SORT_TIME):
    print commit.sha
'''

'''
from pygit2 import GIT_STATUS_CURRENT
status = repo.status()
for filepath, flags in status.items():
    if flags != GIT_STATUS_CURRENT:
        print "Filepath %s isn't clean" % filepath
'''
