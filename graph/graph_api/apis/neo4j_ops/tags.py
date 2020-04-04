
def delete_tagged_relationships(tx, email):
    query = f"""
    MATCH (user {{email: '{email}'}})-[rel:TAGGED]->(:Tag)
    DELETE rel
    """
    return tx.run(query)


def create_TAGGED_relationships(tx, email, tag_names, tag_labels):
    query = f"""
        WITH {tag_names} AS tag_names
        UNWIND tag_names AS tag_name
        MATCH (tag:{tag_labels} {{name: tag_name}})
        MATCH (user {{email: '{email}'}})
        CREATE (user)-[:TAGGED] -> (tag)
    """
    return tx.run(query)


def get_tags(tx, labels):
    labels = ' OR '.join(f'tag:{label}' for label in labels)
    query = f"""
        MATCH (tag)
        WHERE {labels}
        RETURN tag
    """
    return tx.run(query)
