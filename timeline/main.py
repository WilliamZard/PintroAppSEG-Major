import requests
from flask import make_response


def generate_timeline(request):
    '''Fetch a users timeline by their email.'''
    return request.path

    """
    if not _valid_email(email):
        return 'Invalid email'
    return 'timeline response'
    base_url = ''
    response = requests.get(base_url + f'/users/{email}')
    return make_response(response.content, 200)
    """


def _valid_email(email):
    import re
    return re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)
