import pytest
from flask.json import jsonify
import base64
from pathlib import Path
from ast import literal_eval

from .conftest import app, populate_db
from .generate_test_data import Space, basic_space_node


@pytest.mark.GET_space
class TestGet:
    def test_get_space_with_valid_email_that_exists(self, app, populate_db):
        # Generate data
        space = Space(email='space@test.com')._asdict()
        space_node = basic_space_node(space)

        populate_db(nodes_to_create=[space_node])

        # Test
        response = app.get(f"/spaces/{space['email']}")
        assert response.status == '200 OK'
        # TODO: change below assertion to check for length then each individual field.
        assert response.data == jsonify(space).data

    def test_get_space_with_valid_email_that_does_not_exist(self, app, populate_db):
        populate_db()
        nonexistant_space_email = "does@notexist.com"
        response = app.get(f"/spaces/{nonexistant_space_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_get_space_with_invalid_email(self, app, populate_db):
        populate_db()

        invalid_email = "doesnotexist.com"
        response = app.get(f"/spaces/{invalid_email}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    def test_GET_space_with_profile_image_has_its_true_profile_image(self, app, populate_db):
        # Generate test data
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image1.jpg"
        with image_path.open(mode="rb") as imageFile:
            image = base64.b64encode(imageFile.read())

        space = Space(email='space_test@gmail.com',
                      profile_image=image)._asdict()
        space_node = {'properties': dict(space), 'labels': 'Space'}

        populate_db(nodes_to_create=[space_node])

        # Test
        response = app.get(f"/spaces/{space['email']}")
        assert response.status == '200 OK'
        response = response.get_json()
        assert len(response) == len(space)
        assert literal_eval(response['profile_image']) == image


@pytest.mark.DELETE_space
class TestDelete:
    def test_delete_space_with_valid_email_that_exists(self, app, populate_db):
        # Generate data
        space = Space(email='space@test.com')._asdict()
        space_node = basic_space_node(space)

        populate_db(nodes_to_create=[space_node])

        # Test
        response = app.delete(f"/spaces/{space['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        # Assert space was actually deleted in the database
        response = app.get(f"/spaces/{space['email']}")
        assert response.status == '404 NOT FOUND'

    def test_delete_space_with_valid_email_that_does_not_exist(self, app, populate_db):
        populate_db()

        nonexistant_space_email = 'does@notexist.com'
        response = app.delete(f"/spaces/{nonexistant_space_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_delete_space_with_invalid_email(self, app, populate_db):
        populate_db()

        invalid_email = "testemail.com"
        response = app.delete(f"/spaces/{invalid_email}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.PUT_space
class TestPut:
    def test_put_space_with_valid_email_that_exists_with_an_image(self, app, populate_db):
        # Generate data
        space = Space(email='space@test.com')._asdict()
        space_node = basic_space_node(space)

        # new image for space
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image1.jpg"
        with image_path.open(mode="rb") as imageFile:
            new_image = base64.b64encode(imageFile.read())

        new_space = Space(email='space@test.com',
                          short_bio='not default', profile_image=str(new_image))._asdict()
        populate_db(nodes_to_create=[space_node])

        # Test
        response = app.put(
            f"/spaces/{space['email']}", json=dict(new_space))
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        response = app.get(
            f"/spaces/{space['email']}")
        response = response.get_json()
        assert len(response) == len(space)
        for key, value in new_space.items():
            assert key in response
            if(key == 'profile_image'):
                # Check that image bytes are the equal.
                assert new_image == literal_eval(response[key])
                continue
            assert value == response[key]

    def test_put_space_with_valid_email_that_does_not_exist(self, app, populate_db):
        # Generate Data
        nonexistant_email = 'does@notexist.com'
        new_space = Space(email='space@test.com',
                          short_bio='not default')._asdict()
        populate_db()

        # Test
        response = app.put(
            f"/spaces/{nonexistant_email}", json=dict(new_space))
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_put_space_with_invalid_email(self, app, populate_db):
        # Generate Data
        invalid_email = "invalidemail.com"
        new_space = Space(email='space@test.com',
                          short_bio='not default')._asdict()

        populate_db()

        # Test
        response = app.put(
            f"/spaces/{invalid_email}", json=dict(new_space))
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    # TODO: add test for validating payload


@pytest.mark.POST_space
class TestPost:
    def test_post_space_with_valid_payload_that_does_not_exist(self, app, populate_db):
        # Generate Data
        space = Space(email='new_space@test.com')._asdict()
        populate_db()

        # Test
        response = app.post(
            "/spaces/", json=dict(space))
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert space was actually created in the database
        response = app.get(f"/spaces/{space['email']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(space).data

    def test_post_space_with_valid_payload_that_exists(self, app, populate_db):
        # Generate Data
        space = Space(email='validspace@test.com')._asdict()
        space_node = basic_space_node(space)

        populate_db(nodes_to_create=[space_node])

        # Test
        response = app.post(
            "/spaces/", json=dict(space))
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_post_space_with_invalid_payload(self, app, populate_db):
        # Generate Data
        space = Space(email='invalidspactest.com')._asdict()
        populate_db()

        # Test
        response = app.post(
            "/spaces/", json=dict(space))
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'

    def test_POST_space_with_image_posts_correct_image_in_gcs(self, app, populate_db):
        # Generate Test Data
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image3.jpg"
        with image_path.open(mode="rb") as imageFile:
            image = base64.b64encode(imageFile.read())

        space_to_add = Space(email='space_test@gmail.com',
                             profile_image=str(image))._asdict()

        populate_db()

        # Test
        response = app.post("/spaces/", json=space_to_add)
        assert response.status == '201 CREATED'
        response = app.get(f"/spaces/{space_to_add['email']}")
        response = response.get_json()
        assert image == literal_eval(response['profile_image'])
