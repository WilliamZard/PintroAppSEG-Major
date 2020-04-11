import requests
import re
from operator import itemgetter


def generate_timeline(request):
    '''Fetch a users timeline by their email.'''
    headers = request.headers
    if 'Authorization' not in headers:
        return '401 UNAUTHORIZED'

    user_token = headers['Authorization']

    request_json = request.get_json()
    if not request_json or 'email' not in request_json:
        return "422 INVALID PAYLOAD"

    email = request_json['email']
    if not _valid_email(email):
        return "422 INVALID EMAIL"

    response = requests.get(
        f'https://bluej-pintro-project.appspot.com/users/{email}/followings/posts',
        headers={'Authorization': user_token})
    if response.status_code == 404:
        return "404 USER NOT FOUND"
    if response.status_code > 500:
        return response.status_code

    data = response.json()

    # Sort by date modified
    data.sort(key=itemgetter('modified'), reverse=True)
    data = {'results': data}

    return data


def _valid_email(email):
    return re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)
