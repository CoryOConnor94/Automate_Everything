from twilio.rest import Client

account_sid = ''
account_token = ''

client = Client(account_sid, account_token)

message = client.messages.create(
    body='',
    from_='',
    to=''
)

print(message.sid)