from flask import make_response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

from .neo4j_ops import create_session, get_nodes_for_search



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
        '''Search a user, business account, or co-working space given some keywords.
           It returns a record.
        '''
        # try:
        #     deserialised_payload = user_schema.load(api.payload)
        # except ValidationError as e:
        #     return make_response(e.messages['email'][0], 422)
        with create_session() as session:
            #try:
            response = session.write_transaction(get_nodes_for_search, api.payload['query'])
            records = response.records()
            data = []
            for record in records:
                #TODO  lot of code duplication here . Might be solved with polymorphism
                if 'Business' in record.get('node').labels:
                    extracted_business = dict(record.data().get('node').items())
                    extracted_business['score'] = record.data()['score']
                    extracted_business['profile_type'] = "business"
                    formatted_business = business_result_schema.dump(extracted_business)
                    data.append(formatted_business)

                elif 'Person' in record.get('node').labels:
                    extracted_user = dict(record.data().get('node').items())
                    extracted_user['score'] = record.data()['score']
                    extracted_user['profile_type'] = "person"
                    formatted_user = user_result_schema.dump(extracted_user)
                    data.append(formatted_user)

                elif 'Space' in record.get('node').labels:
                    extracted_space = dict(record.data().get('node').items())
                    extracted_space['score'] = record.data()['score']
                    extracted_space['profile_type'] = "space"
                    formatted_space = space_result_schema.dump(extracted_space)
                    data.append(formatted_space)
            return data

