import json
import falcon


personal_details = {
    'name': 'Honza',
    'surname': 'Javorek',
    'socks_size': '42',
}


class PersonalDetailsResource():

    def on_get(self, request, response):
        movies_watchlist_url = '{0}/movies'.format(request.prefix)

        personal_details_repr = dict(personal_details)
        personal_details_repr['movies_watchlist_url'] = movies_watchlist_url

        response.body = json.dumps(personal_details_repr)


movies = [
    {
        'id': 1,
        'name': 'The Last Boy Scout',
        'name_cs': 'Poslední skaut',
        'year': 1991,
        'stars': ['Bruce Willis', 'Damon Wayans', 'Chelsea Field'],
        'imdb_url': 'https://www.imdb.com/title/tt0102266/',
        'csfd_url': 'https://www.csfd.cz/film/8283-posledni-skaut/',
    },
    {
        'id': 2,
        'name': 'Mies vailla menneisyyttä',
        'name_cs': 'Muž bez minulosti',
        'year': 2002,
        'stars': ['Markku Peltola', 'Kati Outinen', 'Juhani Niemelä'],
        'imdb_url': 'https://www.imdb.com/title/tt0311519/',
        'csfd_url': 'https://www.csfd.cz/film/35366-muz-bez-minulosti/',
    },
    {
        'id': 3,
        'name': 'Sharknado',
        'name_cs': 'Žralokonádo',
        'year': 2013,
        'stars': ['Ian Ziering', 'Tara Reid', 'John Heard'],
        'imdb_url': 'https://www.imdb.com/title/tt2724064/',
        'csfd_url': 'https://www.csfd.cz/film/343017-zralokonado/',
    },
    {
        'id': 4,
        'name': 'Mega Shark vs. Giant Octopus',
        'name_cs': 'Megažralok vs. obří chobotnice',
        'year': 2009,
        'stars': ['Debbie Gibson', 'Lorenzo Lamas', 'Vic Chao'],
        'imdb_url': 'https://www.imdb.com/title/tt1350498/',
        'csfd_url': 'https://www.csfd.cz/film/258268-megazralok-vs-obri-chobotnice/',
    },
]


def filter_movies(movies, name):
    if name is not None:
        filtered_movies = []
        for movie in movies:
            if name in movie['name'].lower():
                filtered_movies.append(movie)
        return filtered_movies
    else:
        return movies


def represent_movies(movies, base_url):
    movies_list = []
    for movie in movies:
        movies_list.append({
            'name': movie['name'],
            'url': '{0}/movies/{1}'.format(base_url, movie['id']),
        })
    return movies_list


def create_movie_id(movies):
    ids = []
    for movie in movies:
        ids.append(movie['id'])
    return max(ids) + 1


class MovieListResource():

    def on_get(self, request, response):
        name = request.get_param('name')
        base_url = request.prefix

        filtered_movies = filter_movies(movies, name)
        movies_repr = represent_movies(filtered_movies, base_url)
        response.body = json.dumps(movies_repr)

    def on_post(self, request, response):
        movie = json.load(request.bounded_stream)
        movie['id'] = create_movie_id(movies)
        movies.append(movie)

        movie_url = '{0}/movies/{1}'.format(request.prefix, movie['id'])

        movie_repr = dict(movie)
        movie_repr['url'] = movie_url
        del movie_repr['id']

        response.status = '201 Created'
        response.set_header('Location', movie_url)
        response.body = json.dumps(movie_repr)


def get_movie_by_id(movies, id):
    for movie in movies:
        if movie['id'] == id:
            return movie


def remove_movie_by_id(movies, id):
    for i, movie in enumerate(movies):
        if movie['id'] == id:
            del movies[i]
            return True
    return False


class MovieDetailResource():

    def on_get(self, request, response, id):
        movie = get_movie_by_id(movies, id)
        if movie is None:
            response.status = '404 Not Found'
        else:
            base_url = request.prefix

            movie_repr = dict(movie)
            movie_repr['url'] = '{0}/movies/{1}'.format(base_url, movie['id'])
            del movie_repr['id']

            response.body = json.dumps(movie_repr)

    def on_delete(self, request, response, id):
        movie = get_movie_by_id(movies, id)
        if movie is None:
            response.status = '404 Not Found'
        elif 'Bruce Willis' in movie['stars']:
            response.status = '403 Forbidden'
        else:
            remove_movie_by_id(movies, id)
            response.status = '204 No Content'


app = falcon.API()
app.add_route('/', PersonalDetailsResource())
app.add_route('/movies', MovieListResource())
app.add_route('/movies/{id:int}', MovieDetailResource())
