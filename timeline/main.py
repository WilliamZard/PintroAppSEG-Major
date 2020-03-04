import requests
from flask import make_response


def generate_timeline(email):  # request):
    '''Fetch a users timeline by their email.'''
    # TODO: test
    # TODO: account for invalid email, non-existing email
    # email = request.path[1:]  # exclude slash at beginning of path
    # if not _valid_email(email):
    #    return make_response(b'', 422)
    response = requests.get(
        f'https://bluej-pintro-project.appspot.com/users/{email}/followings/posts').content
    return response


def _valid_email(email):
    import re
    return re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)


if __name__ == '__main__':
    response = generate_timeline('john.snow@winteriscoming.wes')
    print(response)
