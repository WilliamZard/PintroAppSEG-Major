

def get_user_by_email(tx, user_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    # NOTE: tag labels are hardcoded here. If they change in tags csv, must be changed here.
    query = f"""
    MATCH (user:Person {{email: '{user_email}'}})
    OPTIONAL MATCH (user)-->(skill_tag:Tag:CanHelpWithTag)
    OPTIONAL MATCH (user)-->(passion_tag:Tag:PassionsTag)
    RETURN user, COLLECT(skill_tag.name) AS help_others, COLLECT(passion_tag.name) AS passions"""
    return tx.run(query)


def delete_user_by_email(tx, user_email):
    '''Deletes user node, all outbound relationships, and all posts.'''
    query = f"""
    MATCH(n: Person {{email: '{user_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)


def create_user(tx, fields):
    # TODO: update this function to use logic of above one.
    query = "CREATE (new_user: Person {" + ", ".join(
        f"""{k}: \"{v}\"""" for (k, v) in fields.items()) + "})"
    return tx.run(query)


def get_posts_of_followings_of_a_user(tx, email):
    query = f"""
        MATCH (:Person {{email: '{email}'}})
        -[:FOLLOWS]->(user:Person)
        -[:POSTED]->(post:Post)
        RETURN post.content AS content, post.modified AS modified, post.uuid AS uuid, post.created AS created, user.email as user_email"""
    return tx.run(query)


def get_followers_of_a_user(tx, email):
    query = f"""
        MATCH (follower)-[:FOLLOWS]->(:Person {{email: '{email}'}}) RETURN follower.full_name AS full_name, follower.email AS email
    """
    return tx.run(query)


def get_followings_of_a_user(tx, email):
    query = f"""
        MATCH (:Person {{email: '{email}'}})-[:FOLLOWS]->(follower) RETURN follower.full_name AS full_name, follower.email AS email
    """
    return tx.run(query)
