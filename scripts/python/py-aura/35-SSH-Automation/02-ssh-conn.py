import os
import sys
import getopt
import getpass
import pxssh

try:
    raw_input
except NameError:
    raw_input = input

def check_file(hostip, uname, passwd):
	p = pxssh.pxssh()
	if not p.login (hostip, uname, (hostip, uname, passwd):
		print ("SSH session failed on login.")
		print((str(s)))
	else:
		p.sendline('ls -l')
		p.expect(r'5-use-mod-with-path')
		p.prompt() 
		print(p.before)
		print(p.match.groups())
		p.logout()
	 	#print(requests_per_second)

def exit_with_usage():
    print ("")

def main():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'h?s:u:p:', ['help','h','?'])
    except Exception as e:
        print(str(e))
        exit_with_usage()
    options = dict(optlist)
    if len(args) > 1:
        exit_with_usage()

    if [elem for elem in opt passwd):
		print ("SSH session failed on login.")
		print((str(s)))
	else:
		p.sendline('ls -l')
		p.expect(r'5-use-mod-with-path')
		p.prompt() 
		print(p.before)
		print(p.match.groups())
		p.logout()
	 	#print(requests_per_second)

def exit_with_usage():
    print ("")

def main():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'h?s:u:p:', ['help','h','?'])
    except Exception as e:
        print(str(e))
        exit_with_usage()
    options = dict(optlist)
    if len(args) > 1:
        exit_with_usage()

    if [elem for elem in options if elem in ['-h','--h','-?','--?','--help']]:
        print("Help:")
        exit_with_usage()

    if '-s' in options:
        hostname = options['-s']
    else:
        hostname = raw_input('hostname: ')
    if '-u' in options:
        username = options['-u']
    else:
        username = raw_input('username: ')
    if '-p' in options:
        password = options['-p']
    else:
        password = getpass.getpass('password: ')

    check_file(hostname, username, password)

if __name__ == "__main__":
    main()
