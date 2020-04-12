import pytest

from .conftest import app, populate_db
from .generate_test_data import (Business, User, basic_business_node,
                                 basic_user_node)
from flask import Flask


@pytest.mark.POST_approve
class TestPOST:
    # TODO: add tests for entering a valid email
    def test_POST_approve_relation_request_with_invalid_requester_email(self, app: Flask, populate_db: None) -> None:
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
        
        invalid_email = 'requestingaffiliationronacom'

        
        response = app.post(
            f"/approve/affiliation/{invalid_email}/{user_receiving_request['email']}")
        assert response.status == '400 BAD REQUEST'
        assert response.data == b'Requester email invalid format'

    def test_POST_approve_follow_request_with_valid_users(self, app: Flask, populate_db: None) -> None:
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
        response = app.post(
            f"/approve/follow/{user_requesting_follow['email']}/{user_receiving_request['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

    def test_POST_approve_follow_request_with_non_existing_user(self, app: Flask, populate_db: None) -> None:
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
        response = app.post(
            f"/approve/follow/{'wrong_email@email.com'}/{user_receiving_request['email']}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b'USER NOT FOUND'

        response = app.post(
            f"/approve/follow/{user_requesting_follow['email']}/{'wrong_email@email.com'}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b'USER NOT FOUND'

    def test_POST_approve_follow_request_with_invalid_emails(self, app: Flask) -> None:

        response = app.post(
            f"/approve/follow/{'invalid_email'}/{'valid_email@email.com'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

        response = app.post(
            f"/approve/follow/{'valid_email@email.com'}/{'invalid_email'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    def test_POST_approve_affiliation_request_with_valid_users(self, app: Flask, populate_db: None) -> None:
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

        response = app.post(
            f"/approve/affiliation/{business_requesting_affiliation['email']}/{user_receiving_request['email']}")
        assert response.status == '201 CREATED'
        assert response.data == b''

    def test_POST_approve_affiliation_request_with_non_existing_user(self, app: Flask, populate_db: None) -> None:
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

        response = app.post(
            f"/approve/affiliation/{'wrong_email@email.com'}/{user_receiving_request['email']}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b'USER NOT FOUND'

        response = app.post(
            f"/approve/affiliation/{business_requesting_affiliation['email']}/{'wrong_email@email.com'}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b'USER NOT FOUND'

    def test_POST_approve_affiliation_request_with_invalid_emails(self, app: Flask) -> None:

        response = app.post(
            f"/approve/affiliation/{'invalid_email'}/{'valid_email@email.com'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

        response = app.post(
            f"/approve/affiliation/{'valid_email@email.com'}/{'invalid_email'}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''
