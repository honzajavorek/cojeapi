import requests

response = requests.get("https://cojeapi.honzajavorek.now.sh/")

print(response.status_code)
print(response.headers)
print(response.json())
