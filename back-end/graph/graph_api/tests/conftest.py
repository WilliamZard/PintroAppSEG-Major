"""Utility functions and test fixtures."""
import pytest

from graph_api import create_app

from .generate_test_data import create_node, create_relationship
import os
from neo4j import GraphDatabase, Transaction, BoltStatementResult
from graph_api.apis.image_storing import clear_bucket

from flask import Flask

from typing import List, Dict


def connect() -> GraphDatabase.driver:
    """Instantiate a Neo4j database connection."""
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


def clear_db() -> None:
    """Empty the testing database of all nodes, relationships, and indexes."""
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
    def populate(nodes_to_create: List[Dict] = [], relationships_to_create: List[Dict] = []) -> None:
        """
        nodes_to_create example:
            [{
                'properties': {
                    'full_name': 'Default Name', 'preferred_name': 'Defaulter', 'profile_image': '',
                    'short_bio': 'Default Short Bio', 'gender': 'Default Gender', 'story': 'Default Story',
                    'email': 'duke@wellington.com', 'phone_number': '000', 'job_title': 'Default Job Title',
                    'current_company': 'Default Current Company', 'years_in_industry': '100', 'industry': 'Default Industry',
                    'previous_company': 'Default previous company', 'previous_company_year_finished': '10',
                    'university': 'Default University', 'university_year_finished': '1812', 'academic_level': 'Default Academic Level',
                    'location': 'Default Location', 'date_of_birth': '01/01/1812', 'active': 'True'
                },
                'labels': 'Person'
            }]
        relationships_to_create example: 
            [{
                's_node_properties': {'email': 'email@example.com', 's_node_labels': 'Example_label',
                'e_node_properties': {'email': 'email@example.com' }, 'e_node_labels': 'Example_label',
                'relationship_type': RELATIONSHIP_EXAMPLE
            }]
        """
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
