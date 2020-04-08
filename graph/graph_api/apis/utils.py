def valid_email(email: str) -> bool:
    import re
    return re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)
