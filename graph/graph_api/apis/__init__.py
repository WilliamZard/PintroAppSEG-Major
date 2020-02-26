from flask_restx import Api
from .users import api as users
from .posts import api as posts

api = Api(
    title='Pintro Graph Api',
    version='0.1',
    # TODO: there are other parameters to put here that could be useful
)

api.add_namespace(users)
api.add_namespace(posts)
