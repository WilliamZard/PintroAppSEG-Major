import datetime
import os
from neo4j import GraphDatabase, Transaction, BoltStatementResult
from graph_api.apis.image_storing import *


from .test_data.users import *
from .test_data.businesses import *
from .test_data.spaces import *
from .test_data.posts import *
from .test_data.tags import *
from .test_data.businesses import *
from .test_data.spaces import *
from .test_data.chatrooms import *
from .test_data.notifications import *

from typing import Dict, List, Union


def create_node(tx: Transaction, labels: Union[List[str], str], properties: Dict[str, str]) -> BoltStatementResult:
    '''
        Function that creates a node in the database given its properties and its label.
    '''
    '''Args:
        -tx = context where to run cypher queries.
        -labels = a string or a list of strings representing the label/labels for the node/nodes to create.
        -properties = A dictionary of strings representing the properties for each node that needs to be created.
    '''
    if isinstance(labels, list):
        labels = ':'.join(labels)
    query = f"CREATE (new_node:{labels} {{" + ", ".join(
        f"""{k}: \"{v}\"""" if k != 'profile_image' else f"""{k}: \"{upload_data_to_gcs(v)}\"""" for (k, v) in properties.items()) + "})"
    return tx.run(query)


def create_relationship(tx: Transaction,
                        s_node_properties:  Dict[str, str], s_node_labels: str,
                        e_node_properties:  Dict[str, str], e_node_labels: str,
                        relationship_type: str, relationship_properties=None) -> BoltStatementResult:
    '''
        Function that creates a relationship between two different nodes.
    '''
    '''Args:
        -tx = context where to run cypher queries.
        -s_node_properties = A dictionary of strings representing the identifier properties of the node where the relation
        starts
        -s_node_labels = A string representing the label of the node where the relation starts.
        -e_node_properties = A dictionary of strings representing the identifier properties of the node where the relation
        ends
        -e_node_labels = A string representing the label of the node where the relation ends.
        -relationship_type = A string representing the relation type.
        relationship_properties = A dictionary of strings representing properties that the relation might have.
    '''
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


def basic_user_node(user: User) -> Dict[str, str]:
    '''
        Function that formats a user into a valid neo4j User node
    '''
    '''Args:
        user = a user that needs to be formatted into a User node.
    '''
    return {'properties': dict(user), 'labels': 'Person'}


def basic_chatroom_node(chatroom: Chatroom) -> Dict[str, str]:
    '''
        Function that formats a user into a valid neo4j Chatroom node
    '''
    '''Args:
        chatroom = a chatroom that needs to be formatted into a Chatroom node.
    '''
    return {'properties': dict(chatroom), 'labels': 'Chatroom'}


def basic_post_node(post: Post) -> Dict[str, str]:
    '''
        Function that formats a post into a valid neo4j Post node
    '''
    '''Args:
        post = a post that needs to be formatted into a Post node.
    '''
    return {'properties': dict(post), 'labels': 'Post'}


def basic_space_node(space: Space) -> Dict[str, str]:
    '''
        Function that formats a user into a valid neo4j Space node
    '''
    '''Args:
        space = a space that needs to be formatted into a Space node.
    '''
    return {'properties': dict(space), 'labels': 'Space'}


def basic_business_node(business: Business) -> Dict[str, str]:
    '''
        Function that formats a business into a valid neo4j Business node
    '''
    '''Args:
        business = a Business that needs to be formatted into a Business node.
    '''
    return {'properties': dict(business), 'labels': 'Business'}


def basic_tag_node(tag: Tag, labels='Tag') -> Dict[str, str]:
    '''
        Function that formats a tag into a valid neo4j Tag node
    '''
    '''Args:
        tag = a tag that needs to be formatted into a Tag node.
        labels = a str representing the label for such tag. 
    '''
    return {'properties': dict(tag), 'labels': labels}
