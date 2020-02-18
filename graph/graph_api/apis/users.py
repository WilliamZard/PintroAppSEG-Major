from flask_restx import Namespace, Resource, fields, marshal
from .neo4j_ops import create_session, get_user_by_email, delete_user_by_email, set_user_fields
from marshmallow import Schema, fields

# TODO: enable swagger API spec


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


api = Namespace('users', title='User related operations')


@api.route('/<string:email>')
@api.param('email', 'The email of the user')
@api.response(404, 'User not found')
class Users(Resource):
    @api.doc('get_user')
    @api.response(200, 'User Found')
    def get(self, email):
        '''Fetch a user given its email.'''
        # if not valid_email(email):
        #    return 'Invalid email given.', 400

        with create_session() as session:
            response = session.read_transaction(get_user_by_email, email)
            user = response.single()
            # TODO: a lot going on here. See if this can be improved.
            if user:
                data = dict(user.data()['user'].items())
                return marshal(data, users), 200
            return "User not found", 404

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
            response = session.read_transaction(
                set_user_fields, email, api.payload)
            if response:
                return 204
            return "User was not found", 404

    @api.doc('create_user')
    @api.response(204, 'User created')
    def post(self):
        '''Create a user in the database.

        Validation is done in expect decorator.'''
        with create_session() as session:
            response = session.read_transaction(create_user, api.payload())
            # TODO: not sure how to handle neo4j response for this yet
            user = response.single()
            if user:
                return user, 204
            return "User not found", 404


"""
@api.route('/signup')
class SignUp(Resource):

    @api.expect(account_model)
    def post(self):
        with create_session() as session:
            response = session.read_transaction(create_user, api.payload)
            if type(response) is dict:
                return response

            profile = response.single()
            if profile:
                return dict(profile['newUser'].items()), 200
            return "User was not found", 404


@api.route('/login')
class LogIn(Resource):

    @api.expect(login_credentials_model)
    def post(self):
        with create_session() as session:
            profile = session.read_transaction(check_user, api.payload)
            if type(profile) is dict:
                return profile

            if profile:
                return dict(profile['p'].items()), 200
            return "User was not found", 404
"""
