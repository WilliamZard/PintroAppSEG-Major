import requests
import re
from flask import make_response
from marshmallow import Schema, fields
from operator import itemgetter


class PostSchema(Schema):
    content = fields.Str(required=True)
    user_email = fields.Email()
    uuid = fields.UUID(required=True)
    modified = fields.DateTime(required=True)


def generate_timeline(request):
    '''Fetch a users timeline by their email.'''
    email = request.path[1:]  # exclude slash at beginning of path
    if not _valid_email(email):
        return make_response(b'', 422)
    response = requests.get(
        f'https://bluej-pintro-project.appspot.com/users/{email}/followings/posts')
    posts_schema = PostSchema()
    deserialised = posts_schema.load(response.json(), many=True)
    deserialised.sort(key=itemgetter('modified'))

    return deserialised


def _valid_email(email):
    return re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)

# For dev
# if __name__ == '__main__':
#    response = generate_timeline('john.snow@winteriscoming.wes')
#    print(response)
