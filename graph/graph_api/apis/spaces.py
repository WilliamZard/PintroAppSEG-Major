from flask import make_response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from neo4j.exceptions import ConstraintError

from .image_storing import *
from .neo4j_ops import create_session
from .neo4j_ops.general import set_properties, create_node, get_account_field
from .neo4j_ops.spaces import (delete_space_by_email,
                               get_space_by_email)
from .utils import valid_email


# TODO: enable swagger API spec
# TODO: email validation


api = Namespace('spaces', title='Space related operations')


# Schema used for doc generation
spaces = api.model('Spaces', {
    'email': restx_fields.String(required=True, title='The co-working space email.'),
    'password': restx_fields.String(required=True, title='The co-working space password.'),
    'full_name': restx_fields.String(required=True, title='The co-working space full name.'),
    'profile_image': restx_fields.String(title='image saved as array of Bytes representing the co-working space\'s profile pic.'),
    'phone': restx_fields.String(title="The co-working space's phone number."),
    'location': restx_fields.String(title='current city of the co-working space.'),
    'short_bio': restx_fields.String(title='short bio describing the co-working space of maximum 250 characters.')
})  # title for accounts that needs to be created.


@api.route('/<string:email>')
@api.produces('application/json')
class Spaces(Resource):
    def get(self, email):
        '''Fetch a co-working space given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(get_space_by_email, email)
            space = response.single()
            if space:
                # TODO: a lot going on here. See if this can be improved.
                data = dict(space.data()['user'].items())
                data['profile_image'] = str(get_data_from_gcs(data['profile_image']))
                return jsonify(**data)
            return make_response('', 404)

    @api.doc('delete_space')
    @api.response(204, 'Co-working space Deleted')
    def delete(self, email):
        '''Delete a co-working space given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            # Fetch user image url in gcp storage that needs to be deleted.
            profile_image_url = (session.read_transaction(get_account_field, email, 'Space', 'profile_image').data())
            if len(profile_image_url) > 0:
                profile_image_url = profile_image_url[0]['profile_image']
            response = session.read_transaction(delete_space_by_email, email)
            if response.summary().counters.nodes_deleted == 1:
                delete_data_from_gcs(profile_image_url)
                return make_response('', 204)
            return make_response('', 404)

    @api.doc('update_space')
    @api.response(204, 'Co-working Space Fields Deleted')
    def put(self, email):
        '''Update a co-working space by the given fields.'''
        if not valid_email(email):
            return make_response('', 422)

        # TODO: validate payload
        with create_session() as session:
            response = session.write_transaction(
                set_properties, 'Space', 'email', email, api.payload)
            if response.summary().counters.properties_set == len(api.payload):
                return make_response('', 204)
            return make_response('', 404)


@api.route('/')
@api.produces('application/json')
class SpacesPost(Resource):
    @api.doc('create_space')
    @api.response(204, 'Co-working space created')
    @api.response(409, 'Co-working space with that email already exists')
    def post(self):
        '''Create a co-working space.'''
        payload = api.payload
        if not valid_email(payload['email']):
            return make_response('Not a valid email address.', 422)
        with create_session() as session:
            try:
                response = session.write_transaction(
                    create_node, 'Space', api.payload)
                if response.summary().counters.nodes_created == 1:
                    return make_response('', 201)
            except ConstraintError:
                return make_response('Node with that email already exists.', 409)
