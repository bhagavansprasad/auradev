
def my_open(filename):
    fd = 0

    try:
        fd = open("a.txt", "r")

    #except:
    #except IOError:
    except IOError as err:
        print ("File Open failed errno :%d, message :%s" % (err.errno, err.strerror))
        return -1

fd = my_open("t.txt")


