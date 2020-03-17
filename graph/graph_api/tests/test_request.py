import pytest
from .conftest import app
from .generate_test_data import FOLLOW_REQUESTER_A, FOLLOW_REQUESTER_B


@pytest.mark.POST_request
class TestPOST:
    def test_POST_follow_request_with_valid_users(self, app):
        response = app.post(
            f"/request/follow/{FOLLOW_REQUESTER_A['email']}/{FOLLOW_REQUESTER_B['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: add get request for checking if FOLLOW_REQUEST relationship was actually created

    def test_POST_affiliation_request_with_valid_users(self, app):
        pass


@pytest.mark.DELETE_request
class testDELETE:
    def test_DELETE_follow_request_with_valid_users(self, app):
        pass

    def test_DELETE_affiliation_request_with_valid_users(self, app):
        pass
