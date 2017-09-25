import pygit2
import re
from datetime import datetime
 
def dump_committer_details(cmtr):
    #'email', 'name', 'offset', 'raw_email', 'raw_name', 'time'] 
    print( "email:%s, name :%s, raw_name :%s, time :%d" % (cmtr.email, cmtr.name, cmtr.raw_name, cmtr.time))
    print ("")

def dump_message_details(entry):
    #__hash__
    #'committer', 'message', 'oid_new', 'oid_old']
    print ("-->Entry details.....")
    print( "message:%s, oid_new :%s, oid_old :%s" % (entry.message, entry.oid_new, entry.oid_old)) 
    print ("")


def print_normal_email(raw_email):
    regex = r'\|[\w.-]+@'
    #print "search -- '%s' -- '%s' " % (regex, raw_email)

    match = re.search(regex, raw_email)
    if match:
        return raw_email[:match.start()]+raw_email[match.end()-1:]

def dump_git_log(entry):
    print ("commit %s"   % (entry.oid_new))
    print ("Author: %s"  % (print_normal_email(entry.committer.email)))
    print ("Date:   %s"  % (datetime.utcfromtimestamp(entry.committer.time).strftime('%a %b %d %H:%M:%S %Y %z')))
    print ""

def main():
    repo = pygit2.Repository('/opt/git/amath.git')
    all_refs = list(repo.references)
    print all_refs

    head = repo.references.get('refs/heads/master')  # Returns None if not found
    #head = repo.references['refs/heads/master']  # Raises KeyError if not found

    for entry in head.log():
        dump_message_details(entry)
        dump_committer_details(entry.committer)
	
    for entry in head.log():
        dump_git_log(entry)
        exit(1)

if __name__ == '__main__':
    main()

