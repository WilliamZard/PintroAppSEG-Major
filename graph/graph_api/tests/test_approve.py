import pytest

from .conftest import app, populate_db
from .generate_test_data import (Business, User, basic_business_node,
                                 basic_user_node)


@pytest.mark.POST_approve
class TestPOST:
    # TODO: add tests for entering a valid email
    def test_POST_approve_relation_request_with_invalid_requester_email(self, app, populate_db):
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

    def test_POST_approve_relation_request_with_invalid_receiver_email(self, app, populate_db):
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
            f"/approve/affiliation/{business_requesting_affiliation['email']}/{invalid_email}")
        assert response.status == '400 BAD REQUEST'
        assert response.data == b'Request recipient email invalid format'

        
    def test_POST_approve_relation_request_with_non_existing_user(self, app, populate_db):
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

        non_existing_user_email ='non-existing_user@gmail.com'

        response = app.post(
            f"/approve/follow/{user_requesting_follow['email']}/{non_existing_user_email}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b'USER NOT FOUND'


    def test_POST_approve_affiliation_user_to_business_should_fail(self, app, populate_db):
        # Define users
        user_requesting_affiliation = User(
            email='receiving_affiliation_request@rona.com')._asdict()
        user_requesting_affiliation_node = basic_user_node(user_requesting_affiliation)
        business_receiving_request = Business(
            email='receiving_request@rona.com')._asdict()
        business_receiving_request_node = basic_business_node(
            business_receiving_request)

        # Define relationship
        requested_affiliation = {
            's_node_properties': {'email': user_requesting_affiliation['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email':business_receiving_request['email']}, 'e_node_labels': 'Business',
            'relationship_type': 'REQUESTED_AFFILIATION'}

        populate_db(nodes_to_create=[business_receiving_request_node,
                                     user_requesting_affiliation_node],
                    relationships_to_create=[requested_affiliation])

        response = app.post(
            f"/approve/affiliation/{user_requesting_affiliation['email']}/{business_receiving_request['email']}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b'USER NOT FOUND'

    def test_POST_approve_follow_request_with_valid_users(self, app, populate_db):
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


    def test_POST_approve_affiliation_request_with_valid_users(self, app, populate_db):
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

