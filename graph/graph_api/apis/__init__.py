from flask_restplus import Api
from .users import api as users

api = Api(
    title='Piintro Graph Api',
    version='0.1',
    # TODO: there are other parameters to put here that could be useful
)

api.add_namespace(users)
