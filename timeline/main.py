import requests
import re
from operator import itemgetter


def generate_timeline(request):
    '''Fetch a users timeline by their email.'''
    request_json = request.get_json()
    if request_json and 'email' in request_json:
        email = request_json['email']
        if not _valid_email(email):
            return "Invalid Email"  # TODO add status code
        response = requests.get(
            f'https://bluej-pintro-project.appspot.com/users/{email}/followings/posts')
        if response.status_code > 500:
            return response.status_code

        data = response.json()

        # Sort by date modified
        data.sort(key=itemgetter('modified'), reverse=True)

        return str(data)
    else:
        return "Email field empty."


def _valid_email(email):
    return re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)
