import pytest
from flask import json Flask
from flask.json import jsonify

from .conftest import app, populate_db
from .generate_test_data import (Business, Space, Tag, User,
                                 basic_business_node, basic_space_node,
                                 basic_tag_node, basic_user_node)
from .helper_functions import *


@pytest.mark.POST_search
class TestPOST:
    def test_single_character_query_should_return_nothing(self, app: Flask, populate_db: None) -> None:
        ''' A query done with a string of length 1 shouldn't return any node because otherwise it would basically
            return all the nodes in the database
        '''
        # Generate Test data
        nodes = []
        space_data = []
        space_data.append(Space(email='space_a@test.com')._asdict())
        space_data.append(Space(email='space_b@test.com')._asdict())
        for space in space_data:
            nodes.append(basic_space_node(space))

        business_data = []
        business_data.append(Business(email='business_a@test.com')._asdict())
        business_data.append(Business(email='business_b@test.com')._asdict())
        for business in business_data:
            nodes.append(basic_business_node(business))

        user_data = []
        user_data.append(User(email='user_a@test.com')._asdict())
        user_data.append(User(email='user_b@test.com')._asdict())
        for user in user_data:
            user.pop('passions')
            user.pop('help_others')
            nodes.append(basic_user_node(user))
        populate_db(nodes_to_create=nodes)

        # Test
        string_query = 'a'
        response = app.post("/search/", json=dict({'query': string_query}))
        # Assertion
        assert response.status == '200 OK'
        assert response.get_json() == []

    def test_empty_query_should_return_nothing(self, app: Flask, populate_db: None) -> None:
        '''
        A query done with a string of length 0 shouldn't return any node because otherwise it would 
        return all the nodes in the database which doesn't make sense in any situation.
        '''
        # Generate Test data
        nodes = []
        space_data = []
        space_data.append(Space(email='space_a@test.com')._asdict())
        space_data.append(Space(email='space_b@test.com')._asdict())
        for space in space_data:
            nodes.append(basic_space_node(space))

        business_data = []
        business_data.append(Business(email='business_a@test.com')._asdict())
        business_data.append(Business(email='business_b@test.com')._asdict())
        for business in business_data:
            nodes.append(basic_business_node(business))

        user_data = []
        user_data.append(User(email='user_a@test.com')._asdict())
        user_data.append(User(email='user_b@test.com')._asdict())
        for user in user_data:
            user.pop('passions')
            user.pop('help_others')
            nodes.append(basic_user_node(user))
        populate_db(nodes_to_create=nodes)

        # Test
        string_query = ''
        response = app.post("/search/", json=dict({'query': string_query}))
        # Assertion
        assert response.status == '200 OK'
        assert response.get_json() == []

    def test_query_that_partially_matches_full_names_or_emails_should_return_correct_nodes(self, app: Flask, populate_db: None) -> None:
        ''' A query that partially matches some full names or emails should return all the appropriate accounts.'''
        # Generate Test data
        nodes = []
        space_data = []
        matching_space = Space(
            email='matching_space@test.com', full_name='Lello Pasqualino')._asdict()
        space_data.append(matching_space)
        space_data.append(Space(email='space_b@test.com')._asdict())
        space_data.append(Space(email='space_c@test.com')._asdict())
        for space in space_data:
            nodes.append(basic_space_node(space))

        business_data = []
        matching_business = Business(
            email='matching_business@test.com', full_name='Lello Di Caprio')._asdict()
        business_data.append(matching_business)
        business_data.append(Business(email='business_b@test.com')._asdict())
        business_data.append(Business(email='business_c@test.com')._asdict())
        for business in business_data:
            nodes.append(basic_business_node(business))

        user_data = []
        matching_user = User(email='Lello@test.com')._asdict()
        user_data.append(matching_user)
        user_data.append(User(email='user_b@test.com')._asdict())
        user_data.append(User(email='user_c@test.com')._asdict())
        for user in user_data:
            user.pop('passions')
            user.pop('help_others')
            nodes.append(basic_user_node(user))
        populate_db(nodes_to_create=nodes)

        # Test
        string_query = 'Lello'
        response = app.post("/search/", json=dict({'query': string_query}))
        json_response = prepere_search_responses_for_account_assertion(
            response)

        json_response = ordered(json_response)
        expected_accounts = ordered(
            [matching_space, matching_business, matching_user])
        # Assertion
        assert response.status == '200 OK'
        assert json_response == expected_accounts

    def test_query_that_partially_matches_stories_should_return_correct_nodes(self, app: Flask, populate_db: None) -> None:
        '''
        A query that partially matches some stories in any business account, normal user account, 
        or space should return all the appropriated accounts.
        '''
        # Generate Test data
        nodes = []

        business_data = []
        matching_business = Business(
            email='matching_business@test.com', story='It is a business sponsored by UCL.')._asdict()
        business_data.append(matching_business)
        business_data.append(Business(email='business_b@test.com')._asdict())
        business_data.append(Business(email='business_c@test.com')._asdict())
        for business in business_data:
            nodes.append(basic_business_node(business))

        user_data = []
        matching_user = User(email='ucl@test.com')._asdict()
        user_data.append(matching_user)
        user_data.append(User(email='user_b@test.com')._asdict())
        user_data.append(User(email='user_c@test.com')._asdict())
        for user in user_data:
            user.pop('passions')
            user.pop('help_others')
            nodes.append(basic_user_node(user))
        populate_db(nodes_to_create=nodes)

        # Test
        string_query = 'UCL'
        response = app.post("/search/", json=dict({'query': string_query}))
        json_response = prepere_search_responses_for_account_assertion(
            response)
        json_response = ordered(json_response)
        expected_accounts = ordered([matching_business, matching_user])
        # Assertion
        assert response.status == '200 OK'
        assert json_response == expected_accounts

    def test_query_that_partially_matches_short_bios_should_return_correct_nodes(self, app: Flask, populate_db: None) -> None:
        '''
        A query that partially matches some short bios in any business account, normal user account, 
        or space should return all the appropriated accounts.
        '''
        # Generate Test data
        nodes = []

        space_data = []
        matching_space = Space(email='matching_space@test.com',
                               short_bio='This team makes researches on COVID-19')._asdict()
        space_data.append(matching_space)
        space_data.append(Space(email='space_b@test.com')._asdict())
        space_data.append(Space(email='space_c@test.com')._asdict())
        for space in space_data:
            nodes.append(basic_space_node(space))

        business_data = []
        matching_business = Business(email='matching_business@test.com',
                                     short_bio='We are a company fighting against COVID-19')._asdict()
        business_data.append(matching_business)
        business_data.append(Business(email='business_b@test.com')._asdict())
        business_data.append(Business(email='business_c@test.com')._asdict())
        for business in business_data:
            nodes.append(basic_business_node(business))

        user_data = []
        matching_user = User(email='Lello@test.com',
                             short_bio='I got COVID-19 once.')._asdict()
        user_data.append(matching_user)
        user_data.append(User(email='user_b@test.com')._asdict())
        user_data.append(User(email='user_c@test.com')._asdict())
        for user in user_data:
            user.pop('passions')
            user.pop('help_others')
            nodes.append(basic_user_node(user))
        populate_db(nodes_to_create=nodes)

        # Test
        string_query = 'COVID'
        response = app.post("/search/", json=dict({'query': string_query}))

        json_response = prepere_search_responses_for_account_assertion(
            response)
        json_response = ordered(json_response)
        expected_accounts = ordered(
            [matching_space, matching_business, matching_user])
        # Assertion
        assert response.status == '200 OK'
        assert json_response == expected_accounts

    def test_query_that_partially_matches_tag_returns_correct_user(self, app: Flask, populate_db: None) -> None:
        '''
        A query that partially matches a tag used in any business account, normal user account, 
        or space should return all the appropriated accounts.
        '''
        # Generate Test data
        nodes = []
        tag_data = []
        matching_tag = Tag(name='Civil Engineering')._asdict()
        tag_data.append(matching_tag)
        tag_data.append(Tag(name='KCL')._asdict())
        tag_data.append(Tag(name='Research')._asdict())
        for tag in tag_data:
            nodes.append(basic_tag_node(tag))

        business_data = []
        matching_business_a = Business(
            email='matching_business_a@test.com')._asdict()
        matching_business_b = Business(
            email='matching_business_b@test.com')._asdict()
        business_data.append(matching_business_a)
        business_data.append(matching_business_b)
        business_data.append(Business(email='business_b@test.com')._asdict())
        business_data.append(Business(email='business_c@test.com')._asdict())
        for business in business_data:
            nodes.append(basic_business_node(business))

        space_data = []
        space_data.append(Space(email='space_b@test.com')._asdict())
        space_data.append(Space(email='space_c@test.com')._asdict())
        for space in space_data:
            nodes.append(basic_space_node(space))

        user_data = []
        matching_user_a = User(
            email='matching_user_a@test.com')._asdict()
        user_data.append(matching_user_a)
        user_data.append(User(email='user_b@test.com')._asdict())
        user_data.append(User(email='user_c@test.com')._asdict())
        for user in user_data:
            user.pop('passions')
            user.pop('help_others')
            nodes.append(basic_user_node(user))

        # Define tag relationships
        tag_a = {
            's_node_properties': {'email': matching_business_a['email']}, 's_node_labels': 'Business',
            'e_node_properties': {'name': matching_tag['name']}, 'e_node_labels': 'Tag',
            'relationship_type': 'TAGGED'}
        tag_b = {
            's_node_properties': {'email': matching_business_b['email']}, 's_node_labels': 'Business',
            'e_node_properties': {'name': matching_tag['name']}, 'e_node_labels': 'Tag',
            'relationship_type': 'TAGGED'}

        tag_c = {
            's_node_properties': {'email': matching_user_a['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'name': matching_tag['name']}, 'e_node_labels': 'Tag',
            'relationship_type': 'TAGGED'}

        populate_db(nodes_to_create=nodes,
                    relationships_to_create=[tag_a, tag_b, tag_c])

        # Test
        string_query = 'Civil'
        response = app.post("/search/", json=dict({'query': string_query}))

        json_response = prepere_search_responses_for_account_assertion(
            response)
        json_response = ordered(json_response)
        expected_accounts = ordered([matching_business_a, matching_business_b, matching_user_a])
        # Assertion
        assert response.status == '200 OK'
        assert json_response == expected_accounts
