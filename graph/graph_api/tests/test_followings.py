from ast import literal_eval

import pytest
from flask.json import jsonify

from .generate_test_data import FOLLOW_REQUEST_RECIPIENT, FOLLOW_REQUESTER_A, FOLLOW_REQUESTER_B, NONEXISTANT_USER_EMAIL, USER_BEING_FOLLOWED, USER_FOLLOWING


@pytest.mark.POST_follow_request
class TestPOSTFollow_request:
    def test_POST_follow_request_on_existing_users(self, app):
        response = app.post(
            f"/follow/request/{FOLLOW_REQUESTER_A['email']}/{FOLLOW_REQUEST_RECIPIENT['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: get request to assert follow relationship was created.
        # use endpoint to get all followings of user_following and check exists a follow to user being followed

    @pytest.mark.xfail
    # TODO: finish this test. Put on hold for now as niche usecase
    def test_POST_follow_request_on_non_existing_users(self, app):
        response = app.post(
            f"/follow/request/{FOLLOW_REQUESTER_A['email']}/{FOLLOW_REQUEST_RECIPIENT['email']}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_POST_follow_request_where_following_already_exists(self, app):
        raise NotImplementedError

    @pytest.mark.xfail
    def test_POST_follow_request_self(self, app):
        raise NotImplementedError


@pytest.mark.DELETE_follow_request
class TestDELETEFollow_request:
    def test_DELETE_existing_follow_request(self, app):
        response = app.delete(
            f"/follow/request/{FOLLOW_REQUESTER_A['email']}/{FOLLOW_REQUEST_RECIPIENT['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
        # TODO: get request to assert follow relationship was deleted.
        # use endpoint to get all followings of user_following and check does not exist a follow to user being followed

    @pytest.mark.xfail
    def test_DELETE_non_existing_follow_request(self, app):
        raise NotImplementedError


@pytest.mark.POST_follow_approve
class TestPOSTFollow_request_approve:
    def test_POST_follow_approve_on_existing_users(self, app):
        response = app.post(
            f"/follow/approve/{FOLLOW_REQUESTER_B['email']}/{FOLLOW_REQUEST_RECIPIENT['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: get request to assert follow relationship was created.
        # use endpoint to get all followings of user_following and check exists a follow to user being followed
"""
    @pytest.mark.xfail
    # TODO: finish this test. Put on hold for now as niche usecase
    def test_POST_follow_request_approve_on_non_existing_users(self, app):
        response = app.post(
            f"/follow/approve/{FOLLOW_REQUESTER_B['email']}/{FOLLOW_REQUEST_RECIPIENT['email']}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''
"""
