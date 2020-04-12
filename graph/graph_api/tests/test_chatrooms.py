import pytest
from flask import Flask

from .conftest import app, populate_db
from .generate_test_data import User, basic_user_node,\
    Chatroom, basic_chatroom_node,\
    Business, basic_business_node,\
    Space, basic_space_node


@pytest.mark.GET_chatrooms
class TestGET:
    def test_GET_chatrooms_for_accounts_that_exist(self, app: Flask, populate_db: None) -> None:
        # Generate Data
        user = User(email='user1@test.com')._asdict()
        space = Space(email='user2@test.com')._asdict()
        business = Business(email='user3@test.com')._asdict()
        empty_user = User(email='user4@test.com')._asdict()

        chatrooms = [
            Chatroom()._asdict(),
            Chatroom()._asdict(),
        ]

        # Relationships
        user_chatroomA = {
            's_node_properties': {'email': user['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[0]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        space_chatroomA = {
            's_node_properties': {'email': space['email']}, 's_node_labels': 'Space',
            'e_node_properties': {'chat_id': chatrooms[0]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        user_chatroomB = {
            's_node_properties': {'email': user['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[1]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        business_chatroomB = {
            's_node_properties': {'email': business['email']}, 's_node_labels': 'Business',
            'e_node_properties': {'chat_id': chatrooms[1]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }

        populate_db(
            nodes_to_create=[basic_user_node(user),
                             basic_space_node(space),
                             basic_business_node(business),
                             basic_user_node(empty_user)] + list(map(basic_chatroom_node, chatrooms)),
            relationships_to_create=[
                user_chatroomA, space_chatroomA, user_chatroomB, business_chatroomB]
        )

        response = app.get(f"/users/{user['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 2
        assert {"chat_id": str(chatrooms[0]['chat_id']),
                "recipient": space['email'],
                "type": "Space"} in json
        assert {"chat_id": str(chatrooms[1]['chat_id']),
                "recipient": business['email'],
                "type": "Business"} in json

        response = app.get(f"/spaces/{space['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": str(chatrooms[0]['chat_id']),
                "recipient": user['email'],
                "type": "Person"} in json

        response = app.get(f"/businesses/{business['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": str(chatrooms[1]['chat_id']),
                "recipient": user['email'],
                "type": "Person"} in json

        response = app.get(f"/users/{empty_user['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_GET_chatrooms_for_user_that_does_not_exists(self, app: Flask, populate_db: None) -> None:
        populate_db()

        nonexistant_email = 'doesnotexist@test.com'
        response = app.get(f"/users/{nonexistant_email}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_GET_chatrooms_for_business_that_does_not_exists(self, app: Flask, populate_db: None) -> None:
        populate_db()

        nonexistant_email = 'doesnotexist@test.com'
        response = app.get(f"/businesses/{nonexistant_email}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_GET_chatrooms_for_space_that_does_not_exists(self, app: Flask, populate_db: None) -> None:
        populate_db()

        nonexistant_email = 'doesnotexist@test.com'
        response = app.get(f"/spaces/{nonexistant_email}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0


@pytest.mark.POST_chatroom
class TestPost:
    def test_POST_new_chatroom_for_users_with_no_existing_chatroom(self, app: Flask, populate_db: None) -> None:
        users = [
            User(email='user1@test.com')._asdict(),
            User(email='user2@test.com')._asdict(),
        ]
        populate_db(
            nodes_to_create=list(map(basic_user_node, users)),
            relationships_to_create=[]
        )
        response = app.post(
            f"/chatrooms/{users[0]['email']}/Person/{users[1]['email']}/Person")
        assert response.status == '200 OK'
        json = dict(response.get_json())
        assert 'chat_id' in json
        new_chat_id = json['chat_id']

        response = app.get(
            f"/users/{users[0]['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id,
                "recipient": users[1]['email'],
                "type": "Person"} in json

        response = app.get(
            f"/users/{users[1]['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id,
                "recipient": users[0]['email'],
                "type": "Person"} in json

    def test_POST_new_chatroom_for_users_of_different_types(self, app: Flask, populate_db: None) -> None:
        user = User(email='user@test.com')._asdict()
        business = Business(email='business@test.com')._asdict()

        populate_db(
            nodes_to_create=[basic_user_node(user), basic_business_node(business)],
            relationships_to_create=[]
        )
        response = app.post(
            f"/chatrooms/{user['email']}/Person/{business['email']}/Business")
        assert response.status == '200 OK'
        json = dict(response.get_json())
        assert 'chat_id' in json
        new_chat_id = json['chat_id']

        response = app.get(
            f"/users/{user['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id,
                "recipient": business['email'],
                "type": "Business"} in json

        response = app.get(
            f"/businesses/{business['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id,
                "recipient": user['email'],
                "type": "Person"} in json

    def test_POST_new_chatroom_for_users_with_existing_chatroom(self, app: Flask, populate_db: None) -> None:
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
            f"/chatrooms/{users[0]['email']}/Person/{users[1]['email']}/Person")
        assert response.status == '409 CONFLICT'


@pytest.mark.DELETE_chatroom
class TestDelete:
    def test_DELETE_chatroom_with_id_that_exists(self, app: Flask, populate_db: None) -> None:
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
            nodes_to_create=list(map(basic_user_node, users)) +
            [basic_chatroom_node(chatroom)],
            relationships_to_create=[user1_chats, user2_chats]
        )
        response = app.delete(f"/chatrooms/{chatroom['chat_id']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        response = app.get(
            f"/users/{users[0]['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

        response = app.get(
            f"/users/{users[0]['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_DELETE_chatroom_with_id_that_does_not_exist(self, app: Flask, populate_db: None) -> None:
        populate_db()

        import uuid
        nonexistent_chatroom_id = str(uuid.uuid4())
        response = app.delete(f"/chatrooms/{nonexistent_chatroom_id}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''
