import requests
from flask import make_response


def generate_timeline(request):
    '''Fetch a users timeline by their email.'''
    # TODO: test
    # TODO: account for invalid email, non-existing email
    email = request.path[1:]  # exclude slash at beginning of path
    if not _valid_email(email):
        return make_response(b'', 422)
    return requests.get(f'https://bluej-pintro-project.appspot.com/users/{email}').content


def _valid_email(email):
    import re
    return re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)
