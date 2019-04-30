import json
import falcon


personal_details = {
    'name': 'Honza',
    'surname': 'Javorek',
    'socks_size': '42',
}


class PersonalDetailsResource():

    def on_get(self, request, response):
        response.body = json.dumps(personal_details)


movies = [
    {'name': 'The Last Boy Scout', 'year': 1991},
    {'name': 'Mies vailla menneisyyttä', 'year': 2002},
    {'name': 'Sharknado', 'year': 2013},
    {'name': 'Mega Shark vs. Giant Octopus', 'year': 2009},
]


def filter_movies(movies, name):
    if name is not None:
        return [movie for movie in movies if name in movie['name'].lower()]
    else:
        return movies


class MoviesResource():

    def on_get(self, request, response):
        name = request.get_param('name')
        response.body = json.dumps(filter_movies(movies, name))


app = falcon.API()
app.add_route('/', PersonalDetailsResource())
app.add_route('/movies', MoviesResource())
