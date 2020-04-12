from flask import make_response, Response
from flask.json import jsonify
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields

from .utils import *
from .image_storing import *

from .neo4j_ops import create_session
from .neo4j_ops.search import (  # get_users_with_tag, get_spaces_with_tag,
    get_accounts_with_tag, get_nodes_for_business_search,
    get_nodes_for_space_search, get_nodes_for_tag_search,
    get_nodes_for_user_search)

api = Namespace('search', title='Operations for full text search')

# Models needed as payload in request for searching call

query = api.model('Query', {'query': restx_fields.String(
    required=True, title='String to look for relevant search.')})


@api.route('/')
@api.produces('application/json')
@api.expect(query)
class SearchPost(Resource):
    @api.doc('search_query')
    def post(self) -> Response:
        '''Search users, business accounts, or co-working spaces given some keywords or tags.
           It returns a record. It limits the result to only contain at most 10 spaces,
           business profiles, or users.
        '''
        with create_session() as session:
            # COllect record of normal users that matched the full text search query
            user_response = session.write_transaction(
                get_nodes_for_user_search, api.payload['query'])
            user_records = user_response.records()

            # COllect record of business profiles that matched the full text search query
            business_response = session.write_transaction(
                get_nodes_for_business_search, api.payload['query'])
            business_records = business_response.records()

            # Collect record of co-working spaces that matched the full text search query
            space_response = session.write_transaction(
                get_nodes_for_space_search, api.payload['query'])
            space_records = space_response.records()

            # Collect record of tags that matched the full text search query
            tag_response = session.write_transaction(
                get_nodes_for_tag_search, api.payload['query'])
            tag_records = tag_response.records()

            data = []
            # Append all the profiles that used a tag in tag records.
            accounts_with_tags = get_accouts_with_tags(tag_records, session)
            for val in accounts_with_tags:
                val['profile_image'] = get_data_from_gcs(val['profile_image'])
                data.append(val)

            # Append all the normal users that matched the full text search to data.
            for record in user_records:
                extracted_user = dict(record.data().get('node').items())
                extracted_user['score'] = record.data()['score']
                extracted_user['profile_image'] = get_data_from_gcs(
                    extracted_user['profile_image'])
                extracted_user['profile_type'] = "person"
                data.append(extracted_user)

            # Append all the business profiles that matched the full text search to data.
            for record in business_records:
                extracted_business = dict(record.data().get('node').items())
                extracted_business['score'] = record.data()['score']
                extracted_business['profile_image'] = get_data_from_gcs(
                    extracted_business['profile_image'])
                extracted_business['profile_type'] = "business"
                data.append(extracted_business)

            # Append all the coworking spaces that matched the full text search to data.
            for record in space_records:
                extracted_space = dict(record.data().get('node').items())
                extracted_space['score'] = record.data()['score']
                extracted_space['profile_image'] = get_data_from_gcs(
                    extracted_space['profile_image'])
                extracted_space['profile_type'] = "space"
                data.append(extracted_space)

            # delete duplicate nodes in data.
            data = remove_duplicates(data)
            return data
