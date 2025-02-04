import smtpd
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from working_with_files.create_empty_files import filename

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

attachment_path = 'contacts.csv'
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=attachment_path)
message.attach(payload)

server = smtpd.SMTP('smtp.office365.com')
server.starttls()
server.login(sender, password)
message_text = message.as_string()
server.sendmail(sender, receiver, message_text)
server.quit()