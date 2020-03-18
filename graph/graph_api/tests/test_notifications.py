import pytest

from .generate_test_data import USER_WITH_NOTIFICATIONS, NOTIFICATION_A, NOTIFICATION_B


@pytest.mark.GET_notifications
class TestGET:
    def test_GET_notifications_for_existing_user(self, app):
        response = app.get(
            f"/notifications/{USER_WITH_NOTIFICATIONS['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 2
        assert NOTIFICATION_A in json
        assert NOTIFICATION_B in json
        # TODO: create user, create inbound request relationships, create requesting users
