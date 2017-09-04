import json
import sys
from datetime import datetime
import pygit2
sys.path.append('/home/bhagavan/training/scripts/python/class/05-Utilities')
import dumphelp
 
#repo = pygit2.Repository('/opt/git/amath.git')
 
def main(repository):
    #repo = pygit2.Repository(repository)
    repo = pygit2.Repository('/opt/git/amath.git')

    dumphelp.dump_object_help(repo)
    print "head :", dir(repo.head)
    print "walk :", dir(repo.walk)
    exit(1)
    print "head :", dir(repo.head.log)
    print "head :", dir(repo.head.name)
    print "head :", repo.head.name

 
    commits = []
 
    for commit in repo.walk(repo.head.oid_new, pygit2.GIT_SORT_TIME):
        commits.append({
            'hash': commit.hex,
            'message': commit.message,
            'commit_date': datetime.utcfromtimestamp(
                commit.commit_time).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'author_name': commit.author.name,
            'author_email': commit.author.email,
            'parents': [c.hex for c in commit.parents],
        })
 
    print(json.dumps(commits, indent=2))
    exit(1)
 
 
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("USAGE: {0} <repository>".format(__file__))
        sys.exit(0)
 
    main(sys.argv[1])
