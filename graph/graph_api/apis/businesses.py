from flask import make_response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from neo4j.exceptions import ConstraintError

from .neo4j_ops import create_session
from .neo4j_ops.general import set_properties, create_node
from .neo4j_ops.businesses import (delete_business_by_email,
                                   get_business_by_email)
from .neo4j_ops.tags import (create_TAGGED_relationships,
                             delete_tagged_relationships)
from .utils import valid_email

# TODO: enable swagger API spec
# TODO: email validation


api = Namespace('businesses', title='Business related operations')


# Schema used for doc generation
businesses = api.model('Businesses', {
    'email': restx_fields.String(required=True, title='The business email.'),
    'password': restx_fields.String(required=True, title='The business password.'),
    'full_name': restx_fields.String(required=True, title='The business full name.'),
    'profile_image': restx_fields.String(title='image saved as array of Bytes representing the business\'s profile pic.'),
    'phone': restx_fields.String(title="The business's phone number."),
    'location': restx_fields.String(title='current city of the business.'),
    'short_bio': restx_fields.String(title='short bio describing the business of maximum 250 characters.'),
    'story': restx_fields.String(title='story describing the business of maximum 250 words.'),
    'tags': restx_fields.List(restx_fields.String(), description='List of tag UUIDs that the business is related to.'),
    'date_founded': restx_fields.String(title='date the company was founded.'),
    'company_size': restx_fields.String(title='size of the company.'),
    'funding': restx_fields.String(title='amount of funding the comapy currently controls.'),
    'team_members': restx_fields.String(title='main team memebers of the company.'),
    'seeking_investment': restx_fields.String(title='whether the company is looking for investments.'),
    'currently_hiring': restx_fields.String(title='whether the company is currently looking for potential employees.')
})


@api.route('/<string:email>')
@api.produces('application/json')
@api.expect(businesses)
class Businesses(Resource):
    def get(self, email):
        '''Fetch a business given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(get_business_by_email, email)
            response = response.single()
            if response:
                data = response.data()
                business = dict(data['user'].items())
                business['tags'] = data['tags']
                return jsonify(**business)
            return make_response('', 404)

    @api.doc('delete_business')
    @api.response(204, 'Business Deleted')
    def delete(self, email):
        '''Delete a business given its email.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(
                delete_business_by_email, email)
            if response.summary().counters.nodes_deleted == 1:
                return make_response('', 204)
            return make_response('', 404)

    @api.doc('update_business')
    @api.response(204, 'Business Fields Deleted')
    def put(self, email):
        '''Update a business by the given fields.'''
        if not valid_email(email):
            return make_response('', 422)

        payload = api.payload
        tags = []
        if 'tags' in payload:
            tags = payload['tags']
            payload.pop('tags')

        response = None
        with create_session() as session:
            tx = session.begin_transaction()
            delete_tagged_relationships(tx, email)
            response = set_properties(
                tx, 'Business', 'email', email, api.payload)
            create_TAGGED_relationships(tx, email, tags, 'BusinessTag')
            tx.commit()
        if response.summary().counters.properties_set == len(payload):
            return make_response('', 204)
        return make_response('', 404)


@api.route('/')
@api.produces('application/json')
@api.expect(businesses)
class BusinessPost(Resource):
    @api.doc('create_business')
    @api.response(204, 'Business created')
    @api.response(409, 'Business with that email already exists')
    def post(self):
        '''Create a business.'''
        if not valid_email(api.payload['email']):
            return make_response('Not a valid email address.', 422)

        payload = api.payload
        tags = []
        if 'tags' in payload:
            tags = payload['tags']
            payload.pop('tags')

        response = None
        with create_session() as session:
            try:
                # TODO: break up create_business function into different queries.
                tx = session.begin_transaction()
                response = create_node(tx, 'Business', payload)
                create_TAGGED_relationships(
                    tx, payload['email'], tags, 'BusinessTag')
                tx.commit()
                if response.summary().counters.nodes_created == 1:
                    return make_response('', 201)
            except ConstraintError:
                return make_response('Node with that email already exists.', 409)
