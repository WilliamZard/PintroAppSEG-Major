from neo4j import GraphDatabase
import neo4j
from flask import g
import os


def connect() -> neo4j.Driver:
    """Create a new connection object to the NEO4J database."""
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


driver = connect()


def create_session() -> neo4j.Session:
    """Initialise a new NEO4J connection object if it does not exist, and return it."""
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db
