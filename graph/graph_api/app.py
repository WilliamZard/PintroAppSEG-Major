from flask import Flask
import os


def create_app():
    # TODO: use config files instead of env variables in dockerfiles
    app = Flask(__name__)

    from .apis import api
    api.init_app(app)
    return app
