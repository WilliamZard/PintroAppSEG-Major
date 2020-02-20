from flask import Blueprint
from .neo4j_ops import create_session, get_user_by_email, delete_user_by_email, set_user_fields
from marshmallow import Schema, fields
from flask.json import jsonify

# TODO: enable swagger API spec
# TODO: email validation


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


users = Blueprint('users', __name__, url_prefix='/users')
user_schema = UserSchema()


@users.route('/<string:email>', methods=['GET'])
def get_user(email):
    '''Fetch a user given its email.'''

    with create_session() as session:
        response = session.read_transaction(get_user_by_email, email)
        user = response.single()
        if user:
            # TODO: a lot going on here. See if this can be improved.
            data = dict(user.data()['user'].items())
            return user_schema.dump(data)
        return "User not found", 404


@users.route('/<string:email>', methods=['DELETE'])
def delete(email):
    '''Delete a user given its email.'''
    with create_session() as session:
        response = session.read_transaction(delete_user_by_email, email)
        # TODO: not sure how to handle neo4j response for this yet
        user = response.single()
        if user:
            return user, 204
        return "User not found", 404


@users.route('/<string:email>', methods=['PUT'])
def put(email):
    '''Update a user by the given fields.'''
    # TODO: validate payload
    with create_session() as session:
        response = session.read_transaction(
            set_user_fields, email, api.payload)
        if response:
            return 204
        return "User was not found", 404


@users.route('', methods=['POST'])
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
