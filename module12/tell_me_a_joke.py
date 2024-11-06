import requests

res = requests.get('https://api.chucknorris.io/jokes/random')
print(res.json()['value'])