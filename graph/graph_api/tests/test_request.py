import pytest
from .conftest import app


@pytest.mark.POST_request
class TestPOST:
    def test_POST_follow_request_with_valid_users(self, app):
        pass

    def test_POST_affiliation_request_with_valid_users(self, app):
        pass


@pytest.mark.DELETE_request
class testDELETE:
    def test_DELETE_follow_request_with_valid_users(self, app):
        pass

    def test_DELETE_affiliation_request_with_valid_users(self, app):
        pass
