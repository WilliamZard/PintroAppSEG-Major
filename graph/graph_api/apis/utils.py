# TODO: docsstrings

# TODO: docsstrings


def valid_email(email):
    import re
    return re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)
