import json
import sys
from datetime import datetime
import pygit2
sys.path.append('/home/bhagavan/training/scripts/python/class/05-Utilities')
import dumphelp
 
 
def main():
	repo = pygit2.Repository('/opt/git/amath.git')
	all_refs = list(repo.references)
	print all_refs

	head = repo.references.get('refs/heads/master')  # Returns None if not found
	#head = repo.references['refs/heads/master']  # Raises KeyError if not found
	for entry in head.log():
		print(entry.message)
		print(entry.committer.email)
		print(entry.committer.name)
		print(entry.committer.offset)
		print(entry.committer.time)
	
	print dir(entry)
	print dir(entry.committer)

	exit(1)

	master_ref = repo.lookup_reference("refs/heads/master")
	print master_ref
	print dir(master_ref)

	commit = master_ref.get_object() # or repo[master_ref.target]
	print commit

if __name__ == '__main__':
    main()

