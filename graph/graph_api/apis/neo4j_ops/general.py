def set_properties(tx, label, match_field, match_property, set_properties):
    query = f"MATCH (user:{label} {{{match_field}: '{match_property}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in set_properties.items())
    return tx.run(query)


def create_node(tx, label, properties):
    query = f"CREATE (new_node:{label}" + "{" + ", ".join(
        f"""{k}: \"{v}\"""" for (k, v) in properties.items()) + "})"
    return tx.run(query)


def create_relationship(tx,
                        s_node_labels, s_node_properties,
                        e_node_labels, e_node_properties,
                        relationship_type, relationship_properties=None):
    # TODO: the input dictionaries to this function could be constructed differently. No need to specify labels. Just
    # properties to match by, and relationship type. Labels already in node objects.
    s_node_properties = _make_properties_string(s_node_properties)
    e_node_properties = _make_properties_string(e_node_properties)
    if relationship_properties is None:
        relationship_properties = ""
    else:
        relationship_properties = _make_properties_string(
            relationship_properties)
    query = f"""
    MATCH (starting_node:{s_node_labels} {s_node_properties})
    MATCH (ending_node:{e_node_labels} {e_node_properties})
    CREATE (starting_node)-[:{relationship_type}{relationship_properties}]->(ending_node)
    """
    return tx.run(query)


def _make_properties_string(properties):
    return ", ".join(
        f"""{{{k}: "{v}"}}""" for k, v in properties.items())
