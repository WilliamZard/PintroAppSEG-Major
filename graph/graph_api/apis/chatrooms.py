from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email
from .posts import posts

from .neo4j_ops import (create_session,
                        get_chatrooms_of_user, check_users_in_chatroom, check_chatroom_exists,
                        create_chatroom,
                        delete_chatroom)

import uuid

# TODO: enable swagger API spec
# TODO: email validation


api = Namespace('chatrooms', title='Chatroom related operations')

# Schema used for serialisations


class ChatroomSchema(Schema):
    chat_id = fields.Str(required=True)


# Schema used for doc generation
chatrooms = api.model('Chatrooms', {
    'chat_id': restx_fields.String(required=True, title='The chatroom ID.'),
})

chatroom_schema = ChatroomSchema()

@api.route('/<string:email>')
@api.produces('application/json')
class Chatrooms(Resource):
    def get(self, email):
        '''Gets the chatrooms a user is in.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(get_chatrooms_of_user, email)
            response = response.data()
            return jsonify(response)

    def delete(self, email):
        '''Deletes the chatroom with the given ID.'''
        # email is actually chat id but i cant change it

        with create_session() as session:
            check_not_exists = session.read_transaction(check_chatroom_exists, email)
            if not check_not_exists.value('result'):
                return make_response('', 404)
            session.read_transaction(delete_chatroom, email)
            return make_response('', 204)



@api.route("/<string:email1>/<string:email2>")
@api.produces("application/json")
class ChatroomsPOST(Resource):
    @api.doc("create_chatroom")
    @api.response(409, 'Chatroom with these users already exists')
    def post(self, email1, email2):
        '''Create a chatroom with the given users in it.'''
        if not valid_email(email1):
            return make_response('', 422)
        if not valid_email(email2):
            return make_response('', 422)

        with create_session() as session:
            check_not_exists = session.read_transaction(check_users_in_chatroom, email1, email2)
            if check_not_exists.value('result'):
                return make_response('', 409)
            new_id = uuid.uuid4()
            session.read_transaction(create_chatroom, email1, email2, new_id)
            print(new_id)
            return jsonify({'chat_id': new_id})
