from neo4j import Transaction, BoltStatementResult


def get_business_by_email(tx: Transaction, business_email: str) -> BoltStatementResult:

    query = f"""
    MATCH (user:Business {{email: '{business_email}'}})
    OPTIONAL MATCH (user)-->(tag:Tag)
    RETURN user, COLLECT(tag.name) AS tags"""
    return tx.run(query)


def delete_business_by_email(tx: Transaction, business_email: str) -> BoltStatementResult:
    query = f"""
    MATCH(n: Business {{email: '{business_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)
