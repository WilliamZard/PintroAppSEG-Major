
from flask_restx import Namespace, Resource
from flask import make_response
from .neo4j_ops import create_session, create_request_relationship, delete_request_relationship

api = Namespace(
    'request', title='For requesting user relationships(eg FOLLOW or AFFILIATED_WITH')

REQUEST_RELATIONSHIPS = {'follow': 'FOLLOW_REQUEST',
                         'affiliation': 'AFFILIATION_REQUEST'}


@api.route('/<string:relationship_type>/<string:requester_email>/<string:request_recipient_email>')
@api.produces('application/json')
class Request(Resource):
    def post(self, relationship_type, requester_email, request_recipient_email):
        # TODO: docstrings
        if relationship_type not in REQUEST_RELATIONSHIPS:
            return make_response('Invalid relationship type entered', 404)

        # TODO: validate emails
        with create_session() as session:
            response = session.write_transaction(
                create_request_relationship, REQUEST_RELATIONSHIPS[relationship_type], requester_email, request_recipient_email)
            if response.summary().counters.relationships_created == 1:
                return make_response('', 201)
            return make_response('USER NOT FOUND', 404)

    def delete(self, relationship_type, requester_email, request_recipient_email):
        #TODO: docstrings
        with create_session() as session:
            response = session.write_transaction(
                delete_request_relationship, REQUEST_RELATIONSHIPS[relationship_type], requester_email, request_recipient_email)
            if response.summary().counters.relationships_deleted == 1:
                return make_response('', 204)
            return make_response('', 400)
