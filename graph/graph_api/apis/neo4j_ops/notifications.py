from neo4j import Transaction, BoltStatementResult


def get_notifications(tx: Transaction, user_email: str) -> BoltStatementResult:
    query = f"""
        MATCH (recipient:Person {{email: '{user_email}'}})<-[r]-(requester)
        WHERE type(r) = 'REQUESTED_FOLLOW' OR type(r) = 'REQUESTED_AFFILIATION'
        RETURN type(r) AS relationship_type,
               r.created_at as created_at,
               recipient.email AS recipient_email,
               requester.email AS requester_email
    """
    return tx.run(query)
