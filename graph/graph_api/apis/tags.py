import time

from flask import make_response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields, validate
from marshmallow.exceptions import ValidationError

from .neo4j_ops import (create_session, get_tags)


# TODO: refactor these util functions
def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


def convert_to_cypher_datetime(datetime):
    # Assumes there is a single space separating date and time sections
    # Assumes is in UTC time and is timezone naive
    return datetime.replace(' ', 'T') + 'Z'


api = Namespace('tags', description='Tag related operations.')


class TagSchema(Schema):
    uuid = fields.UUID()
    created = fields.DateTime()
    name = fields.Str()


tags = api.model('Tag', {
    'uuid': restx_fields.String(required=True),
    'created': restx_fields.DateTime(),
    'name': restx_fields.String()
})

tags_schema = TagSchema()


@api.route('/')
@api.produces('application/json')
class Tags(Resource):
    def get(self):
        '''Get all tags with the given labels.'''

        with create_session() as session:
            response = session.read_transaction(
                get_tags, api.payload)
            print(response.data())
            if response:
                return jsonify(response.data())
            return make_response('', 404)
