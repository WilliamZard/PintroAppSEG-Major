import time
import uuid

from flask import make_response, Response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from neo4j.exceptions import ConstraintError

from .neo4j_ops import create_session
from .neo4j_ops.general import set_properties, create_node, create_relationship
from .neo4j_ops.posts import (delete_post,
                              get_list_of_user_post_dates, get_post_by_uuid)
from .utils import valid_email


def get_time() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


def convert_to_cypher_datetime(datetime: float) -> None:
    # Assumes there is a single space separating date and time sections
    # Assumes is in UTC time and is timezone naive
    return datetime.replace(' ', 'T') + 'Z'
# TODO: email validation
# TODO: docstrings of functions need updating


api = Namespace('posts', title='Posting related operations')


# TODO: review this
# Schema used for doc generation
posts = api.model('Post', {
    'content': restx_fields.String(required=True, title='The content of the post.'),
    'hashtags': restx_fields.String(title='The post\'s hashtags'),
    'uuid': restx_fields.String(),
    'created': restx_fields.DateTime(),
    'modified': restx_fields.DateTime(),
    'user_email': restx_fields.String()
})


@api.route('/<string:uuid>')
@api.produces('application/json')
class Posts(Resource):
    def get(self, uuid: str) -> Response:
        '''Fetch a post based on its UUID.'''

        with create_session() as session:
            response = session.read_transaction(get_post_by_uuid, uuid)
            post = response.single()
            if post:
                data = dict(post.data()['post'].items())
                data['modified'] = str(data['modified']).replace('+00:00', 'Z')
                data['created'] = str(data['created']).replace('+00:00', 'Z')
                return jsonify(data)
            return make_response('', 404)

    @api.doc('update_post')
    @api.response(204, 'Post updated')
    @api.expect(posts)
    def put(self,uuid: str) -> Response:
        '''Update a Post's content.'''

        with create_session() as session:
            content = api.payload['content']
            hashtags = api.payload['hashtags']
            response = session.write_transaction(
                set_properties, 'Post', 'uuid', uuid, {'content': content, 'hashtags': hashtags})
            if response.summary().counters.properties_set == 2:
                return make_response('', 204)
            return make_response('', 404)

    # TODO It will be necessary to have authorization to do that.
    # TODO It will be necessary to have authorization to do that.
    @api.doc('delete_post')
    @api.response(204, 'Post deleted')
    def delete(self, uuid: str) -> Response:
        '''Delete a post given its uuid.'''
        # TODO: assumes only other response is not found. This needs more details.

        with create_session() as session:
            response = session.read_transaction(
                delete_post, uuid)
            counters = response.summary().counters
            if counters.nodes_deleted == 1 and counters.relationships_deleted == 1:
                return make_response('', 204)
            return make_response('', 404)


@api.route('/')
@api.produces('application/json')
@api.expect(posts)
class PostsPost(Resource):
    @api.doc('create_post')
    @api.response(204, 'Post created')
    def post(self) -> Response:
        '''Create a post.'''
        payload = api.payload
        if len(payload['content']) <= 300 and len(payload['content']) == 0:
            return make_response('Post content length must be between 1 and 300.', 422)
        created = modified = convert_to_cypher_datetime(get_time())
        post_uuid = uuid.uuid4()
        content = payload['content']
        user_email = payload['user_email']
        hashtags = payload['hashtags']
        properties = dict(created=created, uuid=post_uuid,
                          content=content, modified=modified,
                          hashtags=hashtags)
        with create_session() as session:
            try:
                tx = session.begin_transaction()
                node_creation_response = create_node(tx, 'Post', properties)
                node_creation_counters = node_creation_response.summary().counters
                relationship_creation_response = create_relationship(tx, 'Person', {'email': user_email}, 'Post', {
                    'uuid': post_uuid}, 'POSTED')
                relationship_creation_counters = relationship_creation_response.summary().counters
                tx.commit()
                if (node_creation_counters.nodes_created == 1
                    and relationship_creation_counters.relationships_created == 1
                    and node_creation_counters.labels_added == 1  # NOTE: What is this for?
                        and node_creation_counters.properties_set == 5):
                    return make_response('', 201)
            except ConstraintError:
                return make_response('Node with that email already exists.', 409)
