from neo4j import Transaction, BoltStatementResult


def get_chatrooms_of_user(tx: Transaction, email: str) -> BoltStatementResult:
    query = f"""
        MATCH (u:Person {{email: \'{email}\'}})-[:CHATS_IN]->(c:Chatroom)
        MATCH (r:Person)-[:CHATS_IN]->(c)
        WHERE r.email <> \'{email}\'
        RETURN c.chat_id AS chat_id, r.email AS recipient
    """
    return tx.run(query)


def check_users_in_chatroom(tx: Transaction, email1: str, email2: str) -> BoltStatementResult:
    query = f"""
        MATCH (u1:Person {{email: \'{email1}\'}})-[:CHATS_IN]->(c:Chatroom)
        MATCH (u2:Person {{email: \'{email2}\'}})-[:CHATS_IN]->(c)
        RETURN CASE WHEN u1 IS NOT NULL AND u2 IS NOT NULL THEN true ELSE false END AS result
    """
    return tx.run(query)


def check_chatroom_exists(tx: Transaction, chat_id: str) -> BoltStatementResult:
    query = f"""
        MATCH (c:Chatroom {{chat_id: \'{chat_id}\'}})
        RETURN CASE WHEN c IS NULL THEN false ELSE true END AS result
    """
    return tx.run(query)


def delete_chatroom(tx: Transaction, chat_id: str) -> BoltStatementResult:
    query = f"""
        MATCH (c:Chatroom {{chat_id: \'{chat_id}\'}})
        DETACH DELETE c
    """
    return tx.run(query)
