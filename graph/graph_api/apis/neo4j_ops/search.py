def get_nodes_for_user_search(tx, search_string):
    query = f"""CALL db.index.fulltext.queryNodes('SearchUserIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""
    return tx.run(query)


def get_nodes_for_business_search(tx, search_string):
    query = f"""CALL db.index.fulltext.queryNodes('SearchBusinessIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""
    return tx.run(query)


def get_nodes_for_space_search(tx, search_string):
    query = f"""CALL db.index.fulltext.queryNodes('SearchSpaceIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""

    return tx.run(query)


def get_nodes_for_tag_search(tx, search_string):
    query = f"""CALL db.index.fulltext.queryNodes('SearchTagIndex', '"{search_string}"~0.2') YIELD node, score 
                RETURN node, score"""
    return tx.run(query)

# def get_users_with_tag(tx, tag):
#     query = f"""OPTIONAL MATCH (node:Person)-[:TAGGED]->(tag:Tag {{name:'{tag}'}})
#                 RETURN user LIMIT 10
#             """
#     return tx.run(query)


def get_accounts_with_tag(tx, tag, label):
    query = f"""OPTIONAL MATCH (node:{label})-[:TAGGED]->(tag:Tag {{name:'{tag}'}})
                RETURN node LIMIT 10
             """
    # query = f"""MATCH (node:{label})
    #             WHERE any(x IN node.tags WHERE x = '{tag}')
    #             RETURN node LIMIT 10
    #         """
    return tx.run(query)
