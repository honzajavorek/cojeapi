import json
import falcon


personal_details = {
    'name': 'Honza',
    'surname': 'Javorek',
    'socks_size': '42',
}


class PersonalDetailsResource():

    def on_get(self, request, response):
        response.status = '200 OK'
        response.set_header('Content-Type', 'application/json')
        response.body = json.dumps(personal_details)


app = falcon.API()
app.add_route('/', PersonalDetailsResource())
