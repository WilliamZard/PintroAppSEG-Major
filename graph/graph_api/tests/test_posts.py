# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
from ast import literal_eval

import pytest
from flask.json import jsonify
from jsonmerge import merge

from graph_api import create_app
from graph_api.apis.users import UserSchema
from graph_api.apis.neo4j_ops import get_list_of_user_post_dates

from .generate_test_data import (USER_WITH_MULTIPLE_POSTS, USER_POST_C, USER_POST_B, USER_POST_A, 
                                POST_UPDATE_A, POST_UPDATE_B, populate_db, clear_db)


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
class TestGet:
    #TODO refactor the assertions.
    def test_get_all_posts_should_return_all_user_posts(self, app):
        response = app.get(f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}")
        assert response.status == '200 OK'
        assert len(response.get_json()) == 2
        for resp in response.get_json():
            if resp['content'] == USER_POST_B['content']:
                assert True
                continue
            if resp['content'] == USER_POST_A['content']:
                assert True
                continue
            assert False

@pytest.mark.get
class TestPut:
    def test_editing_an_existing_post_should_succeed(self, app):
        #First retrieve all the posts so that we can select extract the id of the user's second post and edit it.
        posts_response = app.get(f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}")# TODO TEST THIS ENDPOINT TOO. 
        post_id = posts_response.get_json()[1]['id']  

        response = app.put(
            f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}", json=merge({'post_id': post_id}, POST_UPDATE_B)) #TODO find a way to have it all set in POST_UPDATE_B and A
        assert response.status == '204 NO CONTENT'
        assert response.data == b''


@pytest.mark.get
class TestPost:
    def test_posting_a_post__should_post_given_content(self, app):
        response = app.post(f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}", json=USER_POST_C)
        assert response.status == '200 OK'
        assert response.get_json()['content'] == USER_POST_C['content']

    def test_posting_post_with_empty_content_should_not_work(self, app):
        response = app.post(f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}", json={'content': ''})
        assert response.status == '404 NOT FOUND'

class TestDelete:
    def test_that_deleting_a_post_should_succeed(self, app):
        posts_response = app.get(f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}")# TODO TEST THIS ENDPOINT TOO. 

        post_id = posts_response.get_json()[0]['id'] 

        response = app.delete(
            f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}", json={'post_id': post_id}) #TODO find a way to have it all set in POST_UPDATE_B and A
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

