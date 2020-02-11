from werkzeug.security import generate_password_hash, check_password_hash

#TODO docstrings
def get_user(tx, user_email):
    return tx.run(f"MATCH (user {{email: '{user_email}'}}) return user")

def set_user_email(tx, user_email, new_email):
    return tx.run(f"MATCH (n:Person {{email: '{user_email}'}}) SET n.email = '{new_email}' RETURN n")

def create_user(tx, user):
    password = user['password']
    if not password:
        return dict(('message', 'password was not found'))
    email = user['email']
    if not email:
        return dict(('message', 'email was not found'))
    full_name = user['full_name']
    if not full_name:
        return dict(('message', 'full name was not found'))
    preferred_name = user['preferred_name']
    if not preferred_name:
        preferred_name = ''
    gender = user['gender']
    if not gender:
        gender = ''
    phone = user['phone']
    if not phone:
        phone = ''
    return tx.run(f"""CREATE (newUser:Person{{email:'{email}', hash_password:'{generate_password_hash(password)}', fullName:'{full_name}',
                  preferredName:'{preferred_name}', gender:'{gender}', phone:'{phone}'}}) RETURN newUser""")
#TODO Check if someone has already has that email.