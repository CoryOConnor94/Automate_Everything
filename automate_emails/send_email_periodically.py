import yagmail
import time
import os
from datetime import datetime as dt

sender = ''
receiver = ''

subject = ''

content = """

"""

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 30:
        yag = yagmail.SMTP(user=sender, password=os.getenv(''))
        yag.send(to=receiver, subject=subject, contents=content)
        print("Email sent!")
        time.sleep(60)