from graph_api.apis.image_storing import *
from ast import literal_eval
from neo4j import Transaction, BoltStatementResult
from typing import Dict

Node_properties = Dict[str, str]


def get_account_field(tx: Transaction, account_email: str, label: str, field: str) -> BoltStatementResult:
    """Gets the required field of a node in the database, identified by its email."""
    query = f"""MATCH(n:{label} {{email:'{account_email}'}})
                RETURN n.{field} as {field}"""
    return tx.run(query)


def set_properties(tx: Transaction, label: str, match_field: str, match_property: str, set_properties: Node_properties) -> BoltStatementResult:
    """Update the properties of an existing node, identified by a specific field in that node."""
    if 'profile_image' in set_properties:
        # upload the image on gcp first and then store its url.
        if len(set_properties['profile_image']) > 0:
            old_image_url = dict(get_account_field(
                tx, match_property, label, 'profile_image').data()[0])['profile_image']
            set_properties['profile_image'] = update_data_from_gcs(
                old_image_url, literal_eval(set_properties['profile_image']))
    query = f"MATCH (user:{label} {{{match_field}: '{match_property}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in set_properties.items())
    return tx.run(query)


def create_node(tx: Transaction, label: str, properties: Node_properties) -> BoltStatementResult:
    """Create a new node in the database of a given type and initialise its fields."""
    # If an image is given, store it in GSP and get its url
    if 'profile_image' in properties:
        if len(properties['profile_image']) > 0:
            properties['profile_image'] = upload_data_to_gcs(
                literal_eval(properties['profile_image']))

    query = f"CREATE (new_node:{label}" + "{" + ", ".join(
        f"""{k}: \"{v}\"""" for (k, v) in properties.items()) + "})"
    return tx.run(query)


def create_relationship(tx: Transaction,
                        s_node_labels: str, s_node_properties: Node_properties,
                        e_node_labels: str, e_node_properties: Node_properties,
                        relationship_type: str, relationship_properties: Node_properties = None) -> BoltStatementResult:
    """
    Create a new relationship between two nodes.

    The nodes are matched by specific fields, and the fields in the relationship itself are initialised by the given fields for it.
    """
    # TODO: the input dictionaries to this function could be constructed differently. No need to specify labels. Just
    # properties to match by, and relationship type. Labels already in node objects.
    s_node_properties = _make_properties_string(s_node_properties)
    e_node_properties = _make_properties_string(e_node_properties)
    if relationship_properties is None:
        relationship_properties = ""
    else:
        relationship_properties = _make_properties_string(
            relationship_properties)
    query = f"""
    MATCH (starting_node:{s_node_labels} {s_node_properties})
    MATCH (ending_node:{e_node_labels} {e_node_properties})
    CREATE (starting_node)-[:{relationship_type}{relationship_properties}]->(ending_node)
    """
    return tx.run(query)


def delete_relationship(tx: Transaction,
                        s_node_labels: str, s_node_properties: Node_properties,
                        e_node_labels: str, e_node_properties: Node_properties,
                        relationship_type: str) -> BoltStatementResult:
    """Delete a relationship between two nodes, matching each node by specific fields and the relationship's type."""
    # TODO: the input dictionaries to this function could be constructed differently. No need to specify labels. Just
    # properties to match by, and relationship type. Labels already in node objects.
    s_node_properties = _make_properties_string(s_node_properties)
    e_node_properties = _make_properties_string(e_node_properties)
    query = f"""
    MATCH (starting_node:{s_node_labels} {s_node_properties})-[rel:{relationship_type}]->(ending_node:{e_node_labels} {e_node_properties})
    DELETE rel
    """
    return tx.run(query)


def _make_properties_string(properties: Node_properties) -> str:
    """Helper function for converting node properties into usable Cypher syntax."""
    return ", ".join(
        f"""{{{k}: "{v}"}}""" for k, v in properties.items())
