import pytest
from .conftest import app
from .generate_test_data import FOLLOW_REQUESTER_A, FOLLOW_REQUESTER_B, AFFILIATION_REQUESTER_A, AFFILIATION_REQUEST_RECIPIENT, FOLLOW_REQUEST_RECIPIENT


@pytest.mark.POST_approve
class TestPOST:
    # TODO: add tests for entering a valid email
    # TODO: add tests for if given users exist or not
    # TODO: add tests for if given user type can make given request.
    #       e.g. users cannot make affiliation requests to businesses.
    def test_POST_approve_follow_request_with_valid_users(self, app):
        response = app.post(
            f"/approve/follow/{FOLLOW_REQUESTER_B['email']}/{FOLLOW_REQUEST_RECIPIENT['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: add get request for checking if FOLLOWrelationship was actually created

    def test_POST_approve_affiliation_request_with_valid_users(self, app):
        response = app.post(
            f"/approve/affiliation/{AFFILIATION_REQUESTER_A['email']}/{AFFILIATION_REQUEST_RECIPIENT['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: add get request for checking if AFFILIATION relationship was actually created
