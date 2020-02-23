import pytest
from graph_api import create_app
from graph_api.apis.users import UserSchema
from .generate_test_data import populate_db, VALID_USER, INVALID_EMAIL_USER
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
        # NOTE commented out populate db
       # populate_db(rewrite_test_data=True)
        yield client


def test_get_user_with_valid_email_that_exists(app):
    response = app.get(f"/users/{VALID_USER['email']}")
    assert response.status == '200 OK'
    # TODO: consider using standard json.dumps instead of jsonify
    assert response.data == jsonify(VALID_USER).data


def test_get_user_with_valid_email_that_does_not_exist(app):
    NONEXISTANT_USER_EMAIL = 'I@donut.exist'
    response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}")
    assert response.status == '404 NOT FOUND'
    assert response.data == jsonify({}).data


def test_get_user_with_invalid_email(app):
    response = app.get(f"/users/{INVALID_EMAIL_USER['email']}")
    print(response)
    print(response.status)
    assert response.status == '422 Invalid Email'
    assert response.data == jsonify({}).data
