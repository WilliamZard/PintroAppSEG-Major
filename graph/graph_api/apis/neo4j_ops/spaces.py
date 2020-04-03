
def get_space_by_email(tx, space_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    return tx.run(f"MATCH (user:Space {{email: '{space_email}'}}) RETURN user")


def delete_space_by_email(tx, space_email):
    return tx.run(f"MATCH (user:Space {{email: '{space_email}'}}) DELETE user")
