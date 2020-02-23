# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
# TODO: add logic for wether or not to populate db
from ast import literal_eval

import pytest
from flask.json import jsonify

from graph_api import create_app
from graph_api.apis.users import UserSchema

from .generate_test_data import (NONEXISTANT_USER_EMAIL,
                                 VALID_USER, VALID_USER_TO_BE_DELETED, INVALID_EMAIL,
                                 VALID_USER_TO_BE_UPDATED, VALID_USER_TO_BE_UPDATED_NEW_FIELDS,
                                 populate_db)


# TODO: consider changing scope of fixture so client object does not creating every time.
@pytest.fixture
def app():
    app = create_app()
    app.testing = True

    # TODO: populate database when testing.
    print("ey!")
    with app.test_client() as client:
        # NOTE commented out populate db
       # populate_db(rewrite_test_data=True)
        yield client

# TODO: some duplicate code here for each endpoint test. Refactor.


# TODO: below is an attempt as reducing duplicate code in tests.
# Failed because it leads to pytest output being less informative.
# Come back to this later.
"""
@pytest.mark.skip
def test_api_endpoint(app, email, status, response_data):
    response = app.get(f"/users/{email}")
    assert response.status == status
    # TODO: consider using standard json.dumps instead of jsonify
    assert response.data == jsonify(response_data).data
"""


class TestGet:
    def test_get_user_with_valid_email_that_exists(self, app):
        response = app.get(f"/users/{VALID_USER['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(VALID_USER).data

    def test_get_user_with_valid_email_that_does_not_exist(self, app):
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == jsonify({}).data

    def test_get_user_with_invalid_email(self, app):
        response = app.get(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 Invalid Email'
        assert response.data == jsonify({}).data


class TestDelete:
    # TODO: some duplicate code here for each endpoint test. Refactor.
    def test_delete_user_with_valid_email_that_exists(self, app):
        email = VALID_USER_TO_BE_DELETED['email']
        response = app.delete(f"/users/{email}")
        assert response.status == '204 OK'
        # TODO: consider using standard json.dumps instead of jsonify
        assert response.data == jsonify(VALID_USER_TO_BE_DELETED).data

        # Assert user was actually deleted in the database
        response = app.get(f"/users/{email}")
        assert response.status == '404 NOT FOUND'

    def test_delete_user_with_valid_email_that_does_not_exist(self, app):
        response = app.delete(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == jsonify({}).data

    def test_delete_user_with_invalid_email(self, app):
        response = app.delete(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 Invalid Email'
        assert response.data == jsonify({}).data


class TestPut:
    def test_put_user_with_valid_email_that_exists(self, app):
        response = app.put(
            f"/users/{VALID_USER_TO_BE_UPDATED['email']}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '204 No Content'
        assert response.data == jsonify({}).data

    def test_put_user_with_valid_email_that_does_not_exist(self, app):
        response = app.put(
            f"/users/{VALID_USER_TO_BE_UPDATED['email']}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '404 NOT FOUND'
        assert response.data == jsonify({}).data

    def test_put_user_with_invalid_email(self, app):
        response = app.put(
            f"/users/{VALID_USER_TO_BE_UPDATED['email']}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '422 Invalid Email'
        assert response.data == jsonify({}).data
