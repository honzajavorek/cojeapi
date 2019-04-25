import falcon


def get_personal_details():
    return (
        'name: Honza\n' +
        'surname: Javorek\n' +
        'socks_size: 42\n'
    )


class PersonalDetailsResource():

    def on_get(self, request, response):
        response.status = '200 OK'
        response.set_header('Content-Type', 'text/plain')
        response.body = get_personal_details()


app = falcon.API()
app.add_route('/', PersonalDetailsResource())
