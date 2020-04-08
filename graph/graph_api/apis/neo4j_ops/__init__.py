from neo4j import GraphDatabase
import neo4j
from flask import g
import os


def connect() -> neo4j.Driver:
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


driver = connect()


def create_session() -> neo4j.Session:
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db
