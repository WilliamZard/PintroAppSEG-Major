import uuid

from flask import make_response, Response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from neo4j.exceptions import ConstraintError

from .neo4j_ops import create_session
from .neo4j_ops.general import create_node, create_relationship
from .neo4j_ops.chatrooms import (check_chatroom_exists,
                                  check_users_in_chatroom,
                                  delete_chatroom, get_chatrooms_of_user)
from .posts import posts
from .utils import valid_email


api = Namespace('chatrooms', title='Chatroom related operations')


# Schema used for doc generation
chatrooms = api.model('Chatrooms', {
    'chat_id': restx_fields.String(required=True, title='The chatroom ID.'),
})


@api.route("/<string:email1>/<string:email2>")
@api.produces("application/json")
class ChatroomsPOST(Resource):
    @api.doc("create_chatroom")
    @api.response(409, 'Chatroom with these users already exists')
    def post(self, email1: str, email2: str) -> Response:
        '''Create a chatroom with the given users in it.'''
        if not valid_email(email1):
            return make_response('', 422)
        if not valid_email(email2):
            return make_response('', 422)

        with create_session() as session:
            check_not_exists = session.read_transaction(
                check_users_in_chatroom, email1, email2)
            if check_not_exists.value('result'):
                return make_response('', 409)
            new_id = str(uuid.uuid4())
            tx = session.begin_transaction()
            create_node(tx, 'Chatroom', {'chat_id': new_id})
            create_relationship(tx, 'Person', {'email': email1}, 'Chatroom', {
                                'chat_id': new_id}, 'CHATS_IN')
            create_relationship(tx, 'Person', {'email': email2}, 'Chatroom', {
                                'chat_id': new_id}, 'CHATS_IN')
            tx.commit()
            return jsonify({'chat_id': new_id})


@api.route('/<string:chat_id>')
@api.produces('application/json')
class ChatroomsDELETE(Resource):
    def delete(self, chat_id):
        '''Deletes the chatroom with the given ID.'''
        with create_session() as session:
            check_not_exists = session.read_transaction(
                check_chatroom_exists, chat_id)
            if not check_not_exists.value('result'):
                return make_response('', 404)
            session.read_transaction(delete_chatroom, chat_id)
            return make_response('', 204)
