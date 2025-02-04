import requests
import json

url = "https://api.languagetool.org/v2/check"
params = {
    "text":"Tis is a nixe day!",
    "language":"auto"
}

response = requests.post(url, params=params)
result = json.loads(response.text)
print(result)