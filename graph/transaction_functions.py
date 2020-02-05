#TODO docstrings
def get_user(tx, user_email):
    return tx.run(f"MATCH (user {{email: '{user_email}'}}) return user")

def set_user_email(tx, user_email, new_email):
    return tx.run(f"MATCH (n:Person {{email: '{user_email}'}}) SET n.email = '{new_email}' RETURN n")
