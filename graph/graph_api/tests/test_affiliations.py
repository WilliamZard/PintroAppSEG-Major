from ast import literal_eval

import pytest
from flask.json import jsonify

from .generate_test_data import AFFILIATION_REQUESTER, AFFILIATION_REQUEST_RECIPIENT


@pytest.mark.POST_affiliation_request
class TestPOSTAffiliation_request:
    def test_POST_affiliation_request_on_existing_business(self, app):
        response = app.post(
            f"/affiliation/request/{AFFILIATION_REQUESTER['email']}/{AFFILIATION_REQUEST_RECIPIENT['email']}")
        print(response)
        print(AFFILIATION_REQUESTER['email'])
        print(AFFILIATION_REQUEST_RECIPIENT['email'])
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
