import pytest
from flask import json
from flask.json import jsonify

from .conftest import app
from .test_data.search import *
from .helper_functions import *


@pytest.mark.POST_search
class TestPOST:
    def test_single_character_query_should_return_nothing(self, app):
        ''' A query done with a string of length 1 shouldn't return any node because otherwise it would basically
            return all the nodes in the database
        '''
        response = app.post("/search/", json=SINGLE_CHAR_SEARCH['request'])

        assert response.status == '200 OK'
        assert response.get_json() == SINGLE_CHAR_SEARCH['result']

    def test_empty_query_should_return_nothing(self, app):
        ''' A query done with a string of length 0 shouldn't return any node because otherwise it would 
            return all the nodes in the database which doesn't make sense in any situation
        '''
        response = app.post("/search/", json=EMPTY_STRING_SEARCH['request'])
        
        assert response.status == '200 OK'
        assert response.get_json() == EMPTY_STRING_SEARCH['result']

    def test_query_that_partially_matches_full_names_or_emails_should_return_correct_nodes(self,app):
        ''' A query that partially matches some full names or emails should return all the appropriate accounts.
        '''

        response = app.post("/search/", json=VALID_MATCHING_NAME_OR_EMAIL_SEARCH['request'])
        json_response = prepere_search_responses_for_account_assertion(response, VALID_MATCHING_NAME_OR_EMAIL_SEARCH)
        
        assert response.status == '200 OK'
        assert ordered(json_response) == ordered(VALID_MATCHING_NAME_OR_EMAIL_SEARCH['result'])

    def test_query_that_partially_matches_stories_should_return_correct_nodes(self,app):
        ''' A query that partially matches some stories in any business account, normal user account, 
            or space should return all the appropriated accounts.
        '''
        response = app.post("/search/", json=MATCHING_STORY_OR_EVENTS_SEARCH['request'])
        json_response = prepere_search_responses_for_account_assertion(response, MATCHING_STORY_OR_EVENTS_SEARCH)

        assert response.status == '200 OK'
        assert ordered(json_response) == ordered(MATCHING_STORY_OR_EVENTS_SEARCH['result'])
    
    def test_query_that_partially_matches_short_bios_should_return_correct_nodes(self,app):
        ''' A query that partially matches some short bios in any business account, normal user account, 
            or space should return all the appropriated accounts.
        '''
        response = app.post("/search/", json=MATCHING_SHORT_BIO_SEARCH['request'])
        json_response = prepere_search_responses_for_account_assertion(response, MATCHING_SHORT_BIO_SEARCH)
        
        assert response.status == '200 OK'
        assert ordered(json_response) == ordered(MATCHING_SHORT_BIO_SEARCH['result'])

    def test_query_that_partially_matches_tag_returns_correct_user(self, app):
        ''' A query that partially matches a tag used in any business account, normal user account, 
            or space should return all the appropriated accounts.
        '''
        response = app.post("/search/", json=MATCHING_TAG_SEARCH['request'])
        json_response = prepere_search_responses_for_account_assertion(response, MATCHING_TAG_SEARCH)

        assert response.status == '200 OK'
        assert ordered(json_response) == ordered(MATCHING_TAG_SEARCH['result'])

        




