# TODO: note need for local neo4j db setup
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
@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.testing = True

    with app.test_client() as client:
        populate_db(rewrite_test_data=True)
        yield client
    clear_db()

@pytest.mark.get
class TestGetPosts:
    def test_order_of_posts_from_user_followings_is_chronological(self, app):
        response = app.get(f"/followings/posts/{USER_WITH_THREE_FOLLOWINGS['email']}")
        assert response.status == '200 OK'
        assert response.get_json() == [USER_WITH_TWO_FOLLOWINGS_POST_A, USER_WITH_TWO_FOLLOWINGS_POST_B,
                                       USER_WITH_TWO_FOLLOWINGS_POST_C, USER_WITH_ONE_FOLLOWING_POST_A,
                                       USER_WITH_NO_FOLLOWINGS_POST_A, USER_WITH_NO_FOLLOWINGS_POST_B]
    
    def test_number_of_posts_returned_for_user_following_posts_is_correct(self, app):
        response = app.get(f"/followings/posts/{USER_WITH_TWO_FOLLOWINGS['email']}")
        assert response.status == '200 OK'
        assert len(response.get_json()) == 3