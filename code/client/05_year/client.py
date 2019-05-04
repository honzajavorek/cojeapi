import requests

response = requests.get("https://cojeapi.honzajavorek.now.sh/movies")
movies = response.json()

for movie in movies:
    response = requests.get(movie['url'])
    movie_details = response.json()
    print(movie_details['name'], movie_details['year'])
