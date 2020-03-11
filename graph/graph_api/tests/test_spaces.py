# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
# TODO: add logic for wether or not to populate db
from ast import literal_eval

import pytest
from flask.json import jsonify

#from graph_api import create_app
from .conftest import app

from .generate_test_data import (INVALID_EMAIL, INVALID_SPACE_TO_BE_CREATED,
                                 NONEXISTANT_SPACE_EMAIL, VALID_SPACE,
                                 VALID_SPACE_TO_BE_CREATED,
                                 VALID_SPACE_TO_BE_DELETED,
                                 VALID_SPACE_TO_BE_UPDATED,
                                 VALID_SPACE_TO_BE_UPDATED_NEW_FIELDS,
                                 SPACE_WITH_THREE_FOLLOWINGS,
                                 SPACE_WITH_TWO_FOLLOWINGS,
                                 SPACE_WITH_ONE_FOLLOWING,
                                 SPACE_WITH_NO_FOLLOWINGS, SPACE_WITH_FOLLOWINGS_THAT_HAVE_POSTS)



@pytest.mark.GET_space
class TestGet:
    def test_get_space_with_valid_email_that_exists(self, app):
        response = app.get(f"/spaces/{VALID_SPACE['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(VALID_SPACE).data

    
    def test_get_space_with_valid_email_that_does_not_exist(self, app):
        response = app.get(f"/spaces/{NONEXISTANT_SPACE_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_get_space_with_invalid_email(self, app):
        response = app.get(f"/spaces/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.DELETE_space
class TestDelete:
    # TODO: some duplicate code here for each endpoint test. Refactor.
    def test_delete_space_with_valid_email_that_exists(self, app):
        email = VALID_SPACE_TO_BE_DELETED['email']
        response = app.delete(f"/spaces/{email}")
        assert response.status == '204 NO CONTENT'
        # TODO: consider using standard json.dumps instead of jsonify
        assert response.data == b''

        # Assert space was actually deleted in the database
        response = app.get(f"/spaces/{email}")
        assert response.status == '404 NOT FOUND'

    def test_delete_space_with_valid_email_that_does_not_exist(self, app):
        response = app.delete(f"/spaces/{NONEXISTANT_SPACE_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_delete_space_with_invalid_email(self, app):
        response = app.delete(f"/spaces/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.PUT_space
class TestPut:
    def test_put_space_with_valid_email_that_exists(self, app):
        response = app.put(
            f"/spaces/{VALID_SPACE_TO_BE_UPDATED['email']}", json=VALID_SPACE_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

    def test_put_space_with_valid_email_that_does_not_exist(self, app):
        response = app.put(
            f"/spaces/{NONEXISTANT_SPACE_EMAIL}", json=VALID_SPACE_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_put_space_with_invalid_email(self, app):
        response = app.put(
            f"/spaces/{INVALID_EMAIL}", json=VALID_SPACE_TO_BE_UPDATED_NEW_FIELDS)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    # TODO: add test for validating payload


@pytest.mark.POST_space
class TestPost:
    def test_post_space_with_valid_payload_that_does_not_exist(self, app):
        response = app.post(
            "/spaces/", json=VALID_SPACE_TO_BE_CREATED)
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert space was actually created in the database
        response = app.get(f"/spaces/{VALID_SPACE_TO_BE_CREATED['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(VALID_SPACE_TO_BE_CREATED).data

    def test_post_space_with_valid_payload_that_exists(self, app):
        response = app.post(
            "/spaces/", json=VALID_SPACE)
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_post_space_with_invalid_payload(self, app):
        response = app.post(
            "/spaces/", json=INVALID_SPACE_TO_BE_CREATED)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'
