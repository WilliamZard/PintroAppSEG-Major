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
class TestPUT:
    # TODO: assert modified was changed properly for all put tests
    # TODO: assert created was not changed for all put tests
    # TODO: get request and assertion to check correct update
    def test_PUT_existing_post(self, app):
        response = app.put(
            f"/posts/{POST_TO_BE_UPDATED_THAT_EXISTS['uuid']}", json=POST_TO_BE_UPDATED_THAT_EXISTS['content'])
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

    def test_PUT_non_existent_post(self, app):
        response = app.put(
            f"/posts/{NON_EXISTING_POST_UUID}", json=POST_TO_BE_UPDATED_THAT_EXISTS['content'])
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_PUT_existing_post_invalid_changes(self, app):
        pass


@pytest.mark.POST_post
class TestPOST:
    # TODO: assert modified was changed properly for all put tests
    # TODO: assert created was not changed for all put tests
    # TODO: get request and assertion to check correct update
    def test_POST_post_with_valid_payload(self, app):
        response = app.post(
            f"/posts/", json=POST_TO_BE_CREATED)
        assert response.status == '201 CREATED'
        assert response.data == b''

    @pytest.mark.xfail
    def test_POST_post_with_invalid_payload(self, app):
        response = app.post(
            f"/posts/", json={'content': '', 'user_email': POST_TO_BE_CREATED['user_email']})
        assert response.status == '400'

    @pytest.mark.xfail
    def test_POST_post_creates_posted_relation(self, app):
        pass


@pytest.mark.DELETE_post
class TestDELETE:
    def test_DELETE_existing_post(self, app):
        raise NotImplementedError

    def test_DELETE_non_existing_post(self, app):
        raise NotImplementedError

    @pytest.mark.xfail
    def test_DELETE_existing_post_deletes_posted_relation(self, app):
        pass
