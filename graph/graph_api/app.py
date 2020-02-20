from flask import Flask
from apis.users import users
import config
import os

app = Flask(__name__)
if os.environ['ENV'] == 'prod':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

app.register_blueprint(users)
app.run(host='0.0.0.0', port=8080)
