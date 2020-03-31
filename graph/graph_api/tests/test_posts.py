import uuid

import pytest
from flask.json import jsonify

from .conftest import app, populate_db
from .test_data.posts import Post
from .test_data.users import User


@pytest.mark.GET_post
class TestGET:
    def test_GET_post_that_exists(self, app, populate_db):
        # Generate Test Data
        post = Post(content='content_x')._asdict()
        posts = [{'properties': dict(post), 'labels': 'Post'}]
        populate_db(nodes_to_create=posts)

        # Test
        response = app.get(f"/posts/{post['uuid']}")
        assert response.status == '200 OK'
        # TODO: change how this is done
        assert response.data == jsonify(post).data

    def test_GET_post_that_does_not_exist(self, app, populate_db):
        populate_db()
        non_existing_uuid = uuid.uuid4()
        response = app.get(f"/posts/{non_existing_uuid}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''


@pytest.mark.PUT_post
class TestPUT:
    def test_PUT_existing_post(self, app, populate_db):
        # Generate Test Data
        post = Post(content='content_x')._asdict()
        new_post = Post(content='content_y')._asdict()
        posts = [{'properties': dict(post), 'labels': 'Post'}]
        populate_db(nodes_to_create=posts)

        # Test
        response = app.put(
            f"/posts/{post['uuid']}", json=post['content'])
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
        # TODO: assert modified was changed properly for all put tests
        # TODO: assert created was not changed for all put tests
        # TODO: get request and assertion to check correct update

    def test_PUT_non_existent_post(self, app, populate_db):
        populate_db()
        post = Post(content='content_x')._asdict()

        response = app.put(
            f"/posts/{uuid.uuid4()}", json=post['content'])
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_PUT_existing_post_invalid_changes(self, app):
        raise NotImplementedError


@pytest.mark.POST_post
class TestPOST:
    # TODO: assert modified was changed properly for all put tests
    # TODO: assert created was not changed for all put tests
    # TODO: get request and assertion to check correct update
    def test_POST_post_with_valid_payload(self, app, populate_db):
        # Generate Test Data
        post = Post(content='content_x')._asdict()
        user = User(email='created_post@post.com')._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}
        payload = {'content': post['content'], 'user_email': user['email']}

        populate_db(nodes_to_create=[user_node])

        # Test
        response = app.post(
            f"/posts/", json=payload)
        assert response.status == '201 CREATED'
        assert response.data == b''

    def test_POST_post_with_invalid_payload(self, app, populate_db):
        user_email = 'test@test.com'
        populate_db()

        response = app.post(
            f"/posts/", json={'content': '', 'user_email': user_email})
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b"Post content length must be between 1 and 300."

    @pytest.mark.xfail
    def test_POST_post_creates_posted_relation(self, app):
        raise NotImplementedError


@pytest.mark.DELETE_post
class TestDELETE:
    def test_DELETE_existing_post(self, app, populate_db):
        # Generate Test Data
        # Nodes
        post = Post(content='content_x')._asdict()
        post_node = {'properties': dict(post), 'labels': 'Post'}
        user = User(email='created_post@post.com')._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}

        # Relationships
        posted = {
            's_node_properties': {'email': user['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'uuid': post['uuid']}, 'e_node_labels': 'Post',
            'relationship_type': 'POSTED'}

        populate_db(nodes_to_create=[
                    user_node, post_node], relationships_to_create=[posted])

        # Test
        response = app.delete(
            f"/posts/{post['uuid']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

    def test_DELETE_non_existing_post(self, app, populate_db):
        populate_db()
        response = app.delete(
            f"/posts/{uuid.uuid4()}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_DELETE_existing_post_deletes_posted_relation(self, app):
        raise NotImplementedError
