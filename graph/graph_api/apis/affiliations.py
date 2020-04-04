import time

from flask import make_response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from neo4j.exceptions import ConstraintError

from .neo4j_ops import create_session
from .neo4j_ops.requests import (create_affiliation_relationship,
                                 delete_affiliation_relationship)
from .utils import valid_email

api = Namespace(
    'affiliation', title='Operations related to the AFFILIATION relationship')


@api.route('/request/<string:affiliation_requester>/<string:affiliation_request_recipient>')
@api.produces('application/json')
class AffiliationRequest(Resource):
    def post(self, affiliation_requester, affiliation_request_recipient):
        '''Create an AFFILIATION_REQUEST relationship, where affiliation_requester has requested to follow affiliation_request_recipient.'''
        with create_session() as session:
            created_at = time.time()
            response = session.write_transaction(
                create_affiliation_relationship,
                affiliation_requester,
                affiliation_request_recipient,
                created_at)
            if response.summary().counters.relationships_created == 1:
                return make_response('', 201)
            return make_response('', 400)

    def delete(self, affiliation_requester, affiliation_request_recipient):
        '''Delete the AFFILIATION relationship, where affiliation_requester wants to be affiliated with affiliation_request_recipient'''
        with create_session() as session:
            response = session.write_transaction(
                delete_affiliation_relationship, affiliation_requester, affiliation_request_recipient)
            print(response)
            if response.summary().counters.relationships_deleted == 1:
                print('reached')
                return make_response('', 204)
            return make_response('', 400)
