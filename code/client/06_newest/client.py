import requests

response = requests.get("https://cojeapi.honzajavorek.now.sh/movies")
movies = response.json()

newest_movie = None
for movie in movies:
    response = requests.get(movie['url'])
    movie_details = response.json()

    if newest_movie is None:
        newest_movie = movie_details
    elif newest_movie['year'] < movie_details['year']:
        newest_movie = movie_details

print('Nejnovější film:', newest_movie['name'], newest_movie['year'])
