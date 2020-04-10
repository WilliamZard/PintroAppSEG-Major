from neo4j import Transaction, BoltStatementResult


def get_space_by_email(tx: Transaction, space_email: str) -> BoltStatementResult:
    """Get a Space node from the database, identified by its email."""
    return tx.run(f"MATCH (user:Space {{email: '{space_email}'}}) RETURN user")


def delete_space_by_email(tx: Transaction, space_email: str) -> BoltStatementResult:
    """Delete a Space node from the database, identified by its email."""
    return tx.run(f"MATCH (user:Space {{email: '{space_email}'}}) DELETE user")
