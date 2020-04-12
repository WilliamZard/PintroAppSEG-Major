from neo4j import Transaction, BoltStatementResult


def get_chatrooms_of_account(tx: Transaction, email: str) -> BoltStatementResult:
    """Get all the chatrooms of a given user, returning the email of the recipient and the UUID of the chatroom itself."""
    query = f"""
        MATCH (u {{email: \'{email}\'}})-[:CHATS_IN]->(c:Chatroom)
        MATCH (r)-[:CHATS_IN]->(c)
        WHERE r.email <> \'{email}\'
        RETURN c.chat_id AS chat_id, r.email AS recipient, labels(r) as type
    """
    return tx.run(query)


def check_users_in_chatroom(tx: Transaction, email1: str, email2: str) -> BoltStatementResult:
    """Check that two users are currently in an existing chatroom with each other."""
    query = f"""
        MATCH (u1 {{email: \'{email1}\'}})-[:CHATS_IN]->(c:Chatroom)
        MATCH (u2 {{email: \'{email2}\'}})-[:CHATS_IN]->(c)
        RETURN CASE WHEN u1 IS NOT NULL AND u2 IS NOT NULL THEN true ELSE false END AS result
    """
    return tx.run(query)


def check_chatroom_exists(tx: Transaction, chat_id: str) -> BoltStatementResult:
    """Check that a chatroom with the given UUID already exists in the database."""
    query = f"""
        MATCH (c:Chatroom {{chat_id: \'{chat_id}\'}})
        RETURN CASE WHEN c IS NULL THEN false ELSE true END AS result
    """
    return tx.run(query)


def delete_chatroom(tx: Transaction, chat_id: str) -> BoltStatementResult:
    """Delete a chatroom from the database, identified by its UUID."""
    query = f"""
        MATCH (c:Chatroom {{chat_id: \'{chat_id}\'}})
        DETACH DELETE c
    """
    return tx.run(query)
