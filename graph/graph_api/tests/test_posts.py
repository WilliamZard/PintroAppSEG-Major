# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
from ast import literal_eval

import pytest
from flask.json import jsonify
from jsonmerge import merge

from .conftest import app
from .generate_test_data import (POST_UPDATE_A, POST_UPDATE_B, USER_POST_A,
                                 USER_POST_B, USER_POST_C,
                                 USER_WITH_MULTIPLE_POSTS)
from .test_data.posts import (EXISTING_POST, NON_EXISTING_POST_UUID,
                              POST_TO_BE_CREATED,
                              POST_TO_BE_UPDATED_THAT_EXISTS)


@pytest.mark.GET_post
class TestGET:
    def test_GET_post_that_exists(self, app):
        response = app.get(f"/posts/{EXISTING_POST['uuid']}")
        assert response.status == '200 OK'
        assert response.data == jsonify(EXISTING_POST).data

    def test_GET_post_that_does_not_exist(self, app):
        response = app.get(f"/posts/{NON_EXISTING_POST_UUID}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''


@pytest.mark.PUT_post
class TestPut:
    # TODO: save UUID of that post in testing data
    def test_PUT_existing_post(self, app):
        response = app.put(
            f"/posts/{POST_TO_BE_UPDATED_THAT_EXISTS['uuid']}", json=POST_TO_BE_UPDATED_THAT_EXISTS['content'])
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
        # TODO: get request and assertion to check correct update
        # TODO: assert modified was changed properly
        # TODO: assert created was not changed
        # TODO: created and modified should not be writable. How can we do this?

    def test_PUT_non_existent_post(self, app):
        response = app.put(
            f"/posts/{NON_EXISTING_POST_UUID}", json=POST_TO_BE_UPDATED_THAT_EXISTS['content'])
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    # TODO: test validation. Add character limit to post schema.
    def test_PUT_existing_post_invalid_changes(self, app):
        pass
        # TODO: define invalid changes

# TODO: use upper case for HTTP method to avoid confusion. Eg test_POST_post...
@pytest.mark.POST_post
class TestPOST:
    # TODO: add created and modified related assertions like in above TODOs
    # TODO: should UUID be returned for user to use? Could run a get request and compare that to response of POST request.
    def test_POST_post_with_valid_payload(self, app):
        response = app.post(
            f"/posts/", json=POST_TO_BE_CREATED)
        assert response.status == '201 CREATED'
        assert response.data == b''
        # TODO: run get requests to make sure it was created

    @pytest.mark.skip
    # TODO: assert modified changed accordingly
    def test_POST_post_with_invalid_payload(self, app):
        response = app.post(
            f"/posts/", json={'content': '', 'user_email': POST_TO_BE_CREATED['user_email']})
        assert response.status == '400'
        raise NotImplementedError

    @pytest.mark.skip
    def test_POST_post_creates_posted_relation(self, app):
        raise NotImplementedError


@pytest.mark.DELETE_post
class TestDELETE:
    def test_DELETE_existing_post(self, app):
        raise NotImplementedError

    def test_DELETE_non_existing_post(self, app):
        raise NotImplementedError

    def test_DELETE_existing_post_deletes_posted_relation(self, app):
        raise NotImplementedError

    """def test_that_deleting_a_post_should_succeed(self, app):
        # TODO TEST THIS ENDPOINT TOO.
        posts_response = app.get(f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}")

        post_id = posts_response.get_json()[0]['id']

        response = app.delete(
            f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}", json={'post_id': post_id})  # TODO find a way to have it all set in POST_UPDATE_B and A
        assert response.status == '204 NO CONTENT'
        assert response.data == b''"""
