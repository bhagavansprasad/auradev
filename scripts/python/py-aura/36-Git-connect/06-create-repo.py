from time import time
from pygit2 import Signature
from pygit2 import Repository
from pygit2 import init_repository
from pygit2 import GIT_FILEMODE_BLOB, GIT_FILEMODE_TREE

repo = init_repository('/tmp/repodir', bare=True)

tf1 = repo.create_blob('this is a test file')
tf2 = repo.create_blob('this is a test file2')

tt1 = repo.TreeBuilder()
tt1.insert('test_file1.txt', tf1, GIT_FILEMODE_BLOB)
tt1.insert('test_file2.txt', tf2, GIT_FILEMODE_BLOB)

tt2 = repo.TreeBuilder()

tt2.insert('tt3', tt3.write(), GIT_FILEMODE_TREE)
tt1.insert('tt2', tt2.write(), GIT_FILEMODE_TREE)
precommit = tt1.write()
sig1 = Signature('Tester', 'test@example.com', int(time()), 0)
commit = repo.create_commit('refs/heads/master', sig1, sig1, 'Test commit with pygit2', precommit, [])
