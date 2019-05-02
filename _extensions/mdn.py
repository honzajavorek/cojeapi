import falcon
from docutils import nodes


MDN_LINK = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/{path}'


def status(name, rawtext, text, lineno, inliner,
           options=None, content=None):
    try:
        code = int(text)
        if code < 100 or code >= 600:
            raise ValueError
        name = getattr(falcon, 'HTTP_' + text)

    except (ValueError, AttributeError):
        message = "Invalid HTTP status code: '{}'".format(text)
        error = inliner.reporter.error(message, line=lineno)
        problematic = inliner.problematic(rawtext, rawtext, error)
        return [problematic], [error]

    url = MDN_LINK.format(path='Status/' + text)
    node = nodes.reference(rawtext, name, refuri=url, **(options or {}))
    return [node], []


def header(name, rawtext, text, lineno, inliner,
           options=None, content=None):
    url = MDN_LINK.format(path='Headers/' + text)
    node = nodes.reference(rawtext, text, refuri=url, **(options or {}))
    return [node], []


def method(name, rawtext, text, lineno, inliner,
           options=None, content=None):
    name = text.upper()
    url = MDN_LINK.format(path='Methods/' + name)
    node = nodes.reference(rawtext, name, refuri=url, **(options or {}))
    return [node], []


def setup(app):
    app.add_role('status', status)
    app.add_role('header', header)
    app.add_role('method', method)
    return {'version': '1.0', 'parallel_read_safe': True}
