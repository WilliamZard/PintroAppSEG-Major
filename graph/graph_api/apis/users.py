from flask import make_response, Response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from neo4j.exceptions import ConstraintError

from .neo4j_ops import create_session
from .neo4j_ops.tags import (create_TAGGED_relationships,
                             delete_tagged_relationships)
from .neo4j_ops.chatrooms import get_chatrooms_of_account
from .neo4j_ops.general import set_properties, create_node, get_account_field
from .neo4j_ops.users import (delete_user_by_email,
                              get_followers_of_a_user,
                              get_followings_of_a_user,
                              get_posts_of_followings_of_a_user,
                              get_user_by_email)
from .utils import valid_email
from .image_storing import *

# TODO: enable swagger API spec
# TODO: email validation


api = Namespace('users', title='User related operations')
# Schema used for serialisations


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
    'active': restx_fields.String(title='DO NOT TOUCH, whether user is active or not.')
})  # title for accounts that needs to be created.


@api.route('/<string:email>')
@api.produces('application/json')
class Users(Resource):
    def get(self, email: str) -> Response:
        '''Fetch a user given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(get_user_by_email, email)
            response = response.single()
            if response:
                data = response.data()
                user = dict(data['user'].items())
                user['passions'] = data['passions']
                user['help_others'] = data['help_others']
                user['profile_image'] = str(
                    get_data_from_gcs(user['profile_image']))
                return jsonify(**user)
            return make_response('', 404)

    @api.doc('delete_user')
    @api.response(204, 'User deleted.')
    def delete(self, email: str) -> Response:
        '''Delete a user given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            # Fetch user image url in gcp storage that needs to be deleted.
            profile_image_url = (session.read_transaction(
                get_account_field, email, 'Person', 'profile_image').data())
            if len(profile_image_url) > 0:
                profile_image_url = profile_image_url[0]['profile_image']
            response = session.write_transaction(delete_user_by_email, email)
            # >= because post nodes of user may have been deleted
            if response.summary().counters.nodes_deleted >= 1:
                delete_data_from_gcs(profile_image_url)
                return make_response('', 204)
            return make_response('', 404)

    @api.doc('update_user')
    @api.response(204, 'User Fields Deleted')
    @api.expect(users)
    def put(self, email: str) -> Response:
        '''Update a user by the given fields.'''
        if not valid_email(email):
            return make_response('', 422)
        payload = api.payload
        passions = help_others = []
        if 'passions' in payload:
            passions = payload['passions']
            payload.pop('passions')
        if 'help_others' in payload:
            help_others = payload['help_others']
            payload.pop('help_others')
        response = None
        with create_session() as session:
            tx = session.begin_transaction()
            delete_tagged_relationships(tx, email)
            response = set_properties(
                tx, 'Person', 'email', email, api.payload)
            create_TAGGED_relationships(tx, email, passions, 'PassionsTag')
            create_TAGGED_relationships(
                tx, email, help_others, 'CanHelpWithTag')
            tx.commit()
        # TODO: validate payload
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
    def post(self) -> Response:
        '''Create a user.'''
        # TODO:validate email
        if not valid_email(api.payload['email']):
            return make_response('Not a valid email address.', 422)
        payload = api.payload
        passions = help_others = []
        if 'passions' in payload:
            passions = payload['passions']
            payload.pop('passions')
        if 'help_others' in payload:
            help_others = payload['help_others']
            payload.pop('help_others')
        with create_session() as session:
            try:
                tx = session.begin_transaction()
                response = create_node(tx, 'Person', payload)
                email = payload['email']
                # NOTE: tag labels specified must be identical to actual tag labels
                create_TAGGED_relationships(
                    tx, email, passions, 'Tag:PassionsTag')
                create_TAGGED_relationships(
                    tx, email, help_others, 'Tag:CanHelpWithTag')
                tx.commit()
                if response.summary().counters.nodes_created == 1:
                    return make_response('', 201)
            except ConstraintError:
                return make_response('Node with that email already exists.', 409)


@api.route('/<string:email>/followers')
@api.produces('application/json')
class UsersGETFollowers(Resource):
    @api.doc('get followers of a user')
    def get(self, email: str) -> Response:
        '''Get followers of a user'''
        with create_session() as session:
            response = session.read_transaction(
                get_followers_of_a_user, email)
            data = response.data()
            if data:
                # TODO iterate on followers and retrieve images, not url.
                return jsonify(data)
            else:
                return jsonify([])
            return make_response('', 404)


@api.route('/<string:email>/followings')
@api.produces('application/json')
class UsersGETFollowings(Resource):
    @api.doc('Get the users that the given user is following')
    def get(self, email: str) -> Response:
        '''Get the users that the given user is following'''
        with create_session() as session:
            response = session.read_transaction(
                get_followings_of_a_user, email)  # TODO iterate on followings and retrieve images, not url.
            data = response.data()
            if data:
                return jsonify(data)
            return make_response('', 404)


@api.route('/<string:email>/followings/posts')
@api.produces('application/json')
class UsersGETPostsOfFollowings(Resource):
    @api.doc('Get the posts of users the given user follows.')
    def get(self, email: str) -> Response:
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
    def put(self, email: str) -> Response:
        '''Deactivate a user account.'''
        if not valid_email(email):
            return make_response('', 422)
        fields = {'active': False}
        # TODO: validate payload
        with create_session() as session:
            response = session.write_transaction(
                set_properties, 'Person', 'email', email, fields)
            if response.summary().counters.properties_set == 1:
                return make_response('', 204)
            return make_response('', 404)


@api.route('/activate/<string:email>')
@api.produces('application/json')
class Users(Resource):
    @api.doc('activate users')
    @api.response(204, 'User activated.')
    def put(self, email: str) -> Response:
        '''Activate a user account if it has been deactivated.'''
        if not valid_email(email):
            return make_response('', 422)
        fields = {'active': True}
        # TODO: validate payload
        with create_session() as session:
            response = session.write_transaction(
                set_properties, 'Person', 'email', email, fields)
            if response.summary().counters.properties_set == 1:
                return make_response('', 204)
            return make_response('', 404)


@api.route('/<string:email>/chatrooms')
@api.produces('application/json')
class GETUserChatrooms(Resource):
    def get(self, email: str) -> Response:
        '''Gets the chatrooms a user is in.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(get_chatrooms_of_account, email)
            response = response.data()
            # gets the first label of each node, which is currently
            # assumed to be the type of the node, e.g. Person, Business, etc.
            for chat in response:
                chat["type"] = chat["type"][0]
            return jsonify(response)
