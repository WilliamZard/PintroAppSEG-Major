from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (
    create_session, create_affiliation_relationship)


api = Namespace(
    'affiliation', title='Operations related to the AFFILIATION relationship')


@api.route('/request/<string:affiliation_requester>/<string:affiliation_request_recipient>')
@api.produces('application/json')
class AffiliationRequest(Resource):
    def post(self, affiliation_requester, affiliation_request_recipient):
        '''Create an AFFILIATION_REQUEST relationship, where affiliation_requester has requested to follow affiliation_request_recipient.'''
        with create_session() as session:
            print('here')
            response = session.write_transaction(
                create_affiliation_relationship, affiliation_requester, affiliation_request_recipient)
            print(response)
            if response.summary().counters.relationships_created == 1:
                print('reached if statement')
                return make_response('', 201)
            print('reached after if statement')
            return 400

