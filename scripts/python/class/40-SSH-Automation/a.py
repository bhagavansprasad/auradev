import socket
import libssh2

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 22))

session = libssh2.Session()
session.startup(sock)
session.userauth_password('bhagavan', 'jnjnuh')

channel = session.channel()
channel.execute('ls -l')

print channel.read(1024)
