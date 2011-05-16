"""
Override tiddlyweb.web.util:server_host_url so that it
attends to HTTP_HOST in the environ. This allows one
TiddlyWeb server to operate on multiple named virtual
hosts.

See also http://tiddlyweb.com/ and http://github.com/tiddlyweb

"""

import tiddlyweb.web.util


original_server_host_url = tiddlyweb.web.util.server_host_url


def virtual_server_host_url(environ):
    """
    Replace server_host_url with a method that is HTTP_HOST aware.
    """
    http_host = environ.get('HTTP_HOST')
    if http_host:
        return '%s://%s' % (environ['wsgi.url_scheme'], http_host)
    else:
        return original_server_host_url(environ)


tiddlyweb.web.util.server_host_url = virtual_server_host_url


def init(config):
    """
    Required for plugin initialization.
    """
    pass
