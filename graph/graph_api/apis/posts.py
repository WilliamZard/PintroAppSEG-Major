from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (create_session, get_posts_by_user_email, create_post_to_user, 
                        modify_post_of_given_user)

# TODO: enable swagger API spec
# TODO: email validation


api = Namespace('posts', title='Posting related operations')

# Schema representing a post element
class PostSchema(Schema):
    content = fields.Str(required=True)

# Schema representing a relation between a user and a post.
class PostRelationSchema(Schema):
    date = fields.DateTime(required=True)

# Schema used for doc generation
posts = api.model('Posts', {'content': restx_fields.String(required=True, title='The content of the post.')})

post_schema = PostSchema()

#TODO There should be an authorization system to do that.
@api.route('/<string:email>')
@api.produces('application/json')
class Posts(Resource):
    def get(self, email):
        '''Fetch user's post given its email.'''

        with create_session() as session:
            response = session.read_transaction(get_posts_by_user_email, email)
            user = response.single()
            if user:
                # TODO: a lot going on here. See if this can be improved.
                data = dict(user.data()['post'].items())
                return jsonify(post_schema.dump(data))
            return make_response('', 404)