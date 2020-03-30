# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.

import pytest
from .conftest import app, populate_db
from .generate_test_data import User, basic_user_node, Chatroom, basic_chatroom_node


@pytest.mark.GET_chatroom
class TestGET:
    def test_GET_chatrooms_for_users_that_exist(self, app, populate_db):
        # Generate Data
        users = [
            User(email='user1@test.com')._asdict(),
            User(email='user2@test.com')._asdict(),
            User(email='user3@test.com')._asdict(),
            User(email='user4@test.com')._asdict(),
        ]
        chatrooms = [
            Chatroom()._asdict(),
            Chatroom()._asdict(),
        ]

        # Relationships
        userA_chatroomA = {
            's_node_properties': {'email': users[0]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[0]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        userB_chatroomA = {
            's_node_properties': {'email': users[1]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[0]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        userA_chatroomB = {
            's_node_properties': {'email': users[0]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[1]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        userC_chatroomB = {
            's_node_properties': {'email': users[2]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[1]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }

        populate_db(
            nodes_to_create=list(map(basic_user_node, users)) + list(map(basic_chatroom_node, chatrooms)),
            relationships_to_create=[userA_chatroomA, userB_chatroomA, userA_chatroomB, userC_chatroomB]
        )

        response = app.get(f"/chatrooms/{users[0]['email']}")
        assert response.status == '200 OK'
        # the order of chatrooms is arbitrary and sorted by the frontend,
        # so turning it into a set allows orderless checking of the data inside
        json = response.get_json()
        assert len(json) == 2
        # TODO: assert this for any json with these two keys, instead of assuming
        #       the response will only have these keys
        assert {"chat_id": str(chatrooms[0]['chat_id']),
                "recipient": users[1]['email']} in json
        assert {"chat_id": str(chatrooms[1]['chat_id']),
                "recipient": users[2]['email']} in json

        response = app.get(f"/chatrooms/{users[1]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": str(chatrooms[0]['chat_id']),
                "recipient": users[0]['email']} in json

        response = app.get(f"/chatrooms/{users[2]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": str(chatrooms[1]['chat_id']),
                "recipient": users[0]['email']} in json

        response = app.get(f"/chatrooms/{users[3]['email']}")
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
    def test_POST_new_chatroom_for_users_with_no_existing_chatroom(self, app, populate_db):
        users = [
            User(email='user1@test.com')._asdict(),
            User(email='user2@test.com')._asdict(),
        ]
        populate_db(
            nodes_to_create=list(map(basic_user_node, users)),
            relationships_to_create=[]
        )
        response = app.post(
            f"/chatrooms/{users[0]['email']}/{users[1]['email']}")
        assert response.status == '200 OK'
        json = dict(response.get_json())
        assert 'chat_id' in json
        new_chat_id = json['chat_id']

        response = app.get(
            f"/chatrooms/{users[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id,
                "recipient": users[1]['email']} in json

        response = app.get(
            f"/chatrooms/{users[1]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id,
                "recipient": users[0]['email']} in json

    def test_POST_new_chatroom_for_users_with_existing_chatroom(self, app, populate_db):
        users = [
            User(email='user1@test.com')._asdict(),
            User(email='user2@test.com')._asdict(),
        ]
        chatroom = Chatroom()._asdict()
        user1_chats = {
            's_node_properties': {'email': users[0]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatroom['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        user2_chats = {
            's_node_properties': {'email': users[1]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatroom['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        populate_db(
            nodes_to_create=list(map(basic_user_node, users)) + [basic_chatroom_node(chatroom)],
            relationships_to_create=[user1_chats, user2_chats]
        )
        response = app.post(
            f"/chatrooms/{users[0]['email']}/{users[1]['email']}")
        assert response.status == '409 CONFLICT'


@pytest.mark.DELETE_chatroom
class TestDelete:
    def test_DELETE_chatroom_with_id_that_exists(self, app, populate_db):
        users = [
            User(email='user1@test.com')._asdict(),
            User(email='user2@test.com')._asdict(),
        ]
        chatroom = Chatroom()._asdict()
        user1_chats = {
            's_node_properties': {'email': users[0]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatroom['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        user2_chats = {
            's_node_properties': {'email': users[1]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatroom['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        populate_db(
            nodes_to_create=list(map(basic_user_node, users)) + [basic_chatroom_node(chatroom)],
            relationships_to_create=[user1_chats, user2_chats]
        )
        response = app.delete(f"/chatrooms/{chatroom['chat_id']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        response = app.get(
            f"/chatrooms/{users[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

        response = app.get(
            f"/chatrooms/{users[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_DELETE_chatroom_with_id_that_does_not_exist(self, app):
        import uuid
        nonexistent_chatroom_id = str(uuid.uuid4())
        response = app.delete(f"/chatrooms/{nonexistent_chatroom_id}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''
