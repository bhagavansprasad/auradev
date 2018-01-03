import subprocess
import os

repositories = [ 
            ['/App/Applications/CubiTV/', 'application.up', '', ''],
            ['/App/Components/SvEPG/', 'svepg.up', '', ''],
            ['/App/Libraries/QBWidgets/', 'libraries.up', '', ''],
            ['/Files/CubiTV/Reliance/', 'files.up', '', '']
        ]

hg_files_types = [
            ["New      :", '?'],
            ["Modified :", 'M']
        ]

ignore_file_types = [
            ['~', ' '],
            ['.swp', ' '],
            ['.up', ' '],
            ['-bak', ' '],
        ]

cleanup_files = [
            ['patch.tar', ' ']
        ]


def get_modified_files(repo_path, output_file):
    cmd = ['hg', 'status', './']
    print "Storing hg status for :", '('+repo_path+')', repo_path+'/'+output_file

    old_dir = os.getcwd()

    try:
        os.chdir(repo_path)
        print os.getcwd()

        with open(output_file, 'w') as out:
            return_code = subprocess.call(cmd, stdout=out)

        os.chdir(old_dir)
        return repo_path+'/'+output_file

    except OSError:
        print "Invalid directory or path ", repo_path
        print "exiting..."
        os.chdir(old_dir)
        exit(1)

def is_in_ignore_list(file_name):
    for ftype in ignore_file_types:
        if (file_name.rfind(ftype[0]) > 0):
            return 1
    return 0

def create_tar_file(repo_path, content):
    tar_cmd = ['tar', '-rvf', 'patch.tar', ' ']

    for line in content:
        if (is_in_ignore_list(line) > 0):
            continue

        for ftypes in hg_files_types:
            if (line.find(ftypes[1]) != -1):
                tar_cmd[3] = '.' + repo_path + line.strip().lstrip(ftypes[1]).lstrip()
                return_code = subprocess.call(tar_cmd)
                break

def gen_patch_file(repo_path, file_list):
    #print repo_path, file_list
    with open(file_list) as fd:
        content = fd.readlines()
        create_tar_file(repo_path, content)

def list_patching_files(repo_path, file_list):
    #print repo_path, file_list
    with open(file_list) as fd:
        content = fd.readlines()
        for line in content:
            if (is_in_ignore_list(line) > 0):
                continue

        for ftypes in hg_files_types:
            if (line.find(ftypes[1]) != -1):
                print '.' + repo_path + line.strip().lstrip(ftypes[1]).lstrip()
                break

def do_cleanup_before_patch():
    for filename in cleanup_files:
        if os.path.exists(filename[0]):
            os.remove(filename[0])
            print "Removing :", filename[0]
    
#main function
do_cleanup_before_patch()

for entry in repositories:
    entry[2] = get_modified_files(os.getcwd()+entry[0], entry[1])

#for entry in repositories:
    #print entry[0], "--", entry[1], "--", entry[2], entry[3]

for entry in repositories:
    list_patching_files(entry[0], entry[2])

exit(1)
for entry in repositories:
    gen_patch_file(entry[0], entry[2])
#files = [line.split(' ', 1)[1] for line in output.split('\n') if line != '']

