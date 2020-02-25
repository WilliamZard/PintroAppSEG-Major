from flask_restx import Namespace, Resource
from .utils import valid_email
from flask import make_response
import requests

api = Namespace('timeline', title='Timeline Endpoint')


# TODO: consider schemas

@api.route('/<string:email>')
@api.produces('application/json')
class Timeline(Resource):
    def get(self, email):
        '''Fetch a users timeline by their email.'''

        if not valid_email(email):
            return make_response('', 422)

        base_url = ''
        response = requests.get(base_url + f'/users/{email}')
        return make_response(response.content, 200)
