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
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) RETURN user")


def delete_user_by_email(tx, user_email):
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) DELETE user")


def set_user_fields(tx, user_email, fields):
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
    query = f"MATCH (user:Person {{email: '{user_email}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in fields.items())
    return tx.run(query)


def create_user(tx, fields):
    query = "CREATE (new_user: Person {" + ", ".join(
        f"{k}: '{v}'" for (k, v) in fields.items()) + "})"
    return tx.run(query)


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
