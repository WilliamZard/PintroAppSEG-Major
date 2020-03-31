from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email
from .posts import posts

from .neo4j_ops import (create_session, create_user, delete_user_by_email,
                        get_user_by_email, set_user_fields, get_followers_of_a_user, get_followings_of_a_user, get_posts_of_followings_of_a_user)

# TODO: enable swagger API spec
# TODO: email validation


api = Namespace('users', title='User related operations')

# Schema used for serialisations


class UserSchema(Schema):
    full_name = fields.Str(required=True)
    preferred_name = fields.String()
    profile_image = fields.String()
    short_bio = fields.String()
    gender = fields.String()
    story = fields.String()
    email = fields.Email(required=True)
    phone_number = fields.String()
    job_title = fields.String()
    current_company = fields.String()
    years_in_industry = fields.Int()
    industry = fields.String()
    previous_company = fields.String()
    previous_company_year_finished = fields.String()
    university = fields.String()
    university_year_finished = fields.Int()
    academic_level = fields.String()
    date_of_birth = fields.String()
    location = fields.String()
    passions = fields.List(fields.String())
    help_others = fields.List(fields.String())
    active = fields.String()


# TODO: update model with new schema
# Schema used for doc generation
users = api.model('Users', {
    'full_name': restx_fields.String(required=True, title='The user full name.'),
    'preferred_name': restx_fields.String(title='The user preferred name.'),
    'profile_image': restx_fields.String(title='image saved as array of Bytes representing the user\'s profile pic.'),
    'short_bio': restx_fields.String(title='short bio describing the user of maximum 250 characters.'),
    'gender': restx_fields.String(title="The User's geneder"),
    'story': restx_fields.String(title='story describing the user of maximum 250 words.'),
    'email': restx_fields.String(required=True, title='The user email.'),
    'phone_number': restx_fields.String(title="The user's phone number."),
    'job_title': restx_fields.String(title='current job title of the user.'),
    'current_company': restx_fields.String(),
    'years_in_industry': restx_fields.String(),
    'industry': restx_fields.String(),
    'previous_company': restx_fields.String(),
    'previous_company_year_finished': restx_fields.String(),
    'university': restx_fields.String(),
    'university_year_finished': restx_fields.String(),
    'academic_level': restx_fields.String(),
    'date_of_birth': restx_fields.String(),
    'location': restx_fields.String(title='current city of the user.'),
    'passions': restx_fields.List(restx_fields.String(), description='List of Passion Tag UUIDs'),
    'help_others': restx_fields.List(restx_fields.String(), description='List of skill Tag UUIDs that user is offering'),
    'active': restx_fields.String(title='DO NOT TOUCH, whether user is active or not.')
})  # title for accounts that needs to be created.

user_schema = UserSchema()


@api.route('/<string:email>')
@api.produces('application/json')
class Users(Resource):
    def get(self, email):
        '''Fetch a user given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(get_user_by_email, email)
            response = response.single()
            if response:
                user = dict(response.data()['user'].items())
                return jsonify(**user)
            return make_response('', 404)

    @api.doc('delete_user')
    @api.response(204, 'User deleted.')
    def delete(self, email):
        '''Delete a user given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.write_transaction(delete_user_by_email, email)
            # >= because post nodes of user may have been deleted
            if response.summary().counters.nodes_deleted >= 1:
                return make_response('', 204)
            return make_response('', 404)

    @api.doc('update_user')
    @api.response(204, 'User Fields Deleted')
    @api.expect(users)
    def put(self, email):
        '''Update a user by the given fields.'''
        if not valid_email(email):
            return make_response('', 422)

        # TODO: validate payload
        with create_session() as session:
            response = session.write_transaction(
                set_user_fields, email, api.payload)
            if response.summary().counters.properties_set == len(api.payload):
                return make_response('', 204)
            return make_response('', 404)


@api.route('/')
@api.produces('application/json')
@api.expect(users)
class UsersPost(Resource):
    @api.doc('create_user')
    @api.response(422, 'Invalid Email')
    @api.response(201, 'User created')
    @api.response(409, 'User with that email already exists')
    def post(self):
        '''Create a user.'''
        try:
            deserialised_payload = user_schema.load(api.payload)
        except ValidationError as e:
            if 'email' in e.messages:
                return make_response(e.messages['email'][0], 422)
            if 'tags' in e.messages:
                return make_response(e.messages['tags'][0], 422)
            return make_response(e.messages, 422)
        with create_session() as session:
            try:
                response = session.write_transaction(
                    create_user, deserialised_payload)
                if response.summary().counters.nodes_created == 1:
                    return make_response('', 201)
            except ConstraintError:
                return make_response('Node with that email already exists.', 409)


@api.route('/<string:email>/followers')
@api.produces('application/json')
class UsersGETFollowers(Resource):
    @api.doc('get followers of a user')
    def get(self, email):
        '''Get followers of a user'''
        with create_session() as session:
            response = session.read_transaction(
                get_followers_of_a_user, email)
            data = response.data()
            if data:
                return jsonify(data)
            return make_response('', 404)


@api.route('/<string:email>/followings')
@api.produces('application/json')
class UsersGETFollowings(Resource):
    @api.doc('Get the users that the given user is following')
    def get(self, email):
        '''Get the users that the given user is following'''
        with create_session() as session:
            response = session.read_transaction(
                get_followings_of_a_user, email)
            data = response.data()
            if data:
                return jsonify(data)
            return make_response('', 404)


@api.route('/<string:email>/followings/posts')
@api.produces('application/json')
class UsersGETPostsOfFollowings(Resource):
    @api.doc('Get the posts of users the given user follows.')
    def get(self, email):
        '''Get the posts of users the given user follows.'''
        with create_session() as session:
            response = session.read_transaction(
                get_posts_of_followings_of_a_user, email)
            data = response.data()

            # Adjusting different in datetime format. Should not be like this.
            for post in data:
                for key in post:
                    if key in ['created', 'modified']:
                        post[key] = str(post[key]).replace('+00:00', 'Z')
            if data:
                return jsonify(data)
            return make_response('', 404)


@api.route('/deactivate/<string:email>')
@api.produces('application/json')
class Users(Resource):
    @api.doc('deactivate users')
    @api.response(204, 'User deactivated.')
    def put(self, email):
        '''Deactivate a user account.'''
        if not valid_email(email):
            return make_response('', 422)
        fields = {'active': False}
        # TODO: validate payload
        with create_session() as session:
            response = session.write_transaction(
                set_user_fields, email, fields)
            if response.summary().counters.properties_set == 1:
                return make_response('', 204)
            return make_response('', 404)


@api.route('/activate/<string:email>')
@api.produces('application/json')
class Users(Resource):
    @api.doc('activate users')
    @api.response(204, 'User activated.')
    def put(self, email):
        '''Activate a user account if it has been deactivated.'''
        if not valid_email(email):
            return make_response('', 422)
        fields = {'active': True}
        # TODO: validate payload
        with create_session() as session:
            response = session.write_transaction(
                set_user_fields, email, fields)
            if response.summary().counters.properties_set == 1:
                return make_response('', 204)
            return make_response('', 404)
