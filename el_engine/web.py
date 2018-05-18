from flask import Flask, Blueprint
from os import urandom


class FlaskEngine:
    def __init__(self, configuration):
        self.app = Flask(__name__)
        self.config = configuration

    def register_blueprint(self, *args, **kwargs):
        self.app.register_blueprint(*args, **kwargs)

    def run(self, *args, **kwargs):
        conf = self.config.copy()
        secret_key = urandom(32)
        for k, v in kwargs.items():
            conf[k] = v

        if "secret_key" in conf.keys():
            secret_key = conf['secret_key']
            del conf['secret_key']

        self.app.secret_key = secret_key
        self.app.run(*args, **conf)


class SingleWebPage:
    def __init__(self,  name=None, route_path=None, description=None, *args, **kwargs):
        self.name = name
        self.route_path = route_path
        self.description = description

        if "name" in kwargs.keys():
            self.name = kwargs['name']
            del kwargs['name']
        if "route_path" in kwargs.keys():
            self.route_path = kwargs['route_path']
            del kwargs['route_path']
        if "description" in kwargs.keys():
            self.description = kwargs['description']
            del kwargs['description']

        self.bp = Blueprint(name, __name__, *args, **kwargs)

    def extract(self):
        return self.bp
