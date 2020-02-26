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
                                 VALID_USER_TO_BE_CREATED, INVALID_USER_TO_BE_CREATED,
                                 populate_db, clear_db)


# TODO: consider changing scope of fixture so client object does not creating every time.
@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.testing = True

    # TODO: right now this populates and clears the database for all tests, as opposed to every test
    # Not sure which if this should happen per test or per module.
    # Figure this out.
    with app.test_client() as client:
        # NOTE commented out populate db
        populate_db(rewrite_test_data=True)
        yield client
    clear_db()

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


@pytest.mark.get
class TestGet:
    def test_get_user_with_valid_email_that_exists(self, app):
        response = app.get(f"/users/{VALID_USER['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(VALID_USER).data

    def test_get_user_with_valid_email_that_does_not_exist(self, app):
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_get_user_with_invalid_email(self, app):
        response = app.get(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.delete
class TestDelete:
    # TODO: some duplicate code here for each endpoint test. Refactor.
    def test_delete_user_with_valid_email_that_exists(self, app):
        email = VALID_USER_TO_BE_DELETED['email']
        response = app.delete(f"/users/{email}")
        assert response.status == '204 NO CONTENT'
        # TODO: consider using standard json.dumps instead of jsonify
        assert response.data == b''

        # Assert user was actually deleted in the database
        response = app.get(f"/users/{email}")
        assert response.status == '404 NOT FOUND'

    def test_delete_user_with_valid_email_that_does_not_exist(self, app):
        response = app.delete(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_delete_user_with_invalid_email(self, app):
        response = app.delete(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.put
class TestPut:
    def test_put_user_with_valid_email_that_exists(self, app):
        response = app.put(
            f"/users/{VALID_USER_TO_BE_UPDATED['email']}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

    def test_put_user_with_valid_email_that_does_not_exist(self, app):
        response = app.put(
            f"/users/{NONEXISTANT_USER_EMAIL}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_put_user_with_invalid_email(self, app):
        response = app.put(
            f"/users/{INVALID_EMAIL}", json=VALID_USER_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    # TODO: add test for validating payload


@pytest.mark.post
class TestPost:
    def test_post_user_with_valid_payload_that_does_not_exist(self, app):
        response = app.post(
            "/users/", json=VALID_USER_TO_BE_CREATED)
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert user was actually created in the database
        response = app.get(f"/users/{VALID_USER_TO_BE_CREATED['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(VALID_USER_TO_BE_CREATED).data

    def test_post_user_with_valid_payload_that_exists(self, app):
        response = app.post(
            "/users/", json=VALID_USER)
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_post_user_with_invalid_payload(self, app):   
        response = app.post(
            "/users/", json=INVALID_USER_TO_BE_CREATED)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'
