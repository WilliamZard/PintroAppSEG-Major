from neo4j import Transaction, BoltStatementResult


def get_post_by_uuid(tx: Transaction, uuid: str) -> BoltStatementResult:
    """Get a Post node from the database, identified by its UUID."""
    query = f"MATCH (post:Post {{uuid:'{uuid}'}}) RETURN post"
    return tx.run(query)


def delete_post(tx: Transaction, uuid: str) -> BoltStatementResult:
    """Delete a Post node from the database, identified by its UUID."""
    query = f"""MATCH (post:Post {{uuid: '{uuid}'}})
                DETACH DELETE post
             """
    return tx.run(query)


def get_list_of_user_post_dates(tx: Transaction, user_email: str) -> BoltStatementResult:
    """Get a list of all the dates of the posts a user has created."""
    query = f"""MATCH (user:Person {{email:'{user_email}'}})-[posted:POSTED]->()
                return collect(posted.date)
             """
    return tx.run(query)
