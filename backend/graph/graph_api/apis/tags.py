"""All endpoints for handling Tags nodes."""
import re
import time

from flask import abort, make_response, Response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields

from .neo4j_ops import create_session
from .neo4j_ops.tags import get_tags


def get_time() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


def convert_to_cypher_datetime(datetime: float) -> str:
    # Assumes there is a single space separating date and time sections
    # Assumes is in UTC time and is timezone naive
    return datetime.replace(' ', 'T') + '+00:00'


api = Namespace('tags', description='Tag related operations.')

tags = api.model('Tag', {
    'uuid': restx_fields.String(required=True),
    'created': restx_fields.String(),
    'name': restx_fields.String()
})

labels = api.model('Label', {
    'labels': restx_fields.List(restx_fields.String())
})


@api.route('/')
@api.produces('application/json')
@api.expect(labels)
class Tags(Resource):
    def post(self) -> Response:
        '''Get all tags with the given labels.'''
        if not api.payload or not api.payload['labels']:
            abort(400)
        label_pattern = r"^[a-zA-Z]*"
        for label in api.payload['labels']:
            if not re.fullmatch(label_pattern, label):
                abort(400)

        with create_session() as session:
            response = session.read_transaction(
                get_tags, api.payload['labels'])
            if response:
                data = [dict(tag['tag'].items())['name']
                        for tag in response.data()]
                return jsonify(data)
