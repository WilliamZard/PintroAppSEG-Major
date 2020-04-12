"""
Use this file to specify Cypher queries that should be ran manually
after a database has been created. Similar to a startup script.
"""
import sys
from neo4j import GraphDatabase, Transaction, BoltStatementResult


def connect(uri: str, password: str) -> GraphDatabase.driver:
    db_user = 'neo4j'
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
    uri, password = sys.argv[1], sys.argv[2]
    driver = connect(uri, password)
    with driver.session() as session:
        session.write_transaction(create_full_text_indexes)
    driver.close()
