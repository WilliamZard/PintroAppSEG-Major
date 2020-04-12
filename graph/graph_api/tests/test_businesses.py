import json
import base64
from pathlib import Path
from ast import literal_eval
from flask import Flask

import pytest

from .conftest import app, populate_db
from .generate_test_data import Business, basic_business_node, Tag, basic_tag_node, User, basic_user_node


@pytest.mark.GET_business
class TestGet:
    def test_get_business_with_valid_email_that_exists(self, app: Flask, populate_db: None) -> None:
        # Define Nodes
        tag_a = Tag(name='King Slayyyying')._asdict()
        tag_a_node = {'properties': tag_a, 'labels': ['Tag', 'BusinessTag']}

        user_1 = User(email='affiliated_user_1@gmail.com')._asdict()
        user_1_node = {'properties': dict(user_1), 'labels': 'Person'}
        user_2 = User(email='affiliated_user_2@gmail.com')._asdict()
        user_2_node = {'properties': dict(user_2), 'labels': 'Person'}

        business_kwargs = dict(email='new_business@rona.com',
                               tags=[tag_a['name']])
        business = Business(**business_kwargs)._asdict()
        business_node = basic_business_node(business)

        # Define relationships
        tagged_a = {
            's_node_properties': {'email': business['email']}, 's_node_labels': 'Business',
            'e_node_properties': {'name': tag_a['name']}, 'e_node_labels': 'Tag',
            'relationship_type': 'TAGGED'}
        affiliated_with_1 = {
            's_node_properties': {'email': user_1['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': business['email']}, 'e_node_labels': 'Business',
            'relationship_type': 'AFFILIATED_WITH'}
        affiliated_with_2 = {
            's_node_properties': {'email': user_2['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': business['email']}, 'e_node_labels': 'Business',
            'relationship_type': 'AFFILIATED_WITH'}
        # Populate
        populate_db(nodes_to_create=[business_node, tag_a_node, user_1_node, user_2_node],
                    relationships_to_create=[tagged_a, affiliated_with_1, affiliated_with_2])

        # Test
        response = app.get(f"/businesses/{business['email']}")
        assert response.status == '200 OK'
        response = response.get_json()
        business_kwargs['team_members'] = [user_1['email'], user_2['email']]
        business = Business(**business_kwargs)._asdict()
        assert len(response) == len(business)
        for key, value in business.items():
            assert key in response
            if isinstance(response[key], list):
                assert len(value) == len(response[key])
                for item in value:
                    assert item in response[key]
            else:
                assert value == response[key]

    def test_get_business_with_valid_email_that_does_not_exist(self, app: Flask) -> None:
        nonexistant_business_email = 'does_not_exist@void.com'
        response = app.get(f"/businesses/{nonexistant_business_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_get_business_with_invalid_email(self, app: Flask):
        invalid_email = 'invalidemail.com'
        response = app.get(f"/businesses/{invalid_email}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    def test_GET_business_with_profile_image_has_its_true_profile_image(self, app: Flask, populate_db: None) -> None:
        # Generate test data
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image1.jpg"
        with image_path.open(mode="rb") as imageFile:
            image = base64.b64encode(imageFile.read())

        business = Business(email='business_test@gmail.com',
                            profile_image=image)._asdict()
        business_node = {'properties': dict(business), 'labels': 'Business'}

        populate_db(nodes_to_create=[business_node])

        # Test
        response = app.get(f"/businesses/{business['email']}")
        assert response.status == '200 OK'
        response = response.get_json()
        assert len(response) == len(business)
        assert literal_eval(response['profile_image']) == image


@pytest.mark.DELETE_business
class TestDelete:
    def test_delete_business_with_valid_email_that_exists(self, app: Flask, populate_db: None) -> None:
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

    def test_delete_business_with_valid_email_that_does_not_exist(self, app: Flask) -> None:
        nonexistant_business_email = 'does_not_exist@void.com'
        response = app.delete(f"/businesses/{nonexistant_business_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_delete_business_with_invalid_email(self, app: Flask) -> None:
        invalid_email = "invalidemaill.com"
        response = app.delete(f"/businesses/{invalid_email}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.PUT_business
class TestPut:
    def test_put_business_with_valid_email_that_exists_and_new_image(self, app: Flask, populate_db: None) -> None:
        # Define Nodes
        business = Business(email='business_to_update@rona.com')._asdict()
        business_node = basic_business_node(business)

        tag = Tag(name='TestBusinessTag')._asdict()
        tag_node = basic_tag_node(tag, 'Tag:BusinessTag')

        # new image for business
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image1.jpg"
        with image_path.open(mode="rb") as imageFile:
            new_image = base64.b64encode(imageFile.read())

        new_business = Business(
            email=business['email'], full_name='new full name', phone='phone', location='new location', tags=[tag['name']], profile_image=str(new_image))._asdict()

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
            if(key == 'profile_image'):
                # Check that image bytes are the equal.
                assert new_image == literal_eval(response[key])
                continue
            assert value == response[key]

    def test_put_business_with_valid_email_that_does_not_exist(self, app: Flask) -> None:
        nonexistant_business_email = 'does_not_exist@void.com'
        new_business_fields = dict(
            full_name='new full name', phone='phone', location='new location')
        response = app.put(
            f"/businesses/{nonexistant_business_email}", json=new_business_fields)
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_put_business_with_invalid_email(self, app: Flask) -> None:
        invalid_email = 'invalidemail.com'
        new_business_fields = dict(
            full_name='new full name', phone='phone', location='new location')
        response = app.put(
            f"/businesses/{invalid_email}", json=new_business_fields)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.POST_business
class TestPost:
    def test_post_business_with_valid_payload_that_does_not_exist(self, app: Flask, populate_db: None) -> None:
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

    def test_post_business_with_valid_payload_that_exists(self, app: Flask, populate_db: None) -> None:
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

    def test_post_business_with_invalid_payload(self, app: Flask) -> None:
        invalid_business = Business(email='bademail.com')._asdict()
        response = app.post(
            "/businesses/", json=dict(invalid_business))
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'

    def test_POST_business_with_image_posts_correct_image_in_gcs(self, app: Flask) -> None:
        # Generate Test Data
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image3.jpg"
        with image_path.open(mode="rb") as imageFile:
            image = base64.b64encode(imageFile.read())

        business_to_add = Business(
            email='business_test@gmail.com', profile_image=str(image))._asdict()

        # Test
        response = app.post("/businesses/", json=business_to_add)
        assert response.status == '201 CREATED'
        response = app.get(f"/businesses/{business_to_add['email']}")
        response = response.get_json()
        assert image == literal_eval(response['profile_image'])
