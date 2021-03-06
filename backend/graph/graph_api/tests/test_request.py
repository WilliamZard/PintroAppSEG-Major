import pytest
from flask import Flask

from .conftest import app, populate_db
from .generate_test_data import User, basic_user_node, Business, basic_business_node


@pytest.mark.POST_request
class TestPOST:
    def test_POST_follow_request_with_valid_users(self, app: Flask, populate_db: None) -> None:
        # Define users
        user_requesting_follow = User(
            email='requesting_follow@rona.com')._asdict()
        user_requesting_follow_node = basic_user_node(user_requesting_follow)
        user_receiving_request = User(
            email='receiving_follow_request@rona.com')._asdict()
        user_receiving_request_node = basic_user_node(user_receiving_request)

        populate_db(nodes_to_create=[user_requesting_follow_node,
                                     user_receiving_request_node])
        response = app.post(
            f"/request/follow/{user_requesting_follow['email']}/{user_receiving_request['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

    def test_POST_follow_request_with_invalid_email(self, app: Flask) -> None:
        response = app.post(
            f"/request/follow/{'invalid_email'}/{'valid_email@email.com'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

        response = app.post(
            f"/request/follow/{'valid_email@email.com'}/{'invalid_email'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    def test_POST_affiliation_request_with_valid_users(self, app: Flask, populate_db: None) -> None:
        # Define users
        business_requesting_affiliation = Business(
            email='requesting_affiliation@rona.com')._asdict()
        business_requesting_affiliation_node = basic_business_node(
            business_requesting_affiliation)
        user_receiving_request = User(
            email='receiving_affiliation_request@rona.com')._asdict()
        user_receiving_request_node = basic_user_node(user_receiving_request)

        populate_db(nodes_to_create=[business_requesting_affiliation_node,
                                     user_receiving_request_node])
        response = app.post(
            f"/request/affiliation/{business_requesting_affiliation['email']}/{user_receiving_request['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

    def test_POST_affiliation_request_with_invalid_email(self, app: Flask) -> None:
        response = app.post(
            f"/request/affiliation/{'invalid_email'}/{'valid_email@email.com'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

        response = app.post(
            f"/request/affiliation/{'valid_email@email.com'}/{'invalid_email'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.DELETE_request
class TestDELETE:
    def test_DELETE_follow_request_with_valid_users(self, app: Flask, populate_db: None) -> None:
        # Define users
        user_requesting_follow = User(
            email='requesting_follow@rona.com')._asdict()
        user_requesting_follow_node = basic_user_node(user_requesting_follow)
        user_receiving_request = User(
            email='receiving_follow_request@rona.com')._asdict()
        user_receiving_request_node = basic_user_node(user_receiving_request)

        # Define relationship
        requested_follow = {
            's_node_properties': {'email': user_requesting_follow['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': user_receiving_request['email']}, 'e_node_labels': 'Person',
            'relationship_type': 'REQUESTED_FOLLOW'}

        populate_db(nodes_to_create=[user_requesting_follow_node,
                                     user_receiving_request_node],
                    relationships_to_create=[requested_follow])
        response = app.delete(
            f"/request/follow/{user_requesting_follow['email']}/{user_receiving_request['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

    def test_DELETE_affiliation_request_with_valid_users(self, app: Flask, populate_db: None) -> None:
        # Define users
        business_requesting_affiliation = Business(
            email='requesting_affiliation@rona.com')._asdict()
        business_requesting_affiliation_node = basic_business_node(
            business_requesting_affiliation)
        user_receiving_request = User(
            email='receiving_affiliation_request@rona.com')._asdict()
        user_receiving_request_node = basic_user_node(user_receiving_request)

        # Define relationship
        requested_affiliation = {
            's_node_properties': {'email': business_requesting_affiliation['email']}, 's_node_labels': 'Business',
            'e_node_properties': {'email': user_receiving_request['email']}, 'e_node_labels': 'Person',
            'relationship_type': 'REQUESTED_AFFILIATION'}

        populate_db(nodes_to_create=[business_requesting_affiliation_node,
                                     user_receiving_request_node],
                    relationships_to_create=[requested_affiliation])
        response = app.delete(
            f"/request/affiliation/{business_requesting_affiliation['email']}/{user_receiving_request['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
