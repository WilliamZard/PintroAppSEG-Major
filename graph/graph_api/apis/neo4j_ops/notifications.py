

def get_notifications(tx, user_email):
    query = f"""
        MATCH (recipient:Person {{email: '{user_email}'}})<-[r]-(requester)
        WHERE type(r) = 'REQUESTED_FOLLOW' OR type(r) = 'REQUESTED_AFFILIATION'
        RETURN type(r) AS relationship_type,
               r.created_at as created_at,
               recipient.email AS recipient_email,
               requester.email AS requester_email
    """
    return tx.run(query)
