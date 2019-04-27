import json
import falcon


def get_personal_details():
    return {
        'name': 'Honza',
        'surname': 'Javorek',
        'socks_size': '42',
    }


class PersonalDetailsResource():

    def on_get(self, request, response):
        response.body = json.dumps(get_personal_details())


def get_favorite_movies(name=None):
    movies = [
        {'name': 'The Last Boy Scout', 'year': 1991},
        {'name': 'Mies vailla menneisyyttä', 'year': 2002},
        {'name': 'Sharknado', 'year': 2013},
        {'name': 'Mega Shark vs. Giant Octopus', 'year': 2009},
    ]
    if name is not None:
        filtered_movies = []
        for movie in movies:
            if name in movie['name'].lower():
                filtered_movies.append(movie)
        return filtered_movies
    else:
        return movies


class FavoriteMoviesResource():

    def on_get(self, request, response):
        name = request.get_param('name')
        response.body = json.dumps(get_favorite_movies(name))


app = falcon.API()
app.add_route('/', PersonalDetailsResource())
app.add_route('/movies', FavoriteMoviesResource())
