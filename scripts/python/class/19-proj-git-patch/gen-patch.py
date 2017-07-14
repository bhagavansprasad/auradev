import os
import subprocess

''' 
def get_modified_files(repo_path, output_file):
    cmd = ['hg', 'status', './']
    print "Storing hg status for :", '('+repo_path+')', repo_path+'/'+output_file

    old_dir = os.getcwd()
    os.chdir(repo_path)

    with open(output_file, 'w') as out:
        return_code = subprocess.call(cmd, stdout=out)

    os.chdir(old_dir)

    return repo_path+'/'+output_file


def gen_patch_file(repo_path, file_list):
    #print repo_path, file_list
    with open(file_list) as fd:
        content = fd.readlines()
        create_tar_file(repo_path, content)
''' 


cmd = ['git', 'status', './']
tar_cmd = ['tar', '-rvf' 'patch.tar']
with open("up.txt", 'w') as descriptor:
     return_code = subprocess.call(cmd, stdout=descriptor)

#close(descriptor)

with open("up.txt", 'r') as descriptor:
    file_content = descriptor.readlines()

#print file_content

for row in file_content:
    if (row.find("modified") != -1):
        #print row,
        tar_cmd.append(row.split(':')[1].lstrip().rstrip('\n'))
        print tar_cmd

subprocess.call(tar_cmd)



