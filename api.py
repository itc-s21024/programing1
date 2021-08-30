import requests

num = input(int())

url = "https://api.zipaddress.net/?zipcode=(num)"
res = requests.get(url)
data = res.json()


print(data)
