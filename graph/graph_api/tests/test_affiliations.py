from ast import literal_eval

import pytest
from flask.json import jsonify

from .generate_test_data import AFFILIATION_REQUESTER, AFFILIATION_REQUEST_RECIPIENT


@pytest.mark.POST_affiliation_request
class TestPOSTAffiliation_request:
    def test_POST_affiliation_request_on_existing_business(self, app):
        response = app.post(
            f"/affiliation/request/{AFFILIATION_REQUESTER['email']}/{AFFILIATION_REQUEST_RECIPIENT['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: get request to assert follow relationship was created.
        # use endpoint to get all followings of user_following and check exists a follow to user being followed


@pytest.mark.DELETE_affiliation_request
class TestDELETEAffiliation_request:
    def test_DELETE_existing_affiliation_request(self, app):
        response = app.delete(
            f"/affiliation/request/{AFFILIATION_REQUESTER['email']}/{AFFILIATION_REQUEST_RECIPIENT['email']}")
        #print(response)
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
        # TODO: get request to assert follow relationship was deleted.
        # use endpoint to get all followings of user_following and check does not exist a follow to user being followed