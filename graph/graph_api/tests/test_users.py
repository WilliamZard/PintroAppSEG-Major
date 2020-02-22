import pytest
from graph_api import create_app
# TODO: note need for local neo4j db setup


@pytest.fixture
def app():
    app = create_app()
    app.testing = True

    print("ey!")
    with app.test_client() as client:
        yield client


def test_get_user(app):
    response = app.get('test_email@test.now')
