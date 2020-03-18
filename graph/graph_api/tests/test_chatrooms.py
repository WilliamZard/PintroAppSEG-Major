# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.

import pytest
from .generate_test_data import (CHATROOMS, CHATROOM_USERS, NONEXISTANT_CHATROOM_ID,
                                 VALID_CHATROOM_TO_BE_DELETED, VALID_CHATROOM_TO_BE_DELETED_USERS,
                                 CHATROOM_TO_BE_CREATED_USERS, NONEXISTANT_USER_EMAIL)


@pytest.mark.GET_chatroom
class TestGET:
    def test_GET_chatrooms_for_users_that_exist(self, app):
        response = app.get(f"/chatrooms/{CHATROOM_USERS[0]['email']}")
        assert response.status == '200 OK'
        # the order of chatrooms is arbitrary and sorted by the frontend,
        # so turning it into a set allows orderless checking of the data inside
        json = response.get_json()
        assert len(json) == 2
        # TODO: assert this for any json with these two keys, instead of assuming
        #       the response will only have these keys
        assert {"chat_id": CHATROOMS[0], "recipient": CHATROOM_USERS[1]['email']} in json
        assert {"chat_id": CHATROOMS[1], "recipient": CHATROOM_USERS[2]['email']} in json

        response = app.get(f"/chatrooms/{CHATROOM_USERS[1]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": CHATROOMS[0], "recipient": CHATROOM_USERS[0]['email']} in json

        response = app.get(f"/chatrooms/{CHATROOM_USERS[2]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": CHATROOMS[1], "recipient": CHATROOM_USERS[0]['email']} in json

        response = app.get(f"/chatrooms/{CHATROOM_USERS[3]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_GET_chatrooms_for_user_that_does_not_exists(self, app):
        response = app.get(f"/chatrooms/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0


@pytest.mark.POST_chatroom
class TestPost:
    def test_POST_new_chatroom_for_users_with_no_existing_chatroom(self, app):
        response = app.post(
            f"/chatrooms/{CHATROOM_TO_BE_CREATED_USERS[0]['email']}/{CHATROOM_TO_BE_CREATED_USERS[1]['email']}")
        assert response.status == '200 OK'
        json = dict(response.get_json())
        assert 'chat_id' in json
        new_chat_id = json['chat_id']

        response = app.get(f"/chatrooms/{CHATROOM_TO_BE_CREATED_USERS[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id, "recipient": CHATROOM_TO_BE_CREATED_USERS[1]['email']} in json

        response = app.get(f"/chatrooms/{CHATROOM_TO_BE_CREATED_USERS[1]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": new_chat_id, "recipient": CHATROOM_TO_BE_CREATED_USERS[0]['email']} in json

    def test_POST_new_chatroom_for_users_with_existing_chatroom(self, app):
        response = app.post(
            f"/chatrooms/{CHATROOM_USERS[0]['email']}/{CHATROOM_USERS[1]['email']}")
        assert response.status == '409 CONFLICT'


@pytest.mark.DELETE_chatroom
class TestDelete:
    def test_DELETE_chatroom_with_id_that_exists(self, app):
        response = app.delete(f"/chatrooms/{VALID_CHATROOM_TO_BE_DELETED}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        response = app.get(f"/chatrooms/{VALID_CHATROOM_TO_BE_DELETED_USERS[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

        response = app.get(f"/chatrooms/{VALID_CHATROOM_TO_BE_DELETED_USERS[0]['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_DELETE_chatroom_with_id_that_does_not_exist(self, app):
        response = app.delete(f"/chatrooms/{NONEXISTANT_CHATROOM_ID}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''