from flask import Flask


class FlaskEngine(Flask):
    def __init__(self, configuration):
        super().__init__(__name__)

        self.config = configuration

    def register_blueprint(self, *args, **kwargs):
        self.register_blueprint(*args, **kwargs)

    def run(self, *args, **kwargs):
        conf = self.config.copy()
        for k, v in kwargs.items():
            conf[k] = v

        super().run(*args, **conf)