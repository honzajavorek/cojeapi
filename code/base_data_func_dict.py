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
        response.set_header('Content-Type', 'text/plain')

        personal_details = get_personal_details()
        body = ''
        for key, value in personal_details.items():
            body += '{0}: {1}\n'.format(key, value)
        response.body = body


app = falcon.API()
app.add_route('/', PersonalDetailsResource())
