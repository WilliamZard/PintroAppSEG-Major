# TODO: docsstrings
import re


# TODO: docsstrings
def validate_email(func):
    def wrapper(self, email):
        valid_email = re.search(
            '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)
        if not valid_email:
            return 'Invalid email given', 400
        return func(self, email)
    return wrapper
