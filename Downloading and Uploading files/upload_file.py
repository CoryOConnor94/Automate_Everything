import requests

url = ''

file = open('', 'rb')

response = requests.post(url=url, files={'':file})