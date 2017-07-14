import os
import subprocess

my_cmd = ['git', 'status', './']

subprocess.call(my_cmd)

# git clone git@192.168.1.254:/opt/git/test_repos-1.git
# git clone git@192.168.1.254:/opt/git/test_repos-2.git
# git clone git@192.168.1.254:/opt/git/test_repos-3.git

#To append/add file to "patch.tar"
#tar -rvf patch.tar test_repos-1/1-a/1a.py

#To list files in "patch.tar"
#tar -tvf patch.tar 

#To extract files in "patch.tar"
#tar -xvf patch.tar 
