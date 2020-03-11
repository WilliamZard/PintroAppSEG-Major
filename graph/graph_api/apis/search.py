from flask import make_response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

from .neo4j_ops import create_session, get_nodes_for_user_search, get_nodes_for_business_search, get_nodes_for_space_search



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
            user_response = session.write_transaction(get_nodes_for_user_search, api.payload['query'])
            user_records = user_response.records()

            business_response = session.write_transaction(get_nodes_for_business_search, api.payload['query'])
            business_records = business_response.records()

            space_response = session.write_transaction(get_nodes_for_space_search, api.payload['query'])
            space_records = space_response.records()

            data = []
            for record in user_records:
                extracted_user = dict(record.data().get('node').items())
                extracted_user['score'] = record.data()['score']
                extracted_user['profile_type'] = "person"
                formatted_user = user_result_schema.dump(extracted_user)
                data.append(formatted_user)

            for record in business_records:
                extracted_business = dict(record.data().get('node').items())
                extracted_business['score'] = record.data()['score']
                extracted_business['profile_type'] = "business"
                formatted_business = business_result_schema.dump(extracted_business)
                data.append(formatted_business)

            for record in space_records:
                extracted_space = dict(record.data().get('node').items())
                extracted_space['score'] = record.data()['score']
                extracted_space['profile_type'] = "space"
                formatted_space = space_result_schema.dump(extracted_space)
                data.append(formatted_space)
            
            return data


