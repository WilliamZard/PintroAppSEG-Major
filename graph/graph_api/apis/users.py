from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (create_session, create_user, delete_user_by_email,
                        get_user_by_email, set_user_fields)

# TODO: enable swagger API spec
# TODO: email validation


api = Namespace('users', title='User related operations')

# Schema used for serialisations


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


# Schema used for doc generation
users = api.model('Users', {
    'email': restx_fields.String(required=True, title='The user email.'),
    'password': restx_fields.String(required=True, title='The user password.'),
    'full_name': restx_fields.String(required=True, title='The user full name.'),
    'preferred_name': restx_fields.String(title='The user preferred name.'),
    'profile_image': restx_fields.String(title='image saved as array of Bytes representing the user\'s profile pic.'),
    'phone': restx_fields.String(title="The user's phone number."),
    'gender': restx_fields.String(title="The User's geneder"),
    'job_title': restx_fields.String(title='current job title of the user.'),
    'location': restx_fields.String(title='current city of the user.'),
    'short_bio': restx_fields.String(title='short bio describing the user of maximum 250 characters.'),
    'story': restx_fields.String(title='story describing the user of maximum 250 words.'),
    'education': restx_fields.String(title='Highest level obtained.')
})  # title for accounts that needs to be created.

user_schema = UserSchema()


@api.route('/<string:email>')
@api.produces('application/json')
@api.expect(users)
class Users(Resource):
    def get(self, email):
        '''Fetch a user given its email.'''
        if not valid_email(email):
            return make_response(jsonify({}), 422)
        with create_session() as session:
            response = session.read_transaction(get_user_by_email, email)
            user = response.single()
            if user:
                # TODO: a lot going on here. See if this can be improved.
                data = dict(user.data()['user'].items())
                return jsonify(user_schema.dump(data))
            return make_response(jsonify({}), 404)

    @api.doc('delete_user')
    @api.response(204, 'User Deleted')
    def delete(self, email):
        '''Delete a user given its email.'''
        with create_session() as session:
            response = session.read_transaction(delete_user_by_email, email)
            # TODO: not sure how to handle neo4j response for this yet
            user = response.single()
            if user:
                return user, 204
            return "User not found", 404

    @api.doc('update_user')
    @api.response(204, 'User Fields Deleted')
    def put(self, email):
        '''Update a user by the given fields.'''
        # TODO: validate payload
        with create_session() as session:
            response = session.write_transaction(
                set_user_fields, email, api.payload)
            if response:
                return 204
            return "User was not found", 404


@api.route('/')
@api.produces('application/json')
@api.expect(users)
class UsersPost(Resource):
    @api.doc('create_user')
    @api.response(204, 'User created')
    @api.response(409, 'User with that email already exists')
    def post(self):
        '''Create a user.'''
        with create_session() as session:
            try:
                response = session.write_transaction(create_user, api.payload)
            except ConstraintError as e:
                return str(e), 409
            else:
                return 'User created', 204
