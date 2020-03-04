# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
from ast import literal_eval

import pytest
from flask.json import jsonify

from .conftest import app
from .generate_test_data import (INVALID_EMAIL, INVALID_USER_TO_BE_CREATED,
                                 NONEXISTANT_USER_EMAIL, VALID_USER,
                                 VALID_USER_TO_BE_CREATED,
                                 VALID_USER_TO_BE_DELETED,
                                 VALID_USER_TO_BE_UPDATED,
                                 VALID_USER_TO_BE_UPDATED_NEW_FIELDS,
                                 USER_WITH_THREE_FOLLOWINGS,
                                 USER_WITH_TWO_FOLLOWINGS,
                                 USER_WITH_ONE_FOLLOWING,
                                 USER_WITH_NO_FOLLOWINGS)


@pytest.mark.GET_user
class TestGET:
    def test_GET_user_with_valid_email_that_exists(self, app):
        response = app.get(f"/users/{VALID_USER['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(VALID_USER).data

    def test_GET_user_with_valid_email_that_does_not_exist(self, app):
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_GET_user_with_invalid_email(self, app):
        response = app.get(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.DELETE_user
class TestDelete:
    def test_DELETE_user_with_valid_email_that_exists(self, app):
        email = VALID_USER_TO_BE_DELETED['email']
        response = app.delete(f"/users/{email}")
        assert response.status == '204 NO CONTENT'
        # TODO: consider using standard json.dumps instead of jsonify
        assert response.data == b''

        # Assert user was actually deleted in the database
        response = app.get(f"/users/{email}")
        assert response.status == '404 NOT FOUND'

    def test_DELETE_user_with_valid_email_that_does_not_exist(self, app):
        response = app.delete(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_DELETE_user_with_invalid_email(self, app):
        response = app.delete(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.PUT_user
class TestPut:
    def test_PUT_user_with_valid_email_that_exists(self, app):
        response = app.put(
            f"/users/{VALID_USER_TO_BE_UPDATED['email']}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
        # TODO: add requests and assertions for checking the resource was actually updated properly, not just good response.

    def test_PUT_user_with_valid_email_that_does_not_exist(self, app):
        response = app.put(
            f"/users/{NONEXISTANT_USER_EMAIL}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_PUT_user_with_invalid_email(self, app):
        response = app.put(
            f"/users/{INVALID_EMAIL}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    # TODO: add test for validating payload


@pytest.mark.POST_user
class TestPost:
    def test_POST_user_with_valid_payload_that_does_not_exist(self, app):
        response = app.post(
            "/users/", json=VALID_USER_TO_BE_CREATED)
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert user was actually created in the database
        response = app.get(f"/users/{VALID_USER_TO_BE_CREATED['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(VALID_USER_TO_BE_CREATED).data

    def test_POST_user_with_valid_payload_that_exists(self, app):
        response = app.post(
            "/users/", json=VALID_USER)
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_POST_user_with_invalid_payload(self, app):
        response = app.post(
            "/users/", json=INVALID_USER_TO_BE_CREATED)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'


@pytest.mark.GET_user_followers
class TestUsersGETFollowers:
    def test_GET_followers_of_existing_user(self, app):
        response = app.get(
            f"/users/{USER_WITH_ONE_FOLLOWING['email']}/followers")
        assert response.status == '200 OK'
        results = [{'full_name': user['full_name'], 'email': user['email']}
                   for user in [USER_WITH_TWO_FOLLOWINGS, USER_WITH_THREE_FOLLOWINGS]]
        assert response.data == jsonify(results).data

    def test_GET_followers_of_non_existing_user(self, app):
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}/followers")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_GET_followers_of_user_with_no_followers(self, app):
        raise NotImplementedError


@pytest.mark.GET_user_followings
class TestUsersGETFollowings:
    def test_GET_followings_of_existing_user(self, app):
        response = app.get(
            f"/users/{USER_WITH_TWO_FOLLOWINGS['email']}/followings")
        assert response.status == '200 OK'
        results = [{'full_name': user['full_name'], 'email': user['email']}
                   for user in [USER_WITH_ONE_FOLLOWING, USER_WITH_NO_FOLLOWINGS]]
        assert response.data == jsonify(results).data

    def test_GET_followings_of_non_existing_user(self, app):
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}/followings")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_GET_followings_of_user_with_no_followers(self, app):
        raise NotImplementedError


@pytest.mark.GET_user_followings_posts
class TestUsersGETFollowingsPosts:
    @pytest.mark.xfail
    def test_GET_all_posts_of_all_followers(self, app):
        raise NotImplementedError
