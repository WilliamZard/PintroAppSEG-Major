import uuid
from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (create_session, get_post_by_uuid,
                        set_post_fields, delete_post_of_give_user, get_list_of_user_post_dates, create_post)
import datetime

# TODO: email validation
# TODO: docstrings of functions need updating


api = Namespace('posts', title='Posting related operations')

# TODO: add more fields to post based on specs
# Schema representing a post element


class PostSchema(Schema):
    content = fields.Str(required=True)
    uuid = fields.Str()
    created = fields.DateTime()
    modified = fields.DateTime()
    user_email = fields.Email()

# TODO: look into how relationship propeties should work
# Schema representing a relation between a user and a post.


"""
class POSTEDRelationSchema(Schema):
    created = fields.DateTime(required=True)
"""

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
                return jsonify(data)
            return make_response('', 404)

    @api.doc('update_post')
    @api.response(204, 'Post updated')
    @api.expect(posts)
    def put(self, uuid):
        '''Update a Post's content.'''

        with create_session() as session:
            response = session.write_transaction(
                set_post_fields, uuid, api.payload)
            if response.summary().counters.properties_set == 1:
                return make_response('', 204)
            return make_response('', 404)

    # TODO It will be necessary to have authorization to do that.
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


@api.route('/')
@api.produces('application/json')
@api.expect(posts)
class UsersPost(Resource):
    @api.doc('create_post')
    @api.response(204, 'Post created')
    def post(self):
        '''Create a post.'''
        print('\n')
        print(api.payload)
        print(post_schema.load(api.payload))
        try:
            deserialised_payload = post_schema.load(api.payload)
        except ValidationError as e:
            return make_response(e, 422)
        created = modified = str(datetime.datetime.now())
        post_uuid = uuid.uuid4()
        content = deserialised_payload['content']
        user_email = deserialised_payload['user_email']
        with create_session() as session:
            try:
                response = session.write_transaction(
                    create_post, content, user_email,
                    created, modified, post_uuid)
                if response.summary().counters.nodes_created == 1:
                    return make_response('', 201)
            except ConstraintError:
                return make_response('Node with that email already exists.', 409)
