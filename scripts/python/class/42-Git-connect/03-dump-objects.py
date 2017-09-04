"""
Writes all the tags and commits from a repository to JSON
"""
 
import base64
import json
import sys
from datetime import datetime
import pygit2

def main(repository):
    repo = pygit2.Repository(repository)
 
    objects = {
        'tags': [],
        'commits': [],
    }
 
    print "COMMIT :", pygit2.GIT_OBJ_COMMIT
    print "TAG    :", pygit2.GIT_OBJ_TAG
    for objhex in repo:
        obj = repo[objhex]
        if (obj.type == pygit2.GIT_OBJ_COMMIT):
            objects['commits'].append({
                'hash': obj.hex,
                'message': obj.message,
                'commit_date': datetime.utcfromtimestamp(
                    obj.commit_time).strftime('%Y-%m-%dT%H:%M:%SZ'),
                'author_name': obj.author.name,
                'author_email': obj.author.email,
                'parents': [c.hex for c in obj.parents],
            })
        elif obj.type == pygit2.GIT_OBJ_TAG:
            objects['tags'].append({
                'hex': obj.hex,
                'name': obj.name,
                'message': obj.message,
                #'target': base64.b16encode(obj.target).lower(),
                'tagger_name': obj.tagger.name,
                'tagger_email': obj.tagger.email,
            })
        else:
            # ignore blobs and trees
            pass
 
    print(json.dumps(objects, indent=2))
 
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("USAGE {0} <repository>".format(__file__))
        sys.exit(1)
 
    main(sys.argv[1])
