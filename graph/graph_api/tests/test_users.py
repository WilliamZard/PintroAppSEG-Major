import pytest
from graph_api import create_app
from graph_api.apis.users import UserSchema
from .generate_test_data import populate_db, VALID_USER
# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
# TODO: add logic for wether or not to populate db
from ast import literal_eval
from flask.json import jsonify


@pytest.fixture
def app():
    app = create_app()
    app.testing = True

    # TODO: populate database when testing.
    print("ey!")
    with app.test_client() as client:
        populate_db(rewrite_test_data=True)
        yield client


def test_get_user_with_valid_email(app):
    response = app.get(f"/users/{VALID_USER['email']}")
    assert response.status == '200 OK'
    assert response.data == jsonify(VALID_USER).data
