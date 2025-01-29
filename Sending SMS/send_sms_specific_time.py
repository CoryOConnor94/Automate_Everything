from twilio.rest import Client
from datetime import datetime as dt
import time

account_sid = ''
account_token = ''

client = Client(account_sid, account_token)

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 30:
        message = client.messages.create(
            body='',
            from_='',
            to=''
        )

        print(message.sid)
    time.sleep(60)