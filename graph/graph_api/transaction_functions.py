#TODO docstrings
def get_user(tx, user_email):
    return tx.run(f"MATCH (user {{email: '{user_email}'}}) return user")

