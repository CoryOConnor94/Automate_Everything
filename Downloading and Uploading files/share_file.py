from filestack import Client

API_KEY = ''

client = Client(API_KEY)

new_link = client.upload(filepath='file.txt')

print(new_link.url)
