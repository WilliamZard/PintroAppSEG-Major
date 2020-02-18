from flask_restplus import Namespace, Resource, fields, marshal
from .neo4j_ops import create_session, get_user_by_email, delete_user_by_email, set_user_fields
from .utils import validate_email

api = Namespace('users', title='User related operations')
users = api.model('Users', {
    'email': fields.String(required=True, title='The user email.'),
    # TODO: could do hashing in a function here
    'password': fields.String(required=True, title='The user password.'),
    'full_name': fields.String(required=True, title='The user full name.'),
    'preferred_name': fields.String(title='The user preferred name.'),
    'profile_image': fields.String(title='image saved as array of Bytes representing the user\'s profile pic.'),
    'phone': fields.String(title="The user's phone number."),
    'gender': fields.String(title="The User's geneder"),
    'job_title': fields.String(title='current job title of the user.'),
    'location': fields.String(title='current city of the user.'),
    'short_bio': fields.String(title='short bio describing the user of maximum 250 characters.'),
    'story': fields.String(title='story describing the user of maximum 250 words.'),
    'education': fields.String(title='Highest level obtained.')
})  # title for accounts that needs to be created.


@api.route('/<string:email>')
@api.param('email', 'The email of the user')
@api.response(404, 'User not found')
class Users(Resource):
    @api.doc('get_user')
    @validate_email
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
    @validate_email
    def delete(self, email):
        '''Delete a user given its email.'''
        with create_session() as session:
            response = session.read_transaction(delete_user_by_email, email)
            # TODO: not sure how to handle neo4j response for this yet
            user = response.single()
            if user:
                return user, 204
            return "User not found", 404

    @api.expect(users)
    @api.marshal_with(users)
    @validate_email
    def put(self, email):
        '''Update a user by the given fields.'''
        # TODO: validate payload
        with create_session() as session:
            response = session.read_transaction(
                set_user_fields, email, api.payload)
            if response:
                return 204
            return "User was not found", 404


# Commented for now as user posting will happen elsewher
"""
    @api.doc('create_user')
    @api.expect(users)
    @api.marshal_with(users, code=201)
    def post(self):
        # TODO: input validation
        with create_session() as session:
            response = session.read_transaction(create_user, api.payload())
            # TODO: not sure how to handle neo4j response for this yet
            user = response.single()
            if user:
                return user, 204
            return "User not found", 404"""

# You need to specify what is expected to be posted as body of the http message on this post.


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
