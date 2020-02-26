# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
# TODO: add logic for wether or not to populate db
from ast import literal_eval

import pytest
from flask.json import jsonify

from graph_api import create_app
from graph_api.apis.users import UserSchema

from .generate_test_data import USER_WITH_MULTIPLE_POSTS, USER_POSTS, populate_db, clear_db


# TODO: consider changing scope of fixture so client object does not creating every time.
@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.testing = True

    # TODO: right now this populates and clears the database for all tests, as opposed to every test
    # Not sure which if this should happen per test or per module.
    # Figure this out.
    with app.test_client() as client:
        # NOTE commented out populate db
        populate_db(rewrite_test_data=True)
        yield client
    clear_db()



@pytest.mark.get
class TestGet:
    def test_get_all_posts_of_person_with_at_least_one_post(self, app):
        response = app.get(f"/posts/{USER_WITH_MULTIPLE_POSTS['email']}")
        assert response.status == '200 OK'
        print(response.get_json())
        assert response.get_json() == USER_POSTS