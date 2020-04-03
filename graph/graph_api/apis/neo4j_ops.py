from neo4j import GraphDatabase
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
"""
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()
"""

""" Functions for Users """
# TODO: start grouping functions by resource type for organisation's sake


def get_user_by_email(tx, user_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    query = f"""
    MATCH (user:Person {{email: '{user_email}'}})
    OPTIONAL MATCH (user)-->(skill_tag:Tag:Skill)
    OPTIONAL MATCH (user)-->(passion_tag:Tag:Passion)
    RETURN user, COLLECT(skill_tag.name) AS help_others, COLLECT(passion_tag.name) AS passions"""
    return tx.run(query)


def delete_user_by_email(tx, user_email):
    '''Deletes user node, all outbound relationships, and all posts.'''
    query = f"""
    MATCH(n: Person {{email: '{user_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)


def set_user_fields(tx, user_email, fields):
    '''
    Sets properties of user with user_email to fields given in fields.
    The query is dynamic. It only operates on fields that are given in the fields paramater.
    This query will also update relationships with tags.
    '''
    passions = help_others = []
    if 'passions' in fields:
        passions = fields['passions']
        fields.pop('passions')
    if 'help_others' in fields:
        help_others = fields['help_others']
        fields.pop('help_others')
    create_tag_query = f"""
    WITH {passions+help_others} AS tag_names
    UNWIND tag_names AS tag_name
    MATCH (tag:Tag {{name: tag_name}})
    MATCH (user:Person {{email: '{user_email}'}})
    MERGE (user)-[:TAGGED]->(tag)"""

    # NOTE: this could error when assigning string values that need quotations
    query = f"MATCH (user:Person {{email: '{user_email}'}}) SET " + \
        ", ".join(f"""user.{k}=\"{v}\"""" for (k, v) in fields.items())

    if create_tag_query:
        query = query + create_tag_query
    return tx.run(query)


def delete_tagged_relationships(tx, email):
    query = f"""
    MATCH (user {{email: '{email}'}})-[rel:TAGGED]->(:Tag)
    DELETE rel
    """
    return tx.run(query)


def create_TAGGED_relationships(tx, email, tag_names, tag_labels):
    query = f"""
        WITH {tag_names} AS tag_names
        UNWIND tag_names AS tag_name
        MATCH (tag:{tag_labels} {{name: tag_name}})
        MATCH (user {{email: '{email}'}})
        CREATE (user)-[:TAGGED] -> (tag)
    """
    return tx.run(query)


def create_user(tx, fields):
    # TODO: update this function to use logic of above one.
    query = "CREATE (new_user: Person {" + ", ".join(
        f"""{k}: \"{v}\"""" for (k, v) in fields.items()) + "})"
    return tx.run(query)


""" Functions for Businesses """


