import json

import pytest

from .conftest import app, populate_db
from .generate_test_data import Business, basic_business_node, Tag, basic_tag_node


@pytest.mark.GET_business
class TestGet:
    def test_get_business_with_valid_email_that_exists(self, app, populate_db):
        # Define Nodes
        tag_a = Tag(name='King Slaying')._asdict()
        tag_a_node = {'properties': tag_a, 'labels': ['Tag', 'BusinessTag']}

        business = Business(email='new_business@rona.com',
                            tags=[tag_a['name']])._asdict()
        business_node = basic_business_node(business)

        # Define relationships
        tagged_a = {
            's_node_properties': {'email': business['email']}, 's_node_labels': 'Business',
            'e_node_properties': {'name': tag_a['name']}, 'e_node_labels': 'Tag',
            'relationship_type': 'TAGGED'}
        # Populate
        populate_db(nodes_to_create=[
                    business_node, tag_a_node], relationships_to_create=[tagged_a])

        # Test
        response = app.get(f"/businesses/{business['email']}")
        assert response.status == '200 OK'
        response = response.get_json()
        assert len(response) == len(business)
        for key, value in business.items():
            assert key in response
            assert value == response[key]

    def test_get_business_with_valid_email_that_does_not_exist(self, app, populate_db):
        populate_db()

        nonexistant_business_email = 'does_not_exist@void.com'
        response = app.get(f"/businesses/{nonexistant_business_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_get_business_with_invalid_email(self, app, populate_db):
        populate_db()

        invalid_email = 'invalidemail.com'
        response = app.get(f"/businesses/{invalid_email}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.DELETE_business
class TestDelete:
    # TODO: some duplicate code here for each endpoint test. Refactor.
    def test_delete_business_with_valid_email_that_exists(self, app, populate_db):
        # Define Nodes
        tag_a = Tag(name='King Slaying')._asdict()
        tag_a_node = {'properties': tag_a, 'labels': ['Tag', 'BusinessTag']}

        business = Business(email='new_business@rona.com',
                            tags=[tag_a['name']])._asdict()
        business_node = basic_business_node(business)

        # Define relationships
        tagged_a = {
            's_node_properties': {'email': business['email']}, 's_node_labels': 'Business',
            'e_node_properties': {'name': tag_a['name']}, 'e_node_labels': 'Tag',
            'relationship_type': 'TAGGED'}
        # Populate
        populate_db(nodes_to_create=[
                    business_node, tag_a_node], relationships_to_create=[tagged_a])

        email = business['email']
        response = app.delete(f"/businesses/{email}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        # Assert business was actually deleted in the database
        response = app.get(f"/businesses/{email}")
        assert response.status == '404 NOT FOUND'

    def test_delete_business_with_valid_email_that_does_not_exist(self, app, populate_db):
        populate_db()

        nonexistant_business_email = 'does_not_exist@void.com'
        response = app.delete(f"/businesses/{nonexistant_business_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_delete_business_with_invalid_email(self, app, populate_db):
        populate_db()

        invalid_email = "invalidemaill.com"
        response = app.delete(f"/businesses/{invalid_email}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.PUT_business
class TestPut:
    def test_put_business_with_valid_email_that_exists(self, app, populate_db):
        # Define Nodes
        business = Business(email='business_to_update@rona.com')._asdict()
        business_node = basic_business_node(business)

        tag = Tag(name='TestBusinessTag')._asdict()
        tag_node = basic_tag_node(tag, 'Tag:BusinessTag')

        new_business = Business(
            email=business['email'], full_name='new full name', phone='phone', location='new location', tags=[tag['name']])._asdict()
        # Populate
        populate_db(nodes_to_create=[business_node, tag_node])

        response = app.put(
            f"/businesses/{business['email']}", json=dict(new_business))
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        response = app.get(
            f"/businesses/{business['email']}")
        response = response.get_json()
        assert len(response) == len(business)
        for key, value in new_business.items():
            assert key in response
            assert value == response[key]

    def test_put_business_with_valid_email_that_does_not_exist(self, app, populate_db):
        populate_db()
        nonexistant_business_email = 'does_not_exist@void.com'
        new_business_fields = dict(
            full_name='new full name', phone='phone', location='new location')
        response = app.put(
            f"/businesses/{nonexistant_business_email}", json=new_business_fields)
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_put_business_with_invalid_email(self, app, populate_db):
        populate_db()
        invalid_email = 'invalidemail.com'
        new_business_fields = dict(
            full_name='new full name', phone='phone', location='new location')
        response = app.put(
            f"/businesses/{invalid_email}", json=new_business_fields)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

        # TODO: add test for validating payload


@pytest.mark.POST_business
class TestPost:
    def test_post_business_with_valid_payload_that_does_not_exist(self, app, populate_db):
        # Define Nodes
        tag_a = Tag(name='King Slaying')._asdict()
        tag_a_node = {'properties': tag_a, 'labels': ['Tag', 'BusinessTag']}

        business = Business(email='business_to_create@rona.com', tags=[
                            tag_a['name']])._asdict()
        populate_db(nodes_to_create=[tag_a_node])

        # Populate
        response = app.post(
            "/businesses/", json=dict(business))
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert business was actually created in the database
        response = app.get(
            f"/businesses/{business['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == len(business)
        for key, value in business.items():
            assert key in json
            assert value == json[key]

    def test_post_business_with_valid_payload_that_exists(self, app, populate_db):
        # Define Nodes
        business = Business(email='business_to_create@rona.com')._asdict()
        business_node = basic_business_node(business)

        # Populate
        populate_db(nodes_to_create=[business_node])

        # Test
        response = app.post(
            "/businesses/", json=dict(business))
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_post_business_with_invalid_payload(self, app, populate_db):
        populate_db()
        invalid_business = Business(email='bademail.com')._asdict()
        response = app.post(
            "/businesses/", json=dict(invalid_business))
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'
