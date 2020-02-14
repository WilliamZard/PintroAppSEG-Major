from flask import Flask
from apis import api
import config
import os

app = Flask(__name__)
if os.environ['ENV'] == 'prod':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

api.init_app(app)
app.run(host='0.0.0.0', port=8080)
