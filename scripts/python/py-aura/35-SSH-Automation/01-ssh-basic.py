from pexpect import pxssh


def simple_login(hostip, uname, passwd):
    s = pxssh.pxssh()
    s.login (hostip, uname, passwd)
    print ("SSH session login successful")
    s.sendline ('ls -l')
    s.prompt()         # match the prompt
    #print(s.before)     # print everything before the prompt.
    print(type(s.before))
    data = str(s.before)
    print (data)
    if (data.find("a.out") > 0):
        print ("Found")
    else:
        print ("NOT Found")
        return

    #extract new cmd from above results
    newcmd = "a.out"
    s.sendline (newcmd)
    s.prompt() 
    print(s.before)

    s.logout()

def simple_login_error_handle(hostip, uname, passwd):
    s = pxssh.pxssh()

    try:
        if not s.login (hostip, uname, passwd):
            print ("SSH session failed on login.")
            print((str(s)))
        else:
            print ("SSH session login successful")
            s.sendline ('ls -l')
            s.prompt()    
            print(s.before)
            s.logout()
    except:
        print ("Got exception")
        print ("SSH session failed on login.")
        print(str(s))

def ssh_interactive_exception_handle(hostip, uname, passwd):
    try:
        s = pxssh.pxssh()
        s.force_password = True
        s.login (hostip, uname, passwd)
        s.sendline ('uptime') # run a command
        s.prompt() # match the prompt
        print(s.before, s.after)
        s.interact()

    except pxssh.ExceptionPxssh as e:
        print('pxssh failed on login.')
        print(str(e))

    except OSError:
        print("End session to " + user + "@" + host)

if (__name__ == "__main__"):
    #simple_login("localhost", "auradev", "jnjnuh")
    #simple_login_error_handle("localhost", "auradev", "jnjnuh")
    #ssh_interactive_exception_handle("localhost", "auradev", "jnjnuh")
    
