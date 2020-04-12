
from flask_restx import Namespace, Resource
from flask import make_response, Response
from .neo4j_ops import create_session
from .neo4j_ops.general import create_relationship, delete_relationship
from .utils import valid_email
import time

api = Namespace(
    'request', title='For requesting user relationships(eg FOLLOW or AFFILIATED_WITH')

REQUEST_RELATIONSHIPS = {'follow': 'REQUESTED_FOLLOW',
                         'affiliation': 'REQUESTED_AFFILIATION'}


@api.route('/<string:relationship_type>/<string:requester_email>/<string:request_recipient_email>')
@api.produces('application/json')
class Request(Resource):
    def post(self, relationship_type: str, requester_email: str, request_recipient_email: str) -> Response:
        '''Create a request relationship.'''
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
            tx = session.begin_transaction()
            response = create_relationship(tx, s_node_label, {'email': requester_email}, e_node_label, {
                                           'email': request_recipient_email}, REQUEST_RELATIONSHIPS[relationship_type], {'created_at': created_at})
            tx.commit()
            if response.summary().counters.relationships_created == 1:
                return make_response('', 201)
            return make_response('USER NOT FOUND', 404)

    def delete(self, relationship_type: str, requester_email: str, request_recipient_email: str) -> Response:
        '''Delete request relationship, effectively denying the request.'''
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
            tx = session.begin_transaction()
            response = delete_relationship(tx, s_node_label, {'email': requester_email}, e_node_label, {
                                           'email': request_recipient_email}, REQUEST_RELATIONSHIPS[relationship_type])
            tx.commit()
            if response.summary().counters.relationships_deleted == 1:
                return make_response('', 204)
            return make_response('', 400)
