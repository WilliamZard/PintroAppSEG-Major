"""# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
# TODO: add logic for wether or not to populate db
from ast import literal_eval

import pytest
from flask.json import jsonify
from jsonmerge import merge

from graph_api import create_app
from graph_api.apis.users import UserSchema

from .generate_test_data import (USER_WITH_THREE_FOLLOWINGS, USER_WITH_TWO_FOLLOWINGS,  USER_WITH_TWO_FOLLOWINGS_POST_A,
                                 USER_WITH_TWO_FOLLOWINGS_POST_B, USER_WITH_TWO_FOLLOWINGS_POST_C, USER_WITH_ONE_FOLLOWING_POST_A,
                                 USER_WITH_NO_FOLLOWINGS_POST_A, USER_WITH_NO_FOLLOWINGS_POST_B, populate_db, clear_db)


# TODO: consider changing scope of fixture so client object does not creating every time.
# TODO: app() fixture is used everywhere, move it somewhere else
@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.testing = True

    with app.test_client() as client:
        populate_db(rewrite_test_data=True)
        yield client
    clear_db()

# TODO: parameterising of pytests needs to become per endpoint, instead of per HTTP method
@pytest.mark.get_followings
class TestGetUserFollowersPosts:
    # TODO: delete ordering in query
    def test_get_posts_of_followers_of_valid_user(self, app):
        response = app.get(
            f"/users/{USER_WITH_THREE_FOLLOWINGS['email']}/followings/posts")
        assert response.status == '200 OK'
        assert response.get_json() == [USER_WITH_TWO_FOLLOWINGS_POST_A, USER_WITH_TWO_FOLLOWINGS_POST_B,
                                       USER_WITH_TWO_FOLLOWINGS_POST_C, USER_WITH_ONE_FOLLOWING_POST_A,
                                       USER_WITH_NO_FOLLOWINGS_POST_A, USER_WITH_NO_FOLLOWINGS_POST_B]

    # TODO: test for non existent user <must_have>
    # TODO: test for user with no followers <edge_case>
    # TODO: test for user with followers with no posts <edge_case>
"""
