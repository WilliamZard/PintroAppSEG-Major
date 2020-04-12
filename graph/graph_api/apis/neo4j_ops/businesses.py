from neo4j import Transaction, BoltStatementResult


def get_business_by_email(tx: Transaction, business_email: str) -> BoltStatementResult:
    """Gets all data associated with a business, identified by its email."""
    query = f"""
    MATCH (user:Business {{email: '{business_email}'}})
    OPTIONAL MATCH (user)-->(tag:Tag)
    OPTIONAL MATCH (person:Person)-[:AFFILIATED_WITH]-(user)
    RETURN user, COLLECT(DISTINCT tag.name) AS tags, COLLECT(DISTINCT person.email) AS team_members"""
    return tx.run(query)


def delete_business_by_email(tx: Transaction, business_email: str) -> BoltStatementResult:
    """Deletes all data associated with a business, including its posts."""
    query = f"""
    MATCH(n: Business {{email: '{business_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)
