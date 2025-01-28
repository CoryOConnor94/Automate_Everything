import requests

link = 'https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3'

response = requests.get(url=link)
content = response.content
with open('download.mp3', 'wb') as file:
    file.write(content)