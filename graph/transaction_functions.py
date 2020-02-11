from werkzeug.security import generate_password_hash, check_password_hash
from neo4j import exceptions
from neobolt.exceptions import ConstraintError

#TODO docstrings
def get_user_by_email(tx, user_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult. 
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) return user")

def get_user_by_full_name(tx, user_fullname):
    '''
        Function that gets all the data related to a user with a particular full name.
        It returns a BoltStatementResult. 
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_fullname = the full name of the user whose data needs to be retrieved.
    '''
    return tx.run(f"MATCH (user:Person {{fullName: '{user_fullname}'}}) return user")

def get_user_by_preferred_name(tx, user_preferred_name):
    '''
        Function that gets all the data related to a user with a particular full name.
        It returns a BoltStatementResult. 
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_preferred_name = the full name of the user whose data needs to be retrieved.
    '''
    return tx.run(f"MATCH (user:Person {{preferredName: '{user_preferred_name}'}}) return user")

def set_user_email(tx, user_email, new_email):
    '''
        Function for setting a new email of a user which has a particular email saved in database.
        It returns a BoltStatementResult containing the record of the edited user. 
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_email = the new email to assign to that user.
    '''
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) SET user.email = '{new_email}' RETURN user")


def set_user_full_name(tx, user_email, new_fullname):
    '''
        Function for setting a new full name of a user who has a specific emailfull name saved in the database.
        It returns a BoltStatementResult containing the record of the edited user. 
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_fullname = the new full name to assign to that user.
    '''
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) SET user.fullName = '{new_fullname}' RETURN user")

def set_user_preferred_name(tx, user_email, new_preferred_name):
    '''
        Function for setting a new preferred name of a user who has a specific email saved in the database.
        It returns a BoltStatementResult containing the record of the edited user. 
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_preferred_name = the new preferred name to assign to that user.
    '''
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) SET user.fullName = '{new_preferred_name}' RETURN user")

def set_user_short_bio(tx, user_email, new_shortbio):
    '''
        Function for setting a new full name of a user who has a specific full name saved in the database.
        It returns a BoltStatementResult containing the record of the edited user. 
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_shortbio = the new full name to assign to that user.
    '''
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) SET user.short_bio = '{new_shortbio}' RETURN user")

def set_user_story(tx, user_email, new_story):
    '''
        Function for setting a new full name of a user who has a specific full name saved in the database.
        It returns a BoltStatementResult containing the record of the edited user. 
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_story = the new story to assign to that user.
    '''
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) SET user.story = '{new_story}' RETURN user")


def create_user(tx, user):
    '''
        It creates a user given some credentials such as email, password, full name, preferred name(optional), gender(optional)
        phone(optional), a short bio(optional), a profile picture(optional), location(optional), a current job title(optional), 
        and a story(optional).
        The creation of the node might not succeed if the email provided was already in use by an existing user in the database,
        or some essential data was not given (such as email, password, or full name of the user). 
        The value returned is either a BoltStatementResult if the operation went through, or a dictionary containing the reason 
        for failure if an error occurred 
    '''
    '''Args
        tx = the context from where to run chipher statements and retreiving information from the db.
        user = a dictionary containing all the data that describing the user that needs to be stored in the database.
    '''
    password = user['password']
    if not password:
        return {'error': 'password was not found'}
    email = user['email']
    if not email:
        return {'error': 'email was not found'}
    full_name = user['full_name']
    if not full_name:
        return {'error': 'full name was not found'}
    preferred_name = user.get('preferred_name', '')
    gender = user.get('gender', '')
    phone = user.get('phone', '')
    image = user.get('image','')
    job_title = user.get('job_title', '')
    short_bio = user.get('short_bio', '')
    story = user.get('story', '')
    location = user.get('location', '')
    education = user.get('education', '')

    if there_exist_account(tx, email):
        return {'error': 'violation of constraint. User already exists with this email in database.'}

    return tx.run(f"""CREATE (newUser:Person{{email:'{email}', hash_password:'{generate_password_hash(password)}', fullName:'{full_name}',
              preferredName:'{preferred_name}', gender:'{gender}', phone:'{phone}', profilePic:'{image}', job_title:'{job_title}', 
              short_bio:'{short_bio}', story:'{story}', location:'{location}', education:'{education}'}}) RETURN newUser""")




def check_user(tx, credentials):
    '''
        Function that checks that there exists a user in the database with a given email and password. If there is, it returns
        a record for that user containing its information, otherwise it might return a dictionary containing an error message 
        describing what went wrong or what did not match.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        credentials= a dictionary containing email and password that needs to be checked
    '''
    password = credentials['password']
    if not password:
        return {'error': 'password was not found'}
    email = credentials['email']
    if not email:
        return {'error': 'email was not found'}

    node_with_email =  tx.run(f"""MATCH (p:Person) where p.email = '{email}' return p""")
    if not node_with_email:
        return {'error': 'no user with such email'}

    node_record = node_with_email.single()
    h_p = dict(node_record['p'].items()).get('hash_password')


    if check_password_hash(h_p, password):
        return node_record
    else:
        return {'error': 'password did not match'}

def there_exist_account(tx, email):
    ''' 
        Function for checking wether an account with a given email is already present in the database.
        It returns True if there is one, or false if there is not.
    '''
    ''' Args
        tx = the context where to run the query statement for the database.
        email = the email that needs to be checked.
    '''
    session = tx.run(f"""MATCH (p:Person) where p.email = '{email}' return count(p) as count""")
    number_of_nodes = session.single()['count']
    if number_of_nodes > 0:
        return True
    else:
        return False
