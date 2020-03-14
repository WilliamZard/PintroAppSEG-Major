import pytest

from graph_api import create_app

from .generate_test_data import clear_db, populate_db


@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.testing = True

    #clear_db()
    # TODO: right now this populates and clears the database for all tests, as opposed to every test
    # Not sure which if this should happen per test or per module.
    # Figure this out.
    with app.test_client() as client:
        # NOTE commented out populate db
        populate_db(rewrite_test_data=True)
        yield client
    clear_db()
