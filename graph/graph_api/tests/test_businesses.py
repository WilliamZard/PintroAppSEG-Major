# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
# TODO: add logic for wether or not to populate db
from ast import literal_eval

import pytest
from flask.json import jsonify

#from graph_api import create_app
from .conftest import app

from .generate_test_data import (INVALID_EMAIL, INVALID_BUSINESS_TO_BE_CREATED,
                                 NONEXISTANT_BUSINESS_EMAIL, VALID_BUSINESS,
                                 VALID_BUSINESS_TO_BE_CREATED,
                                 VALID_BUSINESS_TO_BE_DELETED,
                                 VALID_BUSINESS_TO_BE_UPDATED,
                                 VALID_BUSINESS_TO_BE_UPDATED_NEW_FIELDS,
                                 BUSINESS_WITH_THREE_FOLLOWINGS,
                                 BUSINESS_WITH_TWO_FOLLOWINGS,
                                 BUSINESS_WITH_ONE_FOLLOWING,
                                 BUSINESS_WITH_NO_FOLLOWINGS, BUSINESS_WITH_FOLLOWINGS_THAT_HAVE_POSTS,
                                 AFFILIATION_REQUEST_RECIPIENT)


@pytest.mark.GET_business
class TestGet:
    def test_get_business_with_valid_email_that_exists(self, app):
        response = app.get(f"/businesses/{VALID_BUSINESS['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(VALID_BUSINESS).data

    def test_get_business_with_valid_email_that_does_not_exist(self, app):
        response = app.get(f"/businesses/{NONEXISTANT_BUSINESS_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_get_business_with_invalid_email(self, app):
        response = app.get(f"/businesses/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.DELETE_business
class TestDelete:
    # TODO: some duplicate code here for each endpoint test. Refactor.
    def test_delete_business_with_valid_email_that_exists(self, app):
        email = VALID_BUSINESS_TO_BE_DELETED['email']
        response = app.delete(f"/businesses/{email}")
        assert response.status == '204 NO CONTENT'
        # TODO: consider using standard json.dumps instead of jsonify
        assert response.data == b''

        # Assert business was actually deleted in the database
        response = app.get(f"/businesses/{email}")
        assert response.status == '404 NOT FOUND'

    def test_delete_business_with_valid_email_that_does_not_exist(self, app):
        response = app.delete(f"/businesses/{NONEXISTANT_BUSINESS_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_delete_business_with_invalid_email(self, app):
        response = app.delete(f"/businesses/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.PUT_business
class TestPut:
    def test_put_business_with_valid_email_that_exists(self, app):
        response = app.put(
            f"/businesses/{VALID_BUSINESS_TO_BE_UPDATED['email']}", json=VALID_BUSINESS_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

    def test_put_business_with_valid_email_that_does_not_exist(self, app):
        response = app.put(
            f"/businesses/{NONEXISTANT_BUSINESS_EMAIL}", json=VALID_BUSINESS_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_put_business_with_invalid_email(self, app):
        response = app.put(
            f"/businesses/{INVALID_EMAIL}", json=VALID_BUSINESS_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    # TODO: add test for validating payload


@pytest.mark.POST_business
class TestPost:
    def test_post_business_with_valid_payload_that_does_not_exist(self, app):
        response = app.post(
            "/businesses/", json=VALID_BUSINESS_TO_BE_CREATED)
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert business was actually created in the database
        response = app.get(
            f"/businesses/{VALID_BUSINESS_TO_BE_CREATED['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == len(VALID_BUSINESS_TO_BE_CREATED)
        for field in VALID_BUSINESS_TO_BE_CREATED:
            assert field in json

    def test_post_business_with_valid_payload_that_exists(self, app):
        response = app.post(
            "/businesses/", json=VALID_BUSINESS)
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_post_business_with_invalid_payload(self, app):
        response = app.post(
            "/businesses/", json=INVALID_BUSINESS_TO_BE_CREATED)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'
