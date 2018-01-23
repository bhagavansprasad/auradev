import pygit2
repo = pygit2.Repository('/opt/git/amath.git' )

print repo.path
print repo.workdir
print repo.status()
print dir(repo)

exit(1)
commit = repo.revparse_single('23d01f29337d4e47e5214ed5ad86f0945f5ac9ce')   # equivalent to repo[u'042bb9b5']
print commit.hex
print commit.message
print commit.author.email    # clearly I'm editing out author info
print commit.author.name
print commit.author.offset
print commit.author.time    # epoch time
