# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
# TODO: add logic for wether or not to populate db
from ast import literal_eval

import pytest
from flask.json import jsonify
from jsonmerge import merge

from .generate_test_data import USER_ABOUT_TO_BE_FOLLOWED, USER_ABOUT_TO_FOLLOW, NONEXISTANT_USER_EMAIL, USER_BEING_FOLLOWED, USER_FOLLOWING


@pytest.mark.POST_following
class TestPOSTFollowing:
    def test_POST_following_on_existing_users(self, app):
        response = app.post(
            f"/following/{USER_ABOUT_TO_FOLLOW['email']}/{USER_ABOUT_TO_BE_FOLLOWED['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

        # TODO: get request to assert follow relationship was created.
        # use endpoint to get all followings of user_following and check exists a follow to user being followed

    @pytest.mark.xfail
    # TODO: finish this test. Put on hold for now as niche usecase
    def test_POST_following_on_non_existing_users(self, app):
        response = app.post(
            f"/following/{NONEXISTANT_USER_EMAIL}/{USER_ABOUT_TO_BE_FOLLOWED['email']}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_POST_following_where_following_already_exists(self, app):
        raise NotImplementedError

    @pytest.mark.xfail
    def test_POST_followinig_self(self, app):
        raise NotImplementedError


@pytest.mark.DELETE_following
class TestDELETEFollowing:
    def test_DELETE_existing_following(self, app):
        response = app.delete(
            f"/following/{USER_FOLLOWING['email']}/{USER_BEING_FOLLOWED['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
        # TODO: get request to assert follow relationship was deleted.
        # use endpoint to get all followings of user_following and check does not exist a follow to user being followed

    @pytest.mark.xfail
    def test_DELETE_non_existing_following(self, app):
        raise NotImplementedError


"""
@pytest.mark.get_followings
class TestGetUserFollowersPosts:
    # TODO: delete ordering in query
    def test_get_posts_of_followers_of_valid_user(self, app):
        response = app.get(
            f"/users/{USER_FOLLOWING['email']}/followings/posts")
        assert response.status == '200 OK'
        assert response.get_json() == [USER_BEING_FOLLOWED_POST_A, USER_BEING_FOLLOWED_POST_B,
                                       USER_BEING_FOLLOWED_POST_C, USER_WITH_ONE_FOLLOWING_POST_A,
                                       USER_WITH_NO_FOLLOWINGS_POST_A, USER_WITH_NO_FOLLOWINGS_POST_B]

    # TODO: test for non existent user <must_have>
    # TODO: test for user with no followers <edge_case>
    # TODO: test for user with followers with no posts <edge_case>
"""
