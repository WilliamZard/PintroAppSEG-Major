"""Cypher queries specific to User nodes."""
from neo4j import Transaction, BoltStatementResult


def get_user_by_email(tx: Transaction, user_email: str) -> BoltStatementResult:
    """Returns the associated data of a Person node, identified by its email, including any associated tags."""

    # NOTE: tag labels are hardcoded here. If they change in tags csv, must be changed here.
    query = f"""
    MATCH (user:Person {{email: '{user_email}'}})
    OPTIONAL MATCH (user)-->(skill_tag:Tag:CanHelpWithTag)
    OPTIONAL MATCH (user)-->(passion_tag:Tag:PassionsTag)
    RETURN user, COLLECT(DISTINCT skill_tag.name) AS help_others, COLLECT(DISTINCT passion_tag.name) AS passions"""
    return tx.run(query)


def delete_user_by_email(tx: Transaction, user_email: str) -> BoltStatementResult:
    """Deletes all data of a user from the database, including any associated posts."""
    query = f"""
    MATCH(n: Person {{email: '{user_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)


def get_posts_of_followings_of_a_user(tx: Transaction, email: str) -> BoltStatementResult:
    """Get all the posts of the users a user is following."""
    query = f"""
        MATCH (:Person {{email: '{email}'}})
        -[:FOLLOWS]->(user:Person)
        -[:POSTED]->(post:Post)
        RETURN DISTINCT {{content:post.content, modified:post.modified, created:post.created, uuid:post.uuid, user_email:user.email}} AS posts"""
    return tx.run(query)


def get_followers_of_a_user(tx: Transaction, email: str) -> BoltStatementResult:
    """Get all the posts of all the followers of a user."""
    query = f"""
        MATCH (follower)-[:FOLLOWS]->(:Person {{email: '{email}'}}) RETURN follower.full_name AS full_name, follower.email AS email, follower.profile_image AS profile_image
    """
    return tx.run(query)


def get_followings_of_a_user(tx: Transaction, email: str) -> BoltStatementResult:
    """Get name and email of all the users a user is following."""
    query = f"""
        MATCH (:Person {{email: '{email}'}})-[:FOLLOWS]->(follower) RETURN follower.full_name AS full_name, follower.email AS email, follower.profile_image AS profile_image
    """
    return tx.run(query)
