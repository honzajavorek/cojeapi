from docutils import nodes


GITHUB_LINK = ('https://github.com/honzajavorek/cojeapi/'
               'blob/master/code/{path}')


def code(name, rawtext, text, lineno, inliner,
         options=None, content=None):
    url = GITHUB_LINK.format(path=text)
    node = nodes.reference(rawtext, text, refuri=url, **(options or {}))
    return [node], []


def setup(app):
    app.add_role('codeexample', code)
    return {'version': '1.0', 'parallel_read_safe': True}
