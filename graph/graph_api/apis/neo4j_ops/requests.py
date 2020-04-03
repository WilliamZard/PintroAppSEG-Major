
def create_request_relationship(tx, relationship_type, requester_email, request_recipient_email, created_at):
    query = f"""
        MATCH (requester),(request_recipient)
        WHERE requester.email = '{requester_email}' AND request_recipient.email = '{request_recipient_email}'
        CREATE (requester)-[f:{relationship_type}{{created_at: '{created_at}'}}]->(request_recipient)
    """
    return tx.run(query)


def approve_request(tx, request_relationship_type, approved_relationship_type, requester_email, request_recipient_email, created_at):
    # TODO: see if this query has the right approach. Why not just use DELETE and CREATE clauses?
    query = f"""
        MATCH (requester)-[req:{request_relationship_type}]->(request_recipient)
        WHERE requester.email = '{requester_email}' AND request_recipient.email = '{request_recipient_email}'
        CREATE (requester)-[:{approved_relationship_type}{{created_at: '{created_at}'}}]->(request_recipient)
        DELETE req
    """
    return tx.run(query)


def delete_request_relationship(tx, relationship_type, requester_email, request_recipient_email):
    query = f"""
        MATCH (requester {{email: '{requester_email}' }})-[f:{relationship_type}]->(request_recipient {{email: '{request_recipient_email}'}})
        DELETE f
    """
    return tx.run(query)


def create_affiliation_relationship(tx, affiliation_requester, affiliation_request_recipient, created_at):
    query = f"""
        MATCH (affiliation_requester:Person),(affiliation_request_recipient:Business)
        WHERE affiliation_requester.email = '{affiliation_requester}' AND affiliation_request_recipient.email = '{affiliation_request_recipient}'
        CREATE (affiliation_requester)-[f:REQUESTED_AFFILIATION{{created_at: '{created_at}'}}]->(affiliation_request_recipient)
        RETURN f
    """
    return tx.run(query)


def delete_affiliation_relationship(tx, affiliation_requester, affiliation_request_recipient):
    query = f"""
        MATCH (affiliate {{email: '{affiliation_requester}'}})-[f:REQUESTED_AFFILIATION]->(affiliate_recipient {{email: '{affiliation_request_recipient}'}})
        DELETE f
    """
    return tx.run(query)
