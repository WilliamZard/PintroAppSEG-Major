'''Script for taking a CSV of tags and uploading each tag as a node into the given Neo4j database.'''
import sys
import time

from neo4j import GraphDatabase

import pandas as pd


def connect(uri, password):
    """Create a new connection object to the NEO4J database."""
    db_user = 'neo4j'
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


def generate_tags(csv_path):
    """For each tag in the given CSV, format and yield it."""
    tags_df = pd.read_csv(csv_path)

    # NOTE: these labels are currently hardcoded.
    # Any changes to tags csv structure will need to be reflected here.
    neo4j_labels = [
        'PassionsTag', 'BusinessTag', 'CanHelpWithTag',
        'HelpMeWithTag', 'IntroMeToTag', 'JobTitleTag'
    ]
    neo4j_labels = dict(zip(tags_df.columns[1:], neo4j_labels))
    tags_df.rename(columns=neo4j_labels, inplace=True)
    for index, row in tags_df.iterrows():
        tag = {}
        tag['Name'] = row['TAGS']
        tag['labels'] = [
            label for label in row.index[1:] if pd.notna(row[label])
        ]
        yield tag


def get_time():
    """Generate the current time."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


def convert_to_cypher_datetime(datetime):
    """Convert Python datetime object to Neo4j compatible datetime object."""
    # Assumes there is a single space separating date and time sections
    # Assumes is in UTC time and is timezone naive
    return datetime.replace(' ', 'T') + 'Z'


def create_tag_node(tx, tag):
    """Run Cypher query to create a tag node."""
    tags_string = ':Tag'  # have all tag nodes have default label :Tags
    created = convert_to_cypher_datetime(get_time())
    if tag['labels']:
        tags_string = tags_string + ':' + ':'.join(tag['labels'])
    query = f"""CREATE (new_tag{tags_string} {{name: "{tag['Name']}", created: datetime("{created}")}})"""
    tx.run(query)


def delete_all_tags(tx):
    query = """MATCH(n:Tag) DETACH DELETE n"""
    return tx.run(query)


def main(csv_path, bolt_uri, password):
    """Main function for orchestrating tag deployments."""
    driver = connect(bolt_uri, password)
    with driver.session() as session:
        session.write_transaction(delete_all_tags)
        for tag in generate_tags(csv_path):
            session.write_transaction(create_tag_node, tag)
    driver.close()


if __name__ == '__main__':
    csv_path = sys.argv[1]
    bolt_uri = sys.argv[2]
    password = sys.argv[3]
    main(csv_path, bolt_uri, password)
