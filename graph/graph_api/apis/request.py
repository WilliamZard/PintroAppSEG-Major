
from flask_restx import Namespace, Resource
from flask import make_response
from .neo4j_ops import create_session, create_request_relationship

api = Namespace(
    'request', title='For requesting user relationships(eg FOLLOW or AFFILIATED_WITH')

REQUEST_RELATIONSHIPS = {'follow': 'FOLLOW_REQUEST',
                         'affiliation': 'AFFILIATION_REQUEST'}


@api.route('/<string:relationship_type>/<string:follow_requester_email>/<string:follow_request_recipient_email>')
@api.produces('application/json')
class FollowRequest(Resource):
    def post(self, relationship_type, follow_requester_email, follow_request_recipient_email):
        # TODO: docstrings
        if relationship_type not in REQUEST_RELATIONSHIPS:
            return make_response('Invalid relationship type entered', 404)

        # TODO: validate emails
        with create_session() as session:
            response = session.write_transaction(
                create_request_relationship, REQUEST_RELATIONSHIPS[relationship_type], follow_requester_email, follow_request_recipient_email)
            if response.summary().counters.relationships_created == 1:
                return make_response('', 201)
            return 400

    def delete(self, follow_requester, follow_request_recipient):
        '''Delete the FOLLOW relationship, where follow_requester follows follow_request_recipient'''
        with create_session() as session:
            response = session.write_transaction(
                delete_follow_relationship, follow_requester, follow_request_recipient)
            print(response)
            if response.summary().counters.relationships_deleted == 1:
                print('reached')
                return make_response('', 204)
            return make_response('', 400)
