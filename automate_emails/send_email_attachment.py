import yagmail
import time
import os
from datetime import datetime as dt

sender = ''
receiver = ''

subject = ''

content = ["""
This is the content

""", 'attachment_name.txt']

yag = yagmail.SMTP(user=sender, password=os.getenv(''))
yag.send(to=receiver, subject=subject, contents=content)
print("Email sent!")