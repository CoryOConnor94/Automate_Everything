import smtpd
import os

sender = ''
receiver = ''
password = os.getenv('PASSWORD')

message = """\
Subject: Hello

This is a message
"""

server = smtpd.SMTP('smtp.office365.com')
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()

