import requests

response = requests.get("https://cojeapi.honzajavorek.now.sh/movies")
movies_list = response.json()

movies = []
for movie_item in movies_list:
    response = requests.get(movie_item['url'])
    movie = response.json()
    movies.append(movie)

print('Seznam filmů:')
for movie in movies:
    print(movie['name'])

print('')

print('Nejnovější film:')
newest_movie = movies[0]
for movie in movies:
    if movie['year'] > newest_movie['year']:
        newest_movie = movie
print(newest_movie['name'], newest_movie['year'])
