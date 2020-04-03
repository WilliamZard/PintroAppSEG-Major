
def get_post_by_uuid(tx, uuid):
    query = f"MATCH (post:Post {{uuid:'{uuid}'}}) RETURN post"
    return tx.run(query)


def create_post(tx, post_content, user_email, created, modified, uuid):
    query = f"""MATCH (user:Person {{email:'{user_email}'}})
                CREATE (post:Post {{uuid: '{uuid}', content: '{post_content}', created: datetime('{created}'), modified: datetime('{modified}')}})
                CREATE (user)-[:POSTED]->(post)
                RETURN post
            """
    return tx.run(query)

# TODO: this function can be more dynamic, no need for fixed paramters. See create user function for guide.


def delete_post(tx, uuid):
    query = f"""MATCH (post:Post {{uuid: '{uuid}'}})
                DETACH DELETE post
             """
    return tx.run(query)


def get_list_of_user_post_dates(tx, user_email):
    query = f"""MATCH (user:Person {{email:'{user_email}'}})-[posted:POSTED]->()
                return collect(posted.date)
             """
    return tx.run(query)

# TODO: different function name

# TODO: delete ORDER BY
