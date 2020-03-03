from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (create_session, get_post_by_uuid, create_post_to_user,
                        modify_post_of_given_user, delete_post_of_give_user, get_list_of_user_post_dates)

# TODO: email validation
# TODO: docstrings of functions need updating


api = Namespace('posts', title='Posting related operations')

# TODO: add more fields to post based on specs
# Schema representing a post element


class PostSchema(Schema):
    content = fields.Str(required=True)
    uuid = fields.Str(required=True)
    created = fields.DateTime(required=True)
    modified = fields.DateTime(required=True)

# TODO: look into how relationship propeties should work
# Schema representing a relation between a user and a post.


class POSTEDRelationSchema(Schema):
    created = fields.DateTime(required=True)


# TODO: review this
# Schema used for doc generation
posts = api.model('Post', {
    'content': restx_fields.String(required=True, title='The content of the post.'),
    'uuid': restx_fields.String(required=True),
    'created': restx_fields.DateTime(required=True),
    'modified': restx_fields.DateTime(required=True)
})
"""
update_post_model = api.model('Modifying a post', {'post_id': restx_fields.String(required=True, title='Id of the post that needs to be deleted. '),
                                                   'new_content': restx_fields.String(title='The new content to give to the post')})
delete_post_model = api.model('Deleting a post', {'post_id': restx_fields.String(
    required=True, title='Id of the post that needs to be deleted. ')})"""
post_schema = PostSchema()


@api.route('/<string:uuid>')
@api.produces('application/json')
class Posts(Resource):
    def get(self, uuid):
        '''Fetch a post based on its UUID.'''

        with create_session() as session:
            response = session.read_transaction(get_post_by_uuid, uuid)
            post = response.single()
            if post:
                data = dict(post.data()['post'].items())
                return jsonify(post_schema.dump(data))
            return make_response('', 404)

    @api.doc('update_post')
    @api.response(204, 'Post updated')
    @api.expect(posts)
    def put(self, email):
        '''Fetch user's post given its email.'''

        with create_session() as session:
            response = session.read_transaction(
                modify_post_of_given_user, email, api.payload['post_id'], api.payload['new_content'])
            post = response.single()
            if post:
                return make_response('', 204)
            return make_response('', 404)

    # TODO It will be necessary to have authorization to do that.
    @api.doc('create_post')
    @api.response(204, 'Post created')
    @api.expect(posts)
    def post(self, email):
        '''Create a user's post given its email and the content of the post.'''

        with create_session() as session:
            response = session.read_transaction(
                create_post_to_user, email, api.payload['content'])
            post = response.single()
            if post:
                return dict(post.data()['post'].items())
            return make_response('', 404)

    # TODO It will be necessary to have authorization to do that.
    @api.doc('create_post')
    @api.response(204, 'Post deleted')
    @api.expect(posts)
    def delete(self, email):
        '''Delete a user's post given the user's email and the time when he published the post.'''

        with create_session() as session:
            response = session.read_transaction(
                delete_post_of_give_user, email, api.payload['post_id'])
            content_deleted = response.single()
            # TODO Check wether returning a value in the transaction function is worth it or not.
            if content_deleted:
                return make_response('', 204)
            return make_response('', 404)
