from flask import make_response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

from .neo4j_ops import (create_session, get_nodes_for_user_search, get_nodes_for_business_search, get_nodes_for_space_search, 
                        get_users_with_tag, get_businesses_with_tag, get_spaces_with_tag, get_nodes_for_tag_search)
from .helper_functions import *


api = Namespace('search', title='Operations for full text search')

### Schemas used for serializations TODO once you ll have the business, and spaces API and their schemas instance you might just 
### want to import them from there and not creating them here, or event better create a schemas.py file and have em all in there.

class UserResultSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String()
    full_name = fields.Str(required=True)
    preferred_name = fields.String()
    profile_image = fields.String()
    phone = fields.String()
    gender = fields.String()
    job_title = fields.String()
    location = fields.String()
    short_bio = fields.String()
    story = fields.String()
    education = fields.String()
    profile_type = fields.String()
    active = fields.String()
    score = fields.String()

    
class SpaceResultSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String()
    full_name = fields.Str(required=True)
    profile_image = fields.String()
    phone = fields.String()
    location = fields.String()
    events = fields.String()
    short_bio = fields.String()
    profile_type = fields.String()
    score = fields.String()
    

class BusinessResultSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String()
    full_name = fields.Str(required=True)
    profile_image = fields.String()
    phone = fields.String()
    location = fields.String()
    short_bio = fields.String()
    story = fields.String()
    profile_type = fields.String()
    score = fields.String()

###  Models needed as payload in request for searching call

query = api.model('Query', {'query': restx_fields.String(required=True, title='String to look for relevant search.')})

user_result_schema = UserResultSchema()
space_result_schema = SpaceResultSchema()
business_result_schema = BusinessResultSchema()

@api.route('/')
@api.produces('application/json')
@api.expect(query)
class SearchPost(Resource):
    @api.doc('search_query')
    def post(self):
        '''Search users, business accounts, or co-working spaces given some keywords.
           It returns a record. It limits the result to only contain at most 10 spaces,
           business profiles, or users.
        '''
        with create_session() as session:
            #COllect record of normal users that matched the full text search query
            user_response = session.write_transaction(get_nodes_for_user_search, api.payload['query'])
            user_records = user_response.records()

            #COllect record of business profiles that matched the full text search query
            business_response = session.write_transaction(get_nodes_for_business_search, api.payload['query'])
            business_records = business_response.records()

            #Collect record of co-working spaces that matched the full text search query
            space_response = session.write_transaction(get_nodes_for_space_search, api.payload['query'])
            space_records = space_response.records()

            #Collect record of tags that matched the full text search query
            tag_response = session.write_transaction(get_nodes_for_tag_search, api.payload['query'])
            tag_records = tag_response.records()
                
            data = []
            #Append all the profiles that used a tag in tag records.
            for val in get_accouts_with_tags(tag_records, session):
                data.append(val)
            
            #Append all the normal users that matched the full text search to data.
            for record in user_records:
                extracted_user = dict(record.data().get('node').items())
                extracted_user['score'] = record.data()['score']
                extracted_user['profile_type'] = "person"
                formatted_user = user_result_schema.dump(extracted_user)
                data.append(formatted_user)

            #Append all the business profiles that matched the full text search to data.
            for record in business_records:
                extracted_business = dict(record.data().get('node').items())
                extracted_business['score'] = record.data()['score']
                extracted_business['profile_type'] = "business"
                formatted_business = business_result_schema.dump(extracted_business)
                data.append(formatted_business)

            #Append all the coworking spaces that matched the full text search to data.
            for record in space_records:
                extracted_space = dict(record.data().get('node').items())
                extracted_space['score'] = record.data()['score']
                extracted_space['profile_type'] = "space"
                formatted_space = space_result_schema.dump(extracted_space)
                data.append(formatted_space)
            
            #delete duplicate nodes in data.
            [dict(t) for t in {tuple(d.items()) for d in data}]
            return data


#TODO move subfunctionalities to helper file.