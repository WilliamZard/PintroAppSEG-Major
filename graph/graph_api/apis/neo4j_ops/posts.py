from neo4j import Transaction, BoltStatementResult


def get_post_by_uuid(tx: Transaction, uuid: str) -> BoltStatementResult:
    query = f"MATCH (post:Post {{uuid:'{uuid}'}}) RETURN post"
    return tx.run(query)


def delete_post(tx: Transaction, uuid: str) -> BoltStatementResult:
    query = f"""MATCH (post:Post {{uuid: '{uuid}'}})
                DETACH DELETE post
             """
    return tx.run(query)


def get_list_of_user_post_dates(tx: Transaction, user_email: str) -> BoltStatementResult:
    query = f"""MATCH (user:Person {{email:'{user_email}'}})-[posted:POSTED]->()
                return collect(posted.date)
             """
    return tx.run(query)
