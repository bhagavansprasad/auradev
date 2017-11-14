import git, os, shutil
 
DIR_NAME = "temp"
git_repository_url = "/opt/git/amath.git"
 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME)
 
os.mkdir(DIR_NAME)
 
repo = git.Repo.init(DIR_NAME)
origin = repo.create_remote('origin', git_repository_url)

origin.fetch()

#print "origin.refs    :", origin.refs
#print "origin.refs[0] :", origin.refs[0]
#print "origin.refs[0].remote_head :", origin.refs[0].remote_head


origin.pull(origin.refs[0].remote_head)
print repo.head.reference.log()
 
