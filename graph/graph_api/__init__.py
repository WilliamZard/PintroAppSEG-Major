from flask import Flask
import os
import logging


def create_app():
    logging.basicConfig(level=logging.DEBUG)
    app = Flask(__name__)

    from .apis import api
    api.init_app(app)
    return app
