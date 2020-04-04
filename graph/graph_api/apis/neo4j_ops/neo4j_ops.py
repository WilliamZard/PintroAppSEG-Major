"""from neo4j import GraphDatabase
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
""
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()
""

"" Functions for Users ""
# TODO: start grouping functions by resource type for organisation's sake


"" Functions for Busineses ""


""functions for POSTS""


""
def get_posts_for_timeline(tx, user_email):
    query = f""MATCH(user: Person {{email: '{user_email}'}})-[:FOLLOWS] -> ()-[posted:POSTED] -> (post: Post)
                WITH posted, post
                ORDER BY posted.date
                return post
             ""
    return tx.run(query)"""


"""functions for FOLLOW RELATIONSHIPS"""


""" functions for AFFILIATIONS """
