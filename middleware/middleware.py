from flask import request
from werkzeug.wrappers import Request, Response

class Middleware:
    def __init__(self, app):
        self.app = app
        self.username = 'Wasay'
        self.password = '10pearls'

    def __call__(self, environ, start_response):
        request = Request(environ)
        username = request.authorization['username']
        password = request.authorization['password']

        if username == self.username and password == self.password:
             environ['user'] = { 'name': 'Wasay' }
             return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)