from neo4j import GraphDatabase
from flask import g
import os


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
