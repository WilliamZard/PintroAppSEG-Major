from flask import Flask, Config
from apis.users import users
#from graph_api.config import ProductionConfig, DevelopmentConfig
import os


def create_app():
    app = Flask(__name__)
    app.register_blueprint(users)
    return app
