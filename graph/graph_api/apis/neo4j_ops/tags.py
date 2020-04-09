from neo4j import Transaction, BoltStatementResult
from typing import List


def delete_tagged_relationships(tx: Transaction, email: str) -> BoltStatementResult:
    """Delete all tags that are associated with a user.

    """
    query = f"""
    MATCH (user {{email: '{email}'}})-[rel:TAGGED]->(:Tag)
    DELETE rel
    """
    return tx.run(query)


def create_TAGGED_relationships(tx: Transaction, email: str, tag_names: str, tag_labels: str) -> BoltStatementResult:
    """Create a relationship between a specific user and the given tags.

    """
    query = f"""
        WITH {tag_names} AS tag_names
        UNWIND tag_names AS tag_name
        MATCH (tag:{tag_labels} {{name: tag_name}})
        MATCH (user {{email: '{email}'}})
        CREATE (user)-[:TAGGED] -> (tag)
    """
    return tx.run(query)


def get_tags(tx: Transaction, labels: List[str]) -> BoltStatementResult:
    """Get a list of all the tags that match the given labels.

    """
    labels = ' OR '.join(f'tag:{label}' for label in labels)
    query = f"""
        MATCH (tag)
        WHERE {labels}
        RETURN tag
    """
    return tx.run(query)
