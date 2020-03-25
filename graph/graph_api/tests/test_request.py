import pytest
from .conftest import app
from .generate_test_data import FOLLOW_REQUESTER_A, FOLLOW_REQUESTER_B, AFFILIATION_REQUESTER_A, AFFILIATION_REQUEST_RECIPIENT, FOLLOW_REQUEST_RECIPIENT


@pytest.mark.POST_request
class TestPOST:
    # TODO: add tests for entering a valid email
    # TODO: add tests for if given users exist or not
    # TODO: add tests for if given user type can make given request.
    #       e.g. users cannot make affiliation requests to businesses.
    def test_POST_follow_request_with_valid_users(self, app):
        response = app.post(
            f"/request/follow/{FOLLOW_REQUESTER_A['email']}/{FOLLOW_REQUESTER_B['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: add get request for checking if FOLLOW_REQUEST relationship was actually created

    def test_POST_affiliation_request_with_valid_users(self, app):
        response = app.post(
            f"/request/affiliation/{AFFILIATION_REQUESTER_A['email']}/{AFFILIATION_REQUEST_RECIPIENT['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: add get request for checking if FOLLOW_REQUEST relationship was actually created


@pytest.mark.DELETE_request
class TestDELETE:
    def test_DELETE_follow_request_with_valid_users(self, app):
        response = app.delete(
            f"/request/follow/{FOLLOW_REQUESTER_B['email']}/{FOLLOW_REQUEST_RECIPIENT['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        # TODO: add get request for checking if FOLLOW_REQUEST relationship was actually created

    def test_DELETE_affiliation_request_with_valid_users(self, app):
        # TODO: fix test not passing when all tests are run
        response = app.delete(
            f"/request/affiliation/{AFFILIATION_REQUESTER_A['email']}/{AFFILIATION_REQUEST_RECIPIENT['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
