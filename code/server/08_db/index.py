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
    {
        'id': 1,
        'name': 'The Last Boy Scout',
        'name_cs': 'Poslední skaut',
        'year': 1991,
        'imdb_url': 'https://www.imdb.com/title/tt0102266/',
        'csfd_url': 'https://www.csfd.cz/film/8283-posledni-skaut/',
    },
    {
        'id': 2,
        'name': 'Mies vailla menneisyyttä',
        'name_cs': 'Muž bez minulosti',
        'year': 2002,
        'imdb_url': 'https://www.imdb.com/title/tt0311519/',
        'csfd_url': 'https://www.csfd.cz/film/35366-muz-bez-minulosti/',
    },
    {
        'id': 3,
        'name': 'Sharknado',
        'name_cs': 'Žralokonádo',
        'year': 2013,
        'imdb_url': 'https://www.imdb.com/title/tt2724064/',
        'csfd_url': 'https://www.csfd.cz/film/343017-zralokonado/',
    },
    {
        'id': 4,
        'name': 'Mega Shark vs. Giant Octopus',
        'name_cs': 'Megažralok vs. obří chobotnice',
        'year': 2009,
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


class MovieListResource():

    def on_get(self, request, response):
        name = request.get_param('name')
        response.body = json.dumps(filter_movies(movies, name))


app = falcon.API()
app.add_route('/', PersonalDetailsResource())
app.add_route('/movies', MovieListResource())
