import pytest
from graph_api import create_app


@pytest.fixture
def app():
    app = create_app()

    yield app


def test_get_user(app):
    app.get('test_email@test.now')
