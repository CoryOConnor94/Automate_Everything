import yagmail
import os
import pandas as pd


sender = ''
receiver = ''

subject = ''


contacts = pd.read_csv('contacts.csv')
print(contacts)
# yag = yagmail.SMTP(user=sender, password=os.getenv(''))


def generate_file(filename, content):
    with open(filename, 'w') as f:
        f.write(str(content))


for index, row in contacts.iterrows():
    file_name = row['name'] + '.txt'
    generate_file(file_name, row['amount'])

    content = [f"""
    Hi {row['name']}, you owe {row['amount']} here is your bill
    """, file_name]
    # yag.send(to=receiver, subject=subject, contents=content)
    # print("Email sent!")

