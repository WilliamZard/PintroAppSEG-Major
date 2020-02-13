from neo4j import GraphDatabase
from flask import g
import os

uri = os.getenv("NEO4J_URI")
db_user = 'neo4j'
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(db_user, password))


def create_session():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db


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
    return tx.run(f"MATCH (user:Person {{email: '{user_email}'}}) SET " +
                  ", ".join("user.{}={}".format(k, v) for (k, v) in fields.items()))
