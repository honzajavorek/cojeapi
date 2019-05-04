import requests

response = requests.get("https://cojeapi.honzajavorek.now.sh/movies")
movies = response.json()
for movie in movies:
    print(movie['name'])
