import pytest
from graph_api import create_app
from .generate_test_data import populate_db, VALID_USER
# TODO: note need for local neo4j db setup
# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
# TODO: have a folder for database stuff? That could make it easier to separate
from ast import literal_eval


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
    print(VALID_USER['email'])
    response = app.get(f"/users/{VALID_USER['email']}")
    print(response.data)
    # TODO: you should use marshmallow deserialisation here. Not all this encoding.
    assert literal_eval(response.data.decode('ASCII')) == VALID_USER
