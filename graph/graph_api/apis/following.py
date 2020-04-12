from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import create_session
from .neo4j_ops.requests import (
    create_follow_relationship, delete_follow_relationship, approve_follow_request)


api = Namespace(
    'follow', title='Operations related to the FOLLOW relationship')


@api.route('/request/<string:follow_requester>/<string:follow_request_recipient>')
@api.produces('application/json')
class FollowRequest(Resource):
    def post(self, follow_requester, follow_request_recipient):
        '''Create a FOLLOW_REQUEST relationship, where follow_requester has requested to follow follow_request_recipient.'''
        with create_session() as session:
            response = session.write_transaction(
                create_follow_relationship, follow_requester, follow_request_recipient)
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


@api.route('/approve/<string:follow_requester>/<string:follow_request_recipient>')
@api.produces('application/json')
class FollowApprove(Resource):
    def post(self, follow_requester, follow_request_recipient):
        '''Approve a follow request where follow_requester has requested to follow follow_request_recipient. This converts the REQUESTED_FOLLOW relationship in the graph to a FOLLOWS relationship.'''
        with create_session() as session:
            response = session.write_transaction(
                approve_follow_request, follow_requester, follow_request_recipient)
            counters = response.summary().counters
            print(counters)
            if counters.relationships_created == 1 and counters.relationships_deleted == 1:
                return make_response('', 201)
            return make_response('', 400)
