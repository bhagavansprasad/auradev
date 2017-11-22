import git
#repo = git.Repo( 'git@192.168.1.254:/opt/git/auradev.git' )
repo = git.Repo( '/opt/git/amath.git' )
print repo.git.status()
# checkout and track a remote branch
#print repo.git.checkout( 'origin/master', b='master' )
# add a file
#print repo.git.add( 'somefile' )
# commit
#print repo.git.commit( m='my commit message' )
# now we are one commit ahead
#print repo.git.status()
#repo = GitRepo('/git/manifest.git')
#data = repo.head.commit.tree[filename].data_stream.read()

