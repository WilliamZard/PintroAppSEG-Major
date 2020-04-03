def set_properties(tx, label, match_field, match_property, set_properties):
    query = f"MATCH (user:{label} {{{match_field}: '{match_property}'}}) SET " + \
        ", ".join(f"user.{k}='{v}'" for (k, v) in set_properties.items())
    return tx.run(query)
