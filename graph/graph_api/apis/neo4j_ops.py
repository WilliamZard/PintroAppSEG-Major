from neo4j import GraphDatabase
from flask import g
import os
import datetime


def connect():
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


driver = connect()


def create_session():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db


# TODO: consider using something like this:
"""
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()
"""

""" Functions for Users """
# TODO: start grouping functions by resource type for organisation's sake


def get_user_by_email(tx, user_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    query = f"""MATCH (user:Person {{email: '{user_email}'}})-->(tag:Tag) RETURN user, COLLECT(tag.name) AS tags, COLLECT(labels(tag)) AS tag_labels"""
    return tx.run(query)


def delete_user_by_email(tx, user_email):
    '''Deletes user node, all outbound relationships, and all posts.'''
    query = f"""
    MATCH(n: Person {{email: '{user_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)


def set_user_fields(tx, user_email, fields):
    '''
    Sets properties of user with user_email to fields given in fields.
    The query is dynamic. It only operates on fields that are given in the fields paramater.
    This query will also update relationships with tags.
    '''
    if 'tags' in fields:
        tags = fields['tags']
        fields.pop('tags')

    # NOTE: this could error when assigning string values that need quotations
    match_query = f"MATCH (user:Person {{email: '{user_email}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in fields.items())
    create_tag_query = f"""
    WITH {tags} AS tag_uuids
    UNWIND tag_uuids AS tag_uuid
    MATCH (tag:Tag {{uuid: tag_uuid}})
    MATCH (user:Person {{email: '{user_email}'}})
    MERGE (user)-[:TAGGED]->(tag)"""
    query = match_query + create_tag_query
    return tx.run(query)


def create_user(tx, fields):
    if 'tags' in fields:
        tags = fields['tags']
        fields.pop('tags')
    create_user_query = "CREATE (new_user: Person {" + ", ".join(
        f"{k}: '{v}'" for (k, v) in fields.items()) + "})"

    create_TAGGED_relationships_query = f"""
    WITH {tags} AS tag_uuids
    UNWIND tag_uuids AS tag_uuid
    MATCH(tag: Tag {{uuid: tag_uuid}})
    MATCH(user: Person {{email: '{fields['email']}'}})
    CREATE(user)-[:TAGGED] -> (tag)"""
    query = create_user_query + create_TAGGED_relationships_query
    return tx.run(query)


""" Functions for Businesses """


def get_business_by_email(tx, business_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    query = f"MATCH (user:Business {{email: '{business_email}'}}) RETURN user"
    return tx.run(query)


def delete_business_by_email(tx, business_email):
    return tx.run(f"MATCH (user:Business {{email: '{business_email}'}}) DELETE user")


def set_business_fields(tx, business_email, fields):
    '''
        Function for setting a new email of a user which has a particular email saved in database.
        It returns a BoltStatementResult containing the record of the edited user.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_email = the new email to assign to that user.
    '''
    # NOTE: this could error when assigning string values that need quotations
    query = f"MATCH (user:Business {{email: '{business_email}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in fields.items())
    return tx.run(query)


def create_business(tx, fields):
    query = "CREATE (new_user: Business {" + ", ".join(
        f"{k}: '{v}'" for (k, v) in fields.items()) + "})"
    return tx.run(query)

    """ Functions for Co-working spaces """


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


def set_space_fields(tx, space_email, fields):
    '''
        Function for setting a new email of a user which has a particular email saved in database.
        It returns a BoltStatementResult containing the record of the edited user.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_email = the new email to assign to that user.
    '''
    # NOTE: this could error when assigning string values that need quotations
    query = f"MATCH (user:Space {{email: '{space_email}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in fields.items())
    return tx.run(query)


def create_space(tx, fields):
    query = "CREATE (user: Space {" + ", ".join(
        f"{k}: '{v}'" for (k, v) in fields.items()) + "})"
    return tx.run(query)


"""functions for POSTS"""


def get_post_by_uuid(tx, uuid):
    query = f"MATCH (post:Post {{uuid:'{uuid}'}}) RETURN post"
    return tx.run(query)


def create_post(tx, post_content, user_email, created, modified, uuid):
    query = f"""MATCH (user:Person {{email:'{user_email}'}})   
                CREATE (post:Post {{uuid: '{uuid}', content: '{post_content}', created: datetime('{created}'), modified: datetime('{modified}')}})
                CREATE (user)-[:POSTED]->(post)
                RETURN post 
            """
    return tx.run(query)

# TODO: this function can be more dynamic, no need for fixed paramters. See create user function for guide.


def set_post_fields(tx, uuid, content):
    '''
        Function for setting a new email of a user which has a particular email saved in database.
        It returns a BoltStatementResult containing the record of the edited user.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_email = the new email to assign to that user.
    '''
    # NOTE: this could error when assigning string values that need quotations
    query = f"MATCH (post:Post {{uuid: '{uuid}'}}) SET post.content='{content}'"
    return tx.run(query)


def delete_post(tx, uuid):
    query = f"""MATCH (post:Post {{uuid: '{uuid}'}})
                DETACH DELETE post
             """
    return tx.run(query)


def get_list_of_user_post_dates(tx, user_email):
    query = f"""MATCH (user:Person {{email:'{user_email}'}})-[posted:POSTED]->()
                return collect(posted.date)
             """
    return tx.run(query)

# TODO: different function name

# TODO: delete ORDER BY


def get_posts_for_timeline(tx, user_email):
    query = f"""MATCH (user:Person {{email:'{user_email}'}})-[:FOLLOWS]->()-[posted:POSTED]->(post:Post)
                WITH posted, post
                ORDER BY posted.date
                return post
             """
    return tx.run(query)


def get_posts_of_followings_of_a_user(tx, email):
    query = f"""
        MATCH (:Person {{email: '{email}'}})
        -[:FOLLOWS]->(user:Person)
        -[:POSTED]->(post:Post)
        RETURN post.content AS content, post.modified AS modified, post.uuid AS uuid"""
    return tx.run(query)


"""functions for FOLLOW RELATIONSHIPS"""


def create_follow_relationship(tx, follow_requester, follow_request_recipient):
    query = f"""
        MATCH (follow_requester:Person),(follow_request_recipient:Person)
        WHERE follow_requester.email = '{follow_requester}' AND follow_request_recipient.email = '{follow_request_recipient}'
        CREATE (follow_requester)-[f:REQUESTED_FOLLOW]->(follow_request_recipient)
        RETURN f
    """
    return tx.run(query)


def approve_follow_request(tx, follow_requester, follow_request_recipient):
    query = f"""
        MATCH (follow_requester:Person)-[req:REQUESTED_FOLLOW]->(follow_request_recipient:Person)
        WHERE follow_requester.email = '{follow_requester}' AND follow_request_recipient.email = '{follow_request_recipient}'
        CALL apoc.refactor.setType(req, 'FOLLOWS') YIELD input, output RETURN follow_requester, follow_request_recipient
    """
    print(query)
    return tx.run(query)


def delete_follow_relationship(tx, follow_requester, follow_request_recipient):
    print(query)
    query = f"""
        MATCH (follower {{email: '{follow_requester}' }})-[f:REQUESTED_FOLLOW]->(following {{email: '{follow_request_recipient}'}})
        DELETE f
    """
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


def get_posts_of_followings_of_a_user(tx, email):
    query = f"""
        MATCH (:Person {{email: '{email}'}})
        -[:FOLLOWS]->(user:Person)
        -[:POSTED]->(post:Post)
        RETURN post.content AS content, post.modified AS modified, post.uuid AS uuid"""
    return tx.run(query)


def get_tags(tx, labels):
    labels = ' OR '.join(f'tag:{label}' for label in labels)
    query = f"""
        MATCH (tag)
        WHERE {labels}
        RETURN tag
    """
    print(query)
    return tx.run(query)
