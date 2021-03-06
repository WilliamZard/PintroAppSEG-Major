"""Useful functions used by our API endpoints."""
from .neo4j_ops.search import get_accounts_with_tag
from neo4j import Record, Session
from typing import List, Dict
import re
from re import Match


def valid_email(email: str) -> Match:
    '''
        Function that checks whether a string matches a standard email format. If 
        it does it returns a match object for that string, otherwise it returns None.
    '''
    '''Args: 
        -email = The email that needs to be checked.
    '''
    return re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)


def get_accouts_with_tags(tag_records: List[Record], session: Session) -> List[Dict[str, str]]:
    '''
        Function that returns at most 10 accounts for each type of account (space, user, or business) 
        existing in the db that use some given tags.
    '''
    '''Args:
        -tag_records = a list of records (or so called Generator). These will be used to match all the accounts 
        that use at least one of them.
        -session = the session where to run all the needed queried on the db.
    '''
    profiles_with_tags = []
    # For every tag, look for normal users, business accounts, or spaces that used that tag, and append them to profile_with_tags.
    for tag_record in tag_records:
        tag = dict(tag_record.data().get('node').items())
        # #Check for normal users with such tag.
        tag_user_records = session.write_transaction(
            get_accounts_with_tag, tag['name'], 'Person').records()
        for tag_user_record in tag_user_records:
            if tag_user_record.data().get('node') is not None:
                extracted_user = dict(
                    tag_user_record.data().get('node').items())
                extracted_user['score'] = tag_record.data()['score']
                extracted_user['profile_type'] = "person"
                profiles_with_tags.append(extracted_user)
        # #Check for business accounts with such tag.
        tag_business_records = session.write_transaction(
            get_accounts_with_tag, tag['name'], 'Business').records()
        for tag_business_record in tag_business_records:
            if tag_business_record.data().get('node') is not None:
                extracted_business = dict(
                    tag_business_record.data().get('node').items())
                extracted_business['score'] = tag_record.data()['score']
                extracted_business['profile_type'] = "business"
                profiles_with_tags.append(extracted_business)
        # #Check for coworking spaces with such tag.
        tag_space_records = session.write_transaction(
            get_accounts_with_tag, tag['name'], 'Space').records()
        for tag_space_record in tag_space_records:
            if tag_space_record.data().get('node') is not None:
                extracted_space = dict(
                    tag_space_record.data().get('node').items())
                extracted_space['score'] = tag_record.data()['score']
                extracted_space['profile_type'] = "space"
                profiles_with_tags.append(extracted_space)

    return profiles_with_tags


def remove_duplicates(array: List[Dict[str, str]]) -> List[Dict[str, str]]:
    '''
        Function that removes all the duplicates dictionaries in a list of dictionaries.
    '''
    '''Args:
        -array = list of dictionaries where to remove potential duplicates.
    '''
    new_list = []
    for i in range(0, len(array)):
        if array[i] not in array[i+1:]:
            new_list.append(array[i])
    return new_list
