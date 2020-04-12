"""
Use this file to specify Cypher queries that should be ran manually
after a database has been created. Similar to a startup script.
"""
import os
from neo4j import GraphDatabase, Transaction, BoltStatementResult


def connect() -> GraphDatabase.driver:
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


def create_full_text_indexes(tx: Transaction) -> None:
    queries = [
        "CALL db.index.fulltext.createNodeIndex('SearchSpaceIndex', ['Space'], ['full_name', 'email', 'short_bio', 'story'])",
        "CALL db.index.fulltext.createNodeIndex('SearchUserIndex', ['Person'], ['full_name', 'email', 'short_bio', 'story'])",
        "CALL db.index.fulltext.createNodeIndex('SearchBusinessIndex', ['Business'], ['full_name', 'email', 'short_bio', 'story'])",
        "CALL db.index.fulltext.createNodeIndex('SearchTagIndex', ['Tag'], ['name'])"
    ]
    for query in queries:
        tx.run(query)


if __name__ == '__main__':
    driver = connect()
    with driver.session() as session:
        session.write_transaction(create_full_text_indexes)
    driver.close()
