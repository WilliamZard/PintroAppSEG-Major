# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.

import pytest
from .conftest import app, populate_db
from .generate_test_data import (CHATROOMS, CHATROOM_USERS, NONEXISTANT_CHATROOM_ID,
                                 VALID_CHATROOM_TO_BE_DELETED, VALID_CHATROOM_TO_BE_DELETED_USERS,
                                 CHATROOM_TO_BE_CREATED_USERS, NONEXISTANT_USER_EMAIL)
from .generate_test_data import User, basic_user_node, Chatroom, basic_chatroom_node


@pytest.mark.GET_chatroom
class TestGET:
    def test_GET_chatrooms_for_users_that_exist(self, app, populate_db):
        # TODO: adapt this test to new testing procedures
        # Should be a question of creating right user nodes, chatroom nodes, and relationships

        # Generate Data
        user = User(email='chatty_user@test.com')._asdict()
        user_node = basic_user_node(user)

        chatroom_a = Chatroom()._asdict()
        chatroom_a_node = basic_chatroom_node(chatroom_a)
        chatroom_b = Chatroom()._asdict()
        chatroom_b_node = basic_chatroom_node(chatroom_b)

        # Relationships
        chats_in_a = {
            's_node_properties': {'email': user['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'uuid': chatroom_a['uuid']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'}
        chats_in_b = {
            's_node_properties': {'email': user['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'uuid': chatroom_b['uuid']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'}

        populate_db(nodes_to_create=[user_node, chatroom_a_node, chatroom_b_node],
                    relationships_to_create=[chats_in_a, chats_in_b])

        response = app.get(f"/chatrooms/{user['email']}")
        assert response.status == '200 OK'
        # the order of chatrooms is arbitrary and sorted by the frontend,
        # so turning it into a set allows orderless checking of the data inside
        json = response.get_json()
        assert len(json) == 2
        # TODO: assert this for any json with these two keys, instead of assuming
        #       the response will only have these keys
        assert {"chat_id": chatroom_a['chat_id'],
                "recipient": CHATROOM_USERS[1]['email']} in json
        assert {"chat_id": CHATROOMS[1],
                "recipient": CHATROOM_USERS[2]['email']} in json

        response = app.get(f"/chatrooms/{CHATROOM_USERS[1]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": CHATROOMS[0],
                "recipient": CHATROOM_USERS[0]['email']} in json

        response = app.get(f"/chatrooms/{CHATROOM_USERS[2]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": CHATROOMS[1],
                "recipient": CHATROOM_USERS[0]['email']} in json

        response = app.get(f"/chatrooms/{CHATROOM_USERS[3]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_GET_chatrooms_for_user_that_does_not_exists(self, app):
        nonexistant_email = 'doesnotexist@test.com'
        response = app.get(f"/chatrooms/{nonexistant_email}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0


@pytest.mark.POST_chatroom
class TestPost:
    def test_POST_new_chatroom_for_users_with_no_existing_chatroom(self, app):
        # TODO: adapt to new testing procedures
        # create user nodes
        response = app.post(
            f"/chatrooms/{CHATROOM_TO_BE_CREATED_USERS[0]['email']}/{CHATROOM_TO_BE_CREATED_USERS[1]['email']}")
        assert response.status == '200 OK'
        json = dict(response.get_json())
        assert 'chat_id' in json
        new_chat_id = json['chat_id']

        response = app.get(
            f"/chatrooms/{CHATROOM_TO_BE_CREATED_USERS[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id,
                "recipient": CHATROOM_TO_BE_CREATED_USERS[1]['email']} in json

        response = app.get(
            f"/chatrooms/{CHATROOM_TO_BE_CREATED_USERS[1]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id,
                "recipient": CHATROOM_TO_BE_CREATED_USERS[0]['email']} in json

    def test_POST_new_chatroom_for_users_with_existing_chatroom(self, app):
        # TODO: adapt to new testing procedure
        # create user nodes, chatroom nodes, and relationship between them
        response = app.post(
            f"/chatrooms/{CHATROOM_USERS[0]['email']}/{CHATROOM_USERS[1]['email']}")
        assert response.status == '409 CONFLICT'


@pytest.mark.DELETE_chatroom
class TestDelete:
    def test_DELETE_chatroom_with_id_that_exists(self, app):
        # TODO: adapt to new testing procedures
        # create user nodes, chatroom nodes, and relationship between them
        response = app.delete(f"/chatrooms/{VALID_CHATROOM_TO_BE_DELETED}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        response = app.get(
            f"/chatrooms/{VALID_CHATROOM_TO_BE_DELETED_USERS[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

        response = app.get(
            f"/chatrooms/{VALID_CHATROOM_TO_BE_DELETED_USERS[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_DELETE_chatroom_with_id_that_does_not_exist(self, app):
        import uuid
        nonexistant_chatroom_id = str(uuid.uuid4())
        response = app.delete(f"/chatrooms/{nonexistant_chatroom_id}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''
