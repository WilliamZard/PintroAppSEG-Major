
import time

from flask import make_response
from flask_restx import Namespace, Resource

from .neo4j_ops import create_session
from .neo4j_ops.requests import approve_request
from .request import REQUEST_RELATIONSHIPS

api = Namespace(
    'approve', title='For approving user relationships(eg FOLLOW or AFFILIATED_WITH')

# TODO: combine relationship mappings into a nested dict
APPROVE_RELATIONSHIPS_MAPPING = {
    'follow': 'FOLLOWS', 'affiliation': 'AFFILIATED_WITH'}


@api.route('/<string:relationship_type>/<string:requester_email>/<string:request_recipient_email>')
@api.produces('application/json')
class Approve(Resource):
    def post(self, relationship_type, requester_email, request_recipient_email):
        '''
        Replace the existing request relationship with an approved relationship.
        E.g. REQUESTED_FOLLOW => FOLLOWS
        '''
        if relationship_type not in REQUEST_RELATIONSHIPS:
            return make_response('Invalid relationship type entered', 404)

        # TODO: validate emails
        with create_session() as session:
            created_at = time.time()
            response = session.write_transaction(
                approve_request,
                REQUEST_RELATIONSHIPS[relationship_type],
                APPROVE_RELATIONSHIPS_MAPPING[relationship_type],
                requester_email,
                request_recipient_email,
                created_at)
            if response.summary().counters.relationships_created == 1 and response.summary().counters.relationships_deleted == 1:
                return make_response('', 201)
            return make_response('USER NOT FOUND', 404)
