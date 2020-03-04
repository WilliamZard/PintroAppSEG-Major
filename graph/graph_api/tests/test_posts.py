# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
from ast import literal_eval

import pytest
from flask.json import jsonify
from jsonmerge import merge

from graph_api import create_app
from graph_api.apis.users import UserSchema
from graph_api.apis.neo4j_ops import get_list_of_user_post_dates
from .conftest import app

from .generate_test_data import (USER_WITH_MULTIPLE_POSTS, USER_POST_C, USER_POST_B, USER_POST_A,
                                 POST_UPDATE_A, POST_UPDATE_B)
from .test_data.posts import EXISTING_POST, NON_EXISTING_POST_UUID, POST_TO_BE_UPDATED_THAT_EXISTS, POST_TO_BE_CREATED


@pytest.mark.get_post
class TestGet:
    def test_get_post_that_exists(self, app):
        response = app.get(f"/posts/{EXISTING_POST['uuid']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(EXISTING_POST).data

    def test_get_post_that_does_not_exist(self, app):
        response = app.get(f"/posts/{NON_EXISTING_POST_UUID}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''


@pytest.mark.put_post
class TestPut:
    # TODO: save UUID of that post in testing data
    def test_put_existing_post(self, app):
        response = app.put(
            f"/posts/{POST_TO_BE_UPDATED_THAT_EXISTS['uuid']}", json=POST_TO_BE_UPDATED_THAT_EXISTS['content'])
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
        # TODO: get request and assertion to check correct update
        # TODO: assert modified was changed properly
        # TODO: assert created was not changed
        # TODO: created and modified should not be writable. How can we do this?

    def test_put_non_existent_post(self, app):
        response = app.put(
            f"/posts/{NON_EXISTING_POST_UUID}", json=POST_TO_BE_UPDATED_THAT_EXISTS['content'])
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    # TODO: test validation. Add character limit to post schema.
    def test_put_existing_post_invalid_changes(self, app):
        pass
        # TODO: define invalid changes

# TODO: use upper case for HTTP method to avoid confusion. Eg test_POST_post...
@pytest.mark.post_post
class TestPost:
    # TODO: add created and modified related assertions like in above TODOs
    def test_post_post_with_valid_payload(self, app):
        response = app.post(
            f"/posts/", json=POST_TO_BE_CREATED)
        assert response.status == '201 CREATED'
        assert response.data == b''

    @pytest.mark.skip
    def test_post_post_with_invalid_payload(self, app):
        response = app.post(
            f"/posts/", json={'content': '', 'user_email': POST_TO_BE_CREATED['user_email']})
        assert response.status == '404 NOT FOUND'
        raise NotImplementedError

    @pytest.mark.skip
    def test_post_post_creates_posted_relation(self, app):
        raise NotImplementedError


@pytest.mark.delete_post
class TestDelete:
    def test_delete_existing_post(self, app):
        raise NotImplementedError

    def test_delete_non_existing_post(self, app):
        raise NotImplementedError

    def test_delete_existing_post_deletes_posted_relation(self, app):
        raise NotImplementedError

    """def test_that_deleting_a_post_should_succeed(self, app):
        # TODO TEST THIS ENDPOINT TOO.
        posts_response = app.get(f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}")

        post_id = posts_response.get_json()[0]['id']

        response = app.delete(
            f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}", json={'post_id': post_id})  # TODO find a way to have it all set in POST_UPDATE_B and A
        assert response.status == '204 NO CONTENT'
        assert response.data == b''"""