def get_business_by_email(tx, business_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    query = f"""
    MATCH (user:Business {{email: '{business_email}'}})
    OPTIONAL MATCH (user)-->(tag:Tag)
    RETURN user, COLLECT(tag.name) AS tags"""
    return tx.run(query)


def delete_business_by_email(tx, business_email):
    query = f"""
    MATCH(n: Business {{email: '{business_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)


def set_business_fields(tx, business_email, fields):
    '''
        Function for setting a new email of a user which has a particular email saved in database.
        It returns a BoltStatementResult containing the record of the edited user.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_email = the new email to assign to that user.
    '''

    # NOTE: this could error when assigning string values that need quotations
    query = f"MATCH (user:Business {{email: '{business_email}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in fields.items())
    return tx.run(query)


def create_business(tx, fields):

    create_TAGGED_relationships_query = ""
    if 'tags' in fields:
        tags = fields['tags']
        fields.pop('tags')
        create_TAGGED_relationships_query = f"""
        WITH {tags} AS tag_names
        UNWIND tag_names AS tag_name
        MATCH(tag: Tag {{name: tag_name}})
        MATCH(user: Business {{email: '{fields['email']}'}})
        CREATE(user)-[:TAGGED] -> (tag)"""

    create_user_query = "CREATE (new_user: Business{" + ", ".join(
        f"{k}: '{v}'" for (k, v) in fields.items()) + "})"

    query = create_user_query + create_TAGGED_relationships_query
    print(query)
    return tx.run(query)


def get_space_by_email(tx, space_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    return tx.run(f"MATCH (user:Space {{email: '{space_email}'}}) RETURN user")


def delete_space_by_email(tx, space_email):
    return tx.run(f"MATCH (user:Space {{email: '{space_email}'}}) DELETE user")


def set_space_fields(tx, space_email, fields):
    '''
        Function for setting a new email of a user which has a particular email saved in database.
        It returns a BoltStatementResult containing the record of the edited user.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_email = the new email to assign to that user.
    '''
    # NOTE: this could error when assigning string values that need quotations
    query = f"MATCH (user:Space {{email: '{space_email}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in fields.items())
    return tx.run(query)


def create_space(tx, fields):
    query = "CREATE (user: Space {" + ", ".join(
        f"{k}: '{v}'" for (k, v) in fields.items()) + "})"
    return tx.run(query)


"""functions for POSTS"""


def get_post_by_uuid(tx, uuid):
    query = f"MATCH (post:Post {{uuid:'{uuid}'}}) RETURN post"
    return tx.run(query)


def create_post(tx, post_content, user_email, created, modified, uuid):
    query = f"""MATCH (user:Person {{email:'{user_email}'}})
                CREATE (post:Post {{uuid: '{uuid}', content: '{post_content}', created: datetime('{created}'), modified: datetime('{modified}')}})
                CREATE (user)-[:POSTED]->(post)
                RETURN post
            """
    return tx.run(query)

# TODO: this function can be more dynamic, no need for fixed paramters. See create user function for guide.


def set_post_fields(tx, uuid, content, hashtags):
    '''
        Function for setting a new email of a user which has a particular email saved in database.
        It returns a BoltStatementResult containing the record of the edited user.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_email = the new email to assign to that user.
    '''
    # NOTE: this could error when assigning string values that need quotations
    query = f"MATCH (post:Post {{uuid: '{uuid}'}}) SET post.content='{content}', post.hashtags='{hashtags}'"
    return tx.run(query)


def delete_post(tx, uuid):
    query = f"""MATCH (post:Post {{uuid: '{uuid}'}})
                DETACH DELETE post
             """
    return tx.run(query)


def get_list_of_user_post_dates(tx, user_email):
    query = f"""MATCH (user:Person {{email:'{user_email}'}})-[posted:POSTED]->()
                return collect(posted.date)
             """
    return tx.run(query)

# TODO: different function name

# TODO: delete ORDER BY


def get_posts_for_timeline(tx, user_email):
    query = f"""MATCH (user:Person {{email:'{user_email}'}})-[:FOLLOWS]->()-[posted:POSTED]->(post:Post)
                WITH posted, post
                ORDER BY posted.date
                return post
             """
    return tx.run(query)


def get_posts_of_followings_of_a_user(tx, email):
    query = f"""
        MATCH (:Person {{email: '{email}'}})
        -[:FOLLOWS]->(user:Person)
        -[:POSTED]->(post:Post)
        RETURN post.content AS content, post.modified AS modified, post.uuid AS uuid, post.created AS created, user.email as user_email"""
    return tx.run(query)


"""functions for FOLLOW RELATIONSHIPS"""


def create_request_relationship(tx, relationship_type, requester_email, request_recipient_email, created_at):
    query = f"""
        MATCH (requester),(request_recipient)
        WHERE requester.email = '{requester_email}' AND request_recipient.email = '{request_recipient_email}'
        CREATE (requester)-[f:{relationship_type}{{created_at: '{created_at}'}}]->(request_recipient)
    """
    return tx.run(query)


def approve_request(tx, request_relationship_type, approved_relationship_type, requester_email, request_recipient_email, created_at):
    # TODO: see if this query has the right approach. Why not just use DELETE and CREATE clauses?
    query = f"""
        MATCH (requester)-[req:{request_relationship_type}]->(request_recipient)
        WHERE requester.email = '{requester_email}' AND request_recipient.email = '{request_recipient_email}'
        CREATE (requester)-[:{approved_relationship_type}{{created_at: '{created_at}'}}]->(request_recipient)
        DELETE req
    """
    return tx.run(query)


def delete_request_relationship(tx, relationship_type, requester_email, request_recipient_email):
    query = f"""
        MATCH (requester {{email: '{requester_email}' }})-[f:{relationship_type}]->(request_recipient {{email: '{request_recipient_email}'}})
        DELETE f
    """
    return tx.run(query)


def get_followers_of_a_user(tx, email):
    query = f"""
        MATCH (follower)-[:FOLLOWS]->(:Person {{email: '{email}'}}) RETURN follower.full_name AS full_name, follower.email AS email
    """
    return tx.run(query)


def get_followings_of_a_user(tx, email):
    query = f"""
        MATCH (:Person {{email: '{email}'}})-[:FOLLOWS]->(follower) RETURN follower.full_name AS full_name, follower.email AS email
    """
    return tx.run(query)


def get_nodes_for_user_search(tx, search_string):
    query = f"""CALL db.index.fulltext.queryNodes('SearchUserIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""
    return tx.run(query)


def get_nodes_for_business_search(tx, search_string):
    query = f"""CALL db.index.fulltext.queryNodes('SearchBusinessIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""
    return tx.run(query)


def get_nodes_for_space_search(tx, search_string):
    query = f"""CALL db.index.fulltext.queryNodes('SearchSpaceIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""

    return tx.run(query)


def get_nodes_for_tag_search(tx, search_string):
    query = f"""CALL db.index.fulltext.queryNodes('SearchTagIndex', '"{search_string}"~0.2') YIELD node, score 
                RETURN node, score"""
    return tx.run(query)

# def get_users_with_tag(tx, tag):
#     query = f"""OPTIONAL MATCH (node:Person)-[:TAGGED]->(tag:Tag {{name:'{tag}'}})
#                 RETURN user LIMIT 10
#             """
#     return tx.run(query)


def get_accounts_with_tag(tx, tag, label):
    query = f"""OPTIONAL MATCH (node:{label})-[:TAGGED]->(tag:Tag {{name:'{tag}'}})
                RETURN node LIMIT 10
             """
    # query = f"""MATCH (node:{label})
    #             WHERE any(x IN node.tags WHERE x = '{tag}')
    #             RETURN node LIMIT 10
    #         """
    return tx.run(query)


def get_tags(tx, labels):
    labels = ' OR '.join(f'tag:{label}' for label in labels)
    query = f"""
        MATCH (tag)
        WHERE {labels}
        RETURN tag
    """
    return tx.run(query)


def get_chatrooms_of_user(tx, email):
    query = f"""
        MATCH (u:Person {{email: \'{email}\'}})-[:CHATS_IN]->(c:Chatroom)
        MATCH (r:Person)-[:CHATS_IN]->(c)
        WHERE r.email <> \'{email}\'
        RETURN c.chat_id AS chat_id, r.email AS recipient
    """
    return tx.run(query)


def check_users_in_chatroom(tx, email1, email2):
    query = f"""
        MATCH (u1:Person {{email: \'{email1}\'}})-[:CHATS_IN]->(c:Chatroom)
        MATCH (u2:Person {{email: \'{email2}\'}})-[:CHATS_IN]->(c)
        RETURN CASE WHEN u1 IS NOT NULL AND u2 IS NOT NULL THEN true ELSE false END AS result
    """
    return tx.run(query)


def create_chatroom(tx, email1, email2, chat_id):
    query = f"""
        MATCH (u1:Person {{email: \'{email1}\'}})
        MATCH (u2:Person {{email: \'{email2}\'}})
        CREATE (c:Chatroom {{chat_id: \'{chat_id}\'}})
        CREATE (u1)-[:CHATS_IN]->(c)
        CREATE (u2)-[:CHATS_IN]->(c)
    """
    return tx.run(query)


def check_chatroom_exists(tx, chat_id):
    query = f"""
        MATCH (c:Chatroom {{chat_id: \'{chat_id}\'}})
        RETURN CASE WHEN c IS NULL THEN false ELSE true END AS result
    """
    return tx.run(query)


def delete_chatroom(tx, chat_id):
    query = f"""
        MATCH (c:Chatroom {{chat_id: \'{chat_id}\'}})
        DETACH DELETE c
    """
    return tx.run(query)


""" functions for AFFILIATIONS """


def create_affiliation_relationship(tx, affiliation_requester, affiliation_request_recipient, created_at):
    query = f"""
        MATCH (affiliation_requester:Person),(affiliation_request_recipient:Business)
        WHERE affiliation_requester.email = '{affiliation_requester}' AND affiliation_request_recipient.email = '{affiliation_request_recipient}'
        CREATE (affiliation_requester)-[f:REQUESTED_AFFILIATION{{created_at: '{created_at}'}}]->(affiliation_request_recipient)
        RETURN f
    """
    return tx.run(query)


def delete_affiliation_relationship(tx, affiliation_requester, affiliation_request_recipient):
    query = f"""
        MATCH (affiliate {{email: '{affiliation_requester}'}})-[f:REQUESTED_AFFILIATION]->(affiliate_recipient {{email: '{affiliation_request_recipient}'}})
        DELETE f
    """
    return tx.run(query)


def get_notifications(tx, user_email):
    query = f"""
        MATCH (recipient:Person {{email: '{user_email}'}})<-[r]-(requester)
        WHERE type(r) = 'REQUESTED_FOLLOW' OR type(r) = 'REQUESTED_AFFILIATION'
        RETURN type(r) AS relationship_type,
               r.created_at as created_at,
               recipient.email AS recipient_email,
               requester.email AS requester_email
    """
    return tx.run(query)
