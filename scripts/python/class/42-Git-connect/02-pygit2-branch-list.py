import pygit2

def dump_all_branches(prepo):
    for branch in prepo.references:
        print branch
    

def main():
    repo = pygit2.Repository('/opt/git/amath.git')

    dump_all_branches(repo)

    print "repo.path    :", repo.path
    print "repo.workdir :", repo.workdir

    head = repo.references.get('refs/heads/master')  # Returns None if not found
    #head = repo.references['refs/heads/master']  # Raises KeyError if not found

    for entry in head.log():
        print "",

if __name__ == '__main__':
    main()

