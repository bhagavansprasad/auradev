import os    

def list_all(dirname):
    print(("%-20s" % ("File-Name")))
    for basename in os.listdir(dirname):
        print(("%-20s" % (basename)))
    print("")

def list_files(dirname):
    print(dirname)
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            print(basename)
    print("")

def list_dirs(dirname):
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isdir(filename):
            print(basename)
    print("")

def get_files_with_size(dirname):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    basenames = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        #filename = basename
        if os.path.isfile(filename):
            filepaths.append(filename)
            basenames.append(basename)

    # Re-populate list with filename, size tuples
    for i in range(len(filepaths)):
        filepaths[i] = (basenames[i], os.path.getsize(filepaths[i]))

    print("%-40s %5s" % ("File name", "Size"))
    for fname in filepaths:
        print(("%-40s %5d" % (fname[0], fname[1])))

    print("")

def get_n_list_files_by_file_size(dirname, reverse=False):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    basenames = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        #filename = basename
        if os.path.isfile(filename):
            filepaths.append(filename)
            basenames.append(basename)

    # Re-populate list with filename, size tuples
    for i in range(len(filepaths)):
        #filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))
        filepaths[i] = (basenames[i], os.path.getsize(filepaths[i]))


    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in range(len(filepaths)):
        filepaths[i] = filepaths[i][0]

    print(("%-20s" % ("File name")))
    for fname in filepaths:
        #print("%-20s" % (fname))
        print(("%-40s %5d" % (fname[0], fname[1])))

    print("")
    return filepaths

def main():
	dirname = "/home/bhagavan/training/scripts/python/py-aura/16-PgSQL"
	list_all(dirname)
	list_files(dirname)
	list_dirs(dirname)
	get_files_with_size(dirname)
	return

if (__name__ == '__main__'):
	main()
