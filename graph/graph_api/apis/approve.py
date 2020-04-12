"""All endpoints for approving user requests."""
import time

from flask import make_response, Response
from flask_restx import Namespace, Resource

from .neo4j_ops import create_session
from .neo4j_ops.general import create_relationship, delete_relationship
from .request import REQUEST_RELATIONSHIPS

from neo4j import Transaction
from .utils import valid_email

api = Namespace(
    'approve', title='For approving user relationships(eg FOLLOW or AFFILIATED_WITH')

# TODO: combine relationship mappings into a nested dict
APPROVE_RELATIONSHIPS_MAPPING = {
    'follow': 'FOLLOWS', 'affiliation': 'AFFILIATED_WITH'}


@api.route('/<string:relationship_type>/<string:requester_email>/<string:request_recipient_email>')
@api.produces('application/json')
class Approve(Resource):
    def post(self, relationship_type: str, requester_email: str, request_recipient_email: str) -> Response:
        '''
        Replace the existing request relationship with an approved relationship.
        E.g. REQUESTED_FOLLOW => FOLLOWS
        '''
        if relationship_type not in REQUEST_RELATIONSHIPS:
            return make_response('Invalid relationship type entered', 404)
        if valid_email(requester_email) == None:
            return make_response('', 422)
        if valid_email(request_recipient_email) == None:
            return make_response('', 422)

        s_node_label = e_node_label = 'Person'
        if relationship_type == 'affiliation':
            s_node_label = 'Business'

        with create_session() as session:
            created_at = time.time()
            tx: Transaction = session.begin_transaction()
            del_response = delete_relationship(tx, s_node_label, {'email': requester_email}, e_node_label, {
                'email': request_recipient_email}, REQUEST_RELATIONSHIPS[relationship_type])
            create_response = create_relationship(tx, s_node_label, {'email': requester_email}, e_node_label, {
                'email': request_recipient_email}, APPROVE_RELATIONSHIPS_MAPPING[relationship_type], {'created_at': created_at})
            tx.commit()
            if create_response.summary().counters.relationships_created == 1 and del_response.summary().counters.relationships_deleted == 1:
                return make_response('', 201)
            return make_response('USER NOT FOUND', 404)
