

def get_business_by_email(tx, business_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    query = f"""
    MATCH (user:Business {{email: '{business_email}'}})
    OPTIONAL MATCH (user)-->(tag:Tag)
    OPTIONAL MATCH (person:Person)-[:AFFILIATED_WITH]->(user)
    RETURN user, COLLECT(DISTINCT tag.name) AS tags, COLLECT(person.email) AS team_members"""
    return tx.run(query)


def delete_business_by_email(tx, business_email):
    query = f"""
    MATCH(n: Business {{email: '{business_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)
