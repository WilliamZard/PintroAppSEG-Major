import pytest
from flask import Flask

from .conftest import app, populate_db
from .generate_test_data import User, basic_user_node, Business, basic_business_node


@pytest.mark.POST_request
class TestPOST:
    # TODO: add tests for entering a valid email
    # TODO: add tests for if given users exist or not
    # TODO: add tests for if given user type can make given request.
    #       e.g. users cannot make affiliation requests to businesses.
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

        # TODO: add get request for checking if FOLLOW_REQUEST relationship was actually created

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

        # TODO: add get request for checking if FOLLOW_REQUEST relationship was actually created


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

        # TODO: add get request for checking if FOLLOW_REQUEST relationship was actually created

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
        # TODO: fix test not passing when all tests are run
        response = app.delete(
            f"/request/affiliation/{business_requesting_affiliation['email']}/{user_receiving_request['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''
