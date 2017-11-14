import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

emailfrom = "bhagavan@foreman.auradev.com"  
emailto = "bhagavan@foreman.auradev.com"
fileToSend = "t.txt"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "Sending attachment with mail"
msg.preamble = "mail with attachment"

ctype, encoding = mimetypes.guess_type(fileToSend)
print ctype
print encoding

if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()

attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)

server = smtplib.SMTP("localhost")
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()
