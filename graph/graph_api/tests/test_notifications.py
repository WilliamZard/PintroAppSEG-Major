import pytest

from .generate_test_data import USER_WITH_NOTIFICATIONS, NOTIFICATION_A, NOTIFICATION_B, USER_WITH_NO_NOTIFICATIONS


@pytest.mark.GET_notifications
class TestGET:
    # TODO: test email validity
    # TODO: test only users can make this request
    def test_GET_notifications_for_existing_user(self, app):
        response = app.get(
            f"/notifications/{USER_WITH_NOTIFICATIONS['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert json == [NOTIFICATION_A, NOTIFICATION_B]
        # TODO: create user, create inbound request relationships, create requesting users

    def test_GET_notifications_for_existing_user_with_no_notifications(self, app):
        response = app.get(
            f"/notifications/{USER_WITH_NO_NOTIFICATIONS['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0
