import pytest
from flask.json import jsonify

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
    def test_put_space_with_valid_email_that_exists(self, app, populate_db):
        # Generate data
        space = Space(email='space@test.com')._asdict()
        space_node = basic_space_node(space)

        new_space = Space(email='space@test.com',
                          short_bio='not default')._asdict()
        populate_db(nodes_to_create=[space_node])

        # Test
        response = app.put(
            f"/spaces/{space['email']}", json=dict(new_space))
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

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
