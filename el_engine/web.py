from flask import Flask, Blueprint


class FlaskEngine():
    def __init__(self, configuration):
        self.app = Flask(__name__)

        self.config = configuration

    def register_blueprint(self, *args, **kwargs):
        self.app.register_blueprint(*args, **kwargs)

    def run(self, *args, **kwargs):
        conf = self.config.copy()
        for k, v in kwargs.items():
            conf[k] = v

        self.app.run(*args, **conf)


class SingleWebPage:
    def __init__(self, name=None, route_path=None, description=None, *args, **kwargs):
        self.name = name
        self.route_path = route_path
        self.description = description

        if "name" in kwargs.keys(): self.name = kwargs['name']; del kwargs['name']
        if "route" in kwargs.keys(): self.name = kwargs['route']; del kwargs['route']
        if "description" in kwargs.keys(): self.name = kwargs['description']; del kwargs['description']

        self.bp = Blueprint(name, __name__, *args, **kwargs)

    def extract(self):
        return self.bp
