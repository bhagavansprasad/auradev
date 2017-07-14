''' 
line = "main.c:36:1: warning: control reaches end of non-void function [-Wreturn-type]"
print line
if (line.find(": warning:") != -1):
    print "Yes"
else:
    print "No"

w1count = 0
w2count = 0

fd = open("1log.txt", "r")
lines = fd.readlines()
fd.close()
#print lines

for line in lines:
    #print line
    if (line.find(": warning:") != -1):
        w1count  += 1
print w1count

fd = open("2log.txt", "r")
lines = fd.readlines()
fd.close()
#print lines

for line in lines:
    #print line
    if (line.find(": warning:") != -1):
        w2count  += 1

print w2count
'''


def get_warning_count_by_filename(log_file_name):
    warn_count = 0

    try:
        fd = open(log_file_name, "r")
    except:
        #print "Open file failed"
        return -1

    lines = fd.readlines()
    fd.close()

    '''
    for line in lines:
        if (line.find(": warning:") != -1):
            warn_count  += 1
    '''
    for i in lines[1:]:
        print lines[i]

    return warn_count


list_of_log_files = ["1log.txt", "2log.txt", "3log.txt", "4log.txt"]
#list_of_log_files = ["1log.txt", "2log.txt"]

#print get_warning_count_by_filename("1log.txt")
#print get_warning_count_by_filename("2log.txt")

for log_file in list_of_log_files:
    print log_file, " ", get_warning_count_by_filename(log_file)
    #get_warning_count_by_filename(log_file)



