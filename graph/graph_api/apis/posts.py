from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (create_session, get_posts_by_user_email, create_post_to_user, 
                        modify_post_of_given_user, get_list_of_user_post_dates)

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
post_model = api.model('Post', {'content': restx_fields.String(required=True, title='The content of the post.')})
update_post_model = api.model('Posts', {'post_date': restx_fields.String(required=True, title='The content of the post before updating it.'),
                                        'new_content': restx_fields.String(required=True, title='The new content to give to the post')})

post_schema = PostSchema()

#TODO There should be an authorization system to do that.
@api.route('/<string:email>')
@api.produces('application/json')
class Posts(Resource):
    def get(self, email):
        '''Fetch user's post given its email.'''

        with create_session() as session:
            response = session.read_transaction(get_posts_by_user_email, email)
            posts = response.records()
            if posts:
                data = []
                for post in posts:
                    # TODO: a lot going on here. See if this can be improved.
                    extracted_post = dict(post.data()['post'].items())
                    formatted_post = post_schema.dump(extracted_post)
                    data.append(formatted_post)
                print(data)
                return data
            return make_response('', 404)

    @api.doc('update_post')
    @api.response(204, 'Post updated')
    @api.expect(update_post_model)
    def put(self, email):
        '''Fetch user's post given its email.'''

        with create_session() as session:
            response = session.read_transaction(modify_post_of_given_user, email, api.payload['post_date'], api.payload['new_content'])
            post = response.single()
            if post:
                return make_response('', 204)
            return make_response('', 404)

    @api.doc('delete_post')#TODO It will be necessary to have authorization to do that.
    @api.response(204, 'Post deleted')
    @api.expect(post_model)
    def post(self, email):
        '''Delete a user's post given its email and the time when he posted it.'''

        with create_session() as session:
            response = session.read_transaction(create_post_to_user, email, api.payload['content'])
            post = response.single()
            if post:
                return make_response('', 204)
            return make_response('', 404)

#Move it to a different folder and then fix test_posts
@api.route('/dates/<email>')
@api.produces('application/json')
class UserPostedRelationship(Resource):
        def get(self, email):
            '''Fetch and get all post dates of a user in ascending order'''
            with create_session() as session:
                response = session.read_transaction(get_list_of_user_post_dates, email)
                dates = response.single()
                if dates:
                    return dates
                return make_response('', 404)