import yagmail
import os
import pandas as pd


sender = ''
receiver = ''

subject = ''


contacts = pd.read_csv('contacts.csv')
print(contacts)
# yag = yagmail.SMTP(user=sender, password=os.getenv(''))
for index, row in contacts.iterrows():
    # print(row['email'])
    content = [f"""
    Hi {row['name']}, you owe {row['amount']} here is your bill{row['filepath']}
    """]
    # yag.send(to=row['email'], subject=subject, contents=content)
    # print("Email sent!")