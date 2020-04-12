import pytest
import time
from flask import Flask

from .conftest import app, populate_db
from .generate_test_data import (Business, Notification, User,
                                 basic_business_node, basic_user_node)


@pytest.mark.GET_notifications
class TestGET:
    # TODO: test email validity
    def test_GET_notifications_for_existing_user(self, app: Flask, populate_db: None) -> None:
        # Generate Data
        # Define users
        user_with_notifications = User(
            email='hasnotificatiosn@test.com')._asdict()
        user_with_notifications_node = basic_user_node(user_with_notifications)

        user_requesting_follow = User(
            email='requesting_follow@rona.com')._asdict()
        user_requesting_follow_node = basic_user_node(user_requesting_follow)

        business_requesting_affiliation = Business(
            email='request_affiliation@rona.com')._asdict()
        business_requesting_affiliation_node = basic_business_node(
            business_requesting_affiliation)

        follow_time = time.time()

        notification_a = Notification(requester_email=user_requesting_follow['email'],
                                      recipient_email=user_with_notifications['email'],
                                      relationship_type='follow',
                                      created_at=follow_time)._asdict()

        notification_b = Notification(requester_email=business_requesting_affiliation['email'],
                                      recipient_email=user_with_notifications['email'],
                                      relationship_type='affiliation',
                                      created_at=follow_time+10)._asdict()

        # Define relationships
        requested_follow = {
            's_node_properties': {'email': user_requesting_follow['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': user_with_notifications['email']}, 'e_node_labels': 'Person',
            'relationship_properties': {'created_at': follow_time}, 'relationship_type': 'REQUESTED_FOLLOW'}
        requested_affiliation = {
            's_node_properties': {'email': business_requesting_affiliation['email']}, 's_node_labels': 'Business',
            'e_node_properties': {'email': user_with_notifications['email']}, 'e_node_labels': 'Person',
            'relationship_properties': {'created_at': follow_time+10}, 'relationship_type': 'REQUESTED_AFFILIATION'}

        populate_db(nodes_to_create=[
                    user_with_notifications_node, user_requesting_follow_node, business_requesting_affiliation_node],
                    relationships_to_create=[requested_follow, requested_affiliation])

        # Test
        response = app.get(
            f"/notifications/{user_with_notifications['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 2
        assert dict(notification_a) in json
        assert dict(notification_b) in json

    def test_GET_notifications_for_existing_user_with_no_notifications(self, app: Flask, populate_db: None) -> None:
        # Generate test data
        valid_user = User(full_name='Duke Wellington',
                          email='duke@wellington.com')._asdict()
        # TODO: review how to handle tags at some point.
        valid_user_node = {'properties': dict(valid_user), 'labels': 'Person'}
        populate_db(nodes_to_create=[valid_user_node])

        # Test
        response = app.get(
            f"/notifications/{valid_user['email']}")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_GET_notifications_for_invalid_email(self, app: Flask) -> None:

        # Test
        response = app.get(
            f"/notifications/{'invalid_emailemail.com'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''
