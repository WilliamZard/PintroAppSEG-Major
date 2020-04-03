

def get_business_by_email(tx, business_email):
    '''
        Function that gets all the data related to a user with a particular email.
        It returns a BoltStatementResult.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be retrieved.
    '''
    query = f"""
    MATCH (user:Business {{email: '{business_email}'}})
    OPTIONAL MATCH (user)-->(tag:Tag)
    RETURN user, COLLECT(tag.name) AS tags"""
    return tx.run(query)


def delete_business_by_email(tx, business_email):
    query = f"""
    MATCH(n: Business {{email: '{business_email}'}})
    OPTIONAL MATCH(n)--(p: Post)
    DETACH DELETE n, p"""
    return tx.run(query)


def set_business_fields(tx, business_email, fields):
    '''
        Function for setting a new email of a user which has a particular email saved in database.
        It returns a BoltStatementResult containing the record of the edited user.
    '''
    '''Args:
        tx = the context from where to run chipher statements and retreiving information from the db.
        user_email = the email of the user whose data needs to be edited.
        new_email = the new email to assign to that user.
    '''

    # NOTE: this could error when assigning string values that need quotations
    query = f"MATCH (user:Business {{email: '{business_email}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in fields.items())
    return tx.run(query)


def create_business(tx, fields):

    create_TAGGED_relationships_query = ""
    if 'tags' in fields:
        tags = fields['tags']
        fields.pop('tags')
        create_TAGGED_relationships_query = f"""
        WITH {tags} AS tag_names
        UNWIND tag_names AS tag_name
        MATCH(tag: Tag {{name: tag_name}})
        MATCH(user: Business {{email: '{fields['email']}'}})
        CREATE(user)-[:TAGGED] -> (tag)"""

    create_user_query = "CREATE (new_user: Business{" + ", ".join(
        f"{k}: '{v}'" for (k, v) in fields.items()) + "})"

    query = create_user_query + create_TAGGED_relationships_query
    return tx.run(query)
