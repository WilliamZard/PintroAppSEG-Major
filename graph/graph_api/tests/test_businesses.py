# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
# TODO: add logic for wether or not to populate db
from ast import literal_eval

import pytest
import json
from flask.json import jsonify

#from graph_api import create_app
from .conftest import app, populate_db
from .generate_test_data import Business, basic_business_node


@pytest.mark.GET_business
class TestGet:
    def test_get_business_with_valid_email_that_exists(self, app, populate_db):
        # Define Nodes
        business = Business(email='new_business@rona.com')._asdict()
        business.pop('tags')  # TODO: handle tests later
        business_node = basic_business_node(business)
        # Populate
        populate_db(nodes_to_create=[business_node])

        # Test
        response = app.get(f"/businesses/{business['email']}")
        assert response.status == '200 OK'
        response = response.get_json()
        assert len(response) == len(business)
        for key, value in business.items():
            assert key in response
            assert value == response[key]

    def test_get_business_with_valid_email_that_does_not_exist(self, app):
        nonexistant_business_email = 'does_not_exist@void.com'
        response = app.get(f"/businesses/{nonexistant_business_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_get_business_with_invalid_email(self, app):
        invalid_email = 'invalidemail.com'
        response = app.get(f"/businesses/{invalid_email}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.DELETE_business
class TestDelete:
    # TODO: some duplicate code here for each endpoint test. Refactor.
    def test_delete_business_with_valid_email_that_exists(self, app, populate_db):
        # Define Nodes
        business = Business(email='business_to_delete@rona.com')._asdict()
        business.pop('tags')  # TODO: handle tests later
        business_node = basic_business_node(business)
        # Populate
        populate_db(nodes_to_create=[business_node])

        email = business['email']
        response = app.delete(f"/businesses/{email}")
        assert response.status == '204 NO CONTENT'
        # TODO: consider using standard json.dumps instead of jsonify
        assert response.data == b''

        # Assert business was actually deleted in the database
        response = app.get(f"/businesses/{email}")
        assert response.status == '404 NOT FOUND'

    def test_delete_business_with_valid_email_that_does_not_exist(self, app):
        nonexistant_business_email = 'does_not_exist@void.com'
        response = app.delete(f"/businesses/{nonexistant_business_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_delete_business_with_invalid_email(self, app):
        invalid_email = "invalidemaill.com"
        response = app.delete(f"/businesses/{invalid_email}")
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
