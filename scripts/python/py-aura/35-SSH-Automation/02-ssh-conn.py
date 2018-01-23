import sys
from pexpect import pxssh
import getpass

user = 'bhagavan'
password = 'jnjnuh'
host = 'localhost'

try:
    s = pxssh.pxssh()
    s.force_password = True
    s.login (host, user, password, login_timeout=20)
    s.sendline ('uptime') # run a command
    s.prompt() # match the prompt
    print(s.before, s.after)
    s.interact()
except pxssh.ExceptionPxssh as e:
    print('pxssh failed on login.')
    print(str(e))
except OSError:
    print("End session to " + user + "@" + host)
