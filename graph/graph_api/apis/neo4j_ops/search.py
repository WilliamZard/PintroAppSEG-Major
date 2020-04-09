from neo4j import Transaction, BoltStatementResult


def get_nodes_for_user_search(tx: Transaction, search_string: str) -> BoltStatementResult:
    """Search users by a given search string, sorting them by relevance and returning the top 10 results."""
    query = f"""CALL db.index.fulltext.queryNodes('SearchUserIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""
    return tx.run(query)


def get_nodes_for_business_search(tx: Transaction, search_string: str) -> BoltStatementResult:
    """Search businesses by a given search string, sorting them by relevance and returning the top 10 results."""
    query = f"""CALL db.index.fulltext.queryNodes('SearchBusinessIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""
    return tx.run(query)


def get_nodes_for_space_search(tx: Transaction, search_string: str) -> BoltStatementResult:
    """Search spaces by a given search string, sorting them by relevance and returning the top 10 results."""
    query = f"""CALL db.index.fulltext.queryNodes('SearchSpaceIndex', '"{search_string}"~0.2') YIELD node, score
                RETURN node, score LIMIT 10"""

    return tx.run(query)


def get_nodes_for_tag_search(tx: Transaction, search_string: str) -> BoltStatementResult:
    """Search tags by a given search string, sorting them by relevance and returning the top 10 results."""
    query = f"""CALL db.index.fulltext.queryNodes('SearchTagIndex', '"{search_string}"~0.2') YIELD node, score 
                RETURN node, score"""
    return tx.run(query)


def get_accounts_with_tag(tx: Transaction, tag: str, label: str) -> BoltStatementResult:
    """Get a list of any nodes that are associated with a given tag, returning up to 10 nodes."""
    query = f"""OPTIONAL MATCH (node:{label})-[:TAGGED]->(tag:Tag {{name:'{tag}'}})
                RETURN node LIMIT 10
             """
    return tx.run(query)
