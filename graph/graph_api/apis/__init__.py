from flask_restx import Api
from .users import api as users
from .businesses import api as businesses
from .spaces import api as spaces
from .posts import api as posts
from .tags import api as tags
from .request import api as request
from .approve import api as approve
from .search import api as search
from .chatrooms import api as chatrooms

api = Api(
    title='Pintro Graph Api',
    version='0.1',
    # TODO: there are other parameters to put here that could be useful
)

api.add_namespace(users)
api.add_namespace(businesses)
api.add_namespace(spaces)
api.add_namespace(posts)
api.add_namespace(tags)
api.add_namespace(request)
api.add_namespace(approve)
api.add_namespace(search)
api.add_namespace(chatrooms)
