from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (create_session, get_posts_for_timeline)

# TODO: enable swagger API spec
# TODO: email validation


api = Namespace('followings', title='Followings related operations')

# Schema used for serializations for user nodes
class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    full_name = fields.Str(required=True)
    preferred_name = fields.String()
    profile_image = fields.String()
    phone = fields.String()
    gender = fields.String()
    job_title = fields.String()
    location = fields.String()
    short_bio = fields.String()
    story = fields.String()
    education = fields.String()

# Schema used for serialization for user nodes
class PostSchema(Schema):
    content = fields.Str(required=True)

user_schema = UserSchema()
post_schema = PostSchema()

@api.route('/posts/<string:email>')
@api.produces('application/json')
class FollowingPosts(Resource):
    def get(self, email):
        '''Fetch a user given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(get_posts_for_timeline, email)
            posts = response.records()
            if posts:
                data = []
                for post in posts:
                    print(post)
                    # TODO: a lot going on here. See if this can be improved.
                    extracted_post = dict(post.data()['post'].items())
                    formatted_post = post_schema.dump(extracted_post)
                    data.append(formatted_post)
                print(data)
                return data
            return make_response('', 404)