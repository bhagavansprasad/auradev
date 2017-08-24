import smtplib

textfile = "t.txt"

from email.mime.text import MIMEText
with open(textfile) as fp:
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = "pyscript@foreman.auradev.com"
msg['To'] = "bhagavan@foreman.auradev.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
print dir(s)
s.sendmail("bhagavan@foreman.auradev.com", "bhagavan@foreman.auradev.com", msg)
s.quit()
