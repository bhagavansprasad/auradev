import smtplib

server = smtplib.SMTP('localhost')

msg = "This message is from Python Script!"
server.sendmail("bhagavan@foreman.auradev.com", "bhagavan@foreman.auradev.com", msg)
