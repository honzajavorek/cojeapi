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
        response.status = '200 OK'
        response.set_header('Content-Type', 'application/json')
        response.body = json.dumps(get_personal_details())


app = falcon.API()
app.add_route('/', PersonalDetailsResource())
