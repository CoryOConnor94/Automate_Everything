import smtpd
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = ''
receiver = ''
password = os.getenv('PASSWORD')

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again'

body = """
<h2>Hi there!</h2>
This is a message
"""
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

server = smtpd.SMTP('smtp.office365.com')
server.starttls()
server.login(sender, password)
message_text = message.as_string()
server.sendmail(sender, receiver, message_text)
server.quit()