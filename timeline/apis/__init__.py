from flask_restx import Api
from .timeline import api as timeline

api = Api(
    title='Pintro Timeline API',
    version='0.1',
    # TODO: there are other parameters to put here that could be useful
)

api.add_namespace(timeline)
