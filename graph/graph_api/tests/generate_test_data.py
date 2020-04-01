import datetime
import os
from neo4j import GraphDatabase


from .test_data.users import *
from .test_data.businesses import *
from .test_data.spaces import *
from .test_data.posts import *
from .test_data.tags import *
from .test_data.businesses import *
from .test_data.spaces import *
from .test_data.chatrooms import *
from .test_data.notifications import *


def create_node(tx, labels, properties):
    # NOTE: this current code assumes all properties are a string.
    if isinstance(labels, list):
        labels = ':'.join(labels)
    query = f"CREATE (new_node:{labels} {{" + ", ".join(
        f"""{k}: \"{v}\"""" for (k, v) in properties.items()) + "})"
    return tx.run(query)


def create_relationship(tx,
                        s_node_properties, s_node_labels,
                        e_node_properties, e_node_labels,
                        relationship_type, relationship_properties=None):
    # TODO: the input dictionaries to this function could be constructed differently. No need to specify labels. Just
    # properties to match by, and relationship type. Labels already in node objects.
    s_node_properties = ", ".join(
        f"""{{{k}: "{v}"}}""" for k, v in s_node_properties.items())
    e_node_properties = ", ".join(
        f"""{{{k}: "{v}"}}""" for k, v in e_node_properties.items())
    if relationship_properties is None:
        relationship_properties = ""
    else:
        relationship_properties = ", ".join(
            f"""{{{k}: "{v}"}}""" for k, v in relationship_properties.items()
        )
    query = f"""
    MATCH (starting_node:{s_node_labels} {s_node_properties})
    MATCH (ending_node:{e_node_labels} {e_node_properties})
    CREATE (starting_node)-[:{relationship_type} {relationship_properties}]->(ending_node)
    """
    return tx.run(query)


def basic_user_node(user):
    return {'properties': dict(user), 'labels': 'Person'}


def basic_chatroom_node(user):
    return {'properties': dict(user), 'labels': 'Chatroom'}


def basic_post_node(post):
    return {'properties': dict(post), 'labels': 'Post'}


def basic_space_node(user):
    return {'properties': dict(user), 'labels': 'Space'}


def basic_business_node(business):
    return {'properties': dict(business), 'labels': 'Business'}


def basic_tag_node(tag):
    return {'properties': dict(tag), 'labels': 'Tag'}


def create_full_text_indexes(tx):
    queries = []
    queries.append(
        "CALL db.index.fulltext.createNodeIndex('SearchSpaceIndex', ['Space'], ['full_name', 'email', 'short_bio', 'story'])")
    queries.append(
        "CALL db.index.fulltext.createNodeIndex('SearchUserIndex', ['Person'], ['full_name', 'email', 'short_bio', 'story'])")
    queries.append(
        "CALL db.index.fulltext.createNodeIndex('SearchBusinessIndex', ['Business'], ['full_name', 'email', 'short_bio', 'story'])")
    queries.append(
        "CALL db.index.fulltext.createNodeIndex('SearchTagIndex', ['Tag'], ['name'])")
    for query in queries:
        tx.run(query)
