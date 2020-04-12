"""Utility functions and test fixtures."""
import pytest

from graph_api import create_app

from .generate_test_data import create_node, create_relationship
import os
from neo4j import GraphDatabase, Transaction, BoltStatementResult
from graph_api.apis.image_storing import clear_bucket

from flask import Flask
from typing import List


def connect() -> GraphDatabase.driver:
    """Instantiate a Neo4j database connection."""
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


def clear_db() -> None:
    """Empty the testing database of all nodes, relationships, and indexes."""
    # TODO: refactor this function
    clear_bucket()
    DELETE_ALL_NODES = "MATCH(n) DETACH DELETE n"
    driver = connect()
    with driver.session() as session:
        session.write_transaction(_run_query, DELETE_ALL_NODES)
    driver.close()


def _run_query(tx: Transaction, query: str) -> BoltStatementResult:
    return tx.run(query)


@pytest.fixture()
def populate_db() -> None:
    """Populate the test database with the given nodes and relationships."""
    # TODO: add example inputs
    def populate(nodes_to_create=[], relationships_to_create=[]) -> None:
        driver = connect()
        with driver.session() as session:
            # Where nodes_to_create is list of dictionaries containing properties and labels
            for node in nodes_to_create:
                session.write_transaction(create_node, **node)
            # Where relationships_to_create is list of dictionaries containing properties and labels for both nodes, plus relationship type
            for relationship in relationships_to_create:
                session.write_transaction(create_relationship, **relationship)
        driver.close()
    yield populate
    clear_db()


@pytest.fixture()
def app() -> Flask:
    app = create_app()
    app.testing = True

    with app.test_client() as client:
        yield client
