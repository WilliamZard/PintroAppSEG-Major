'''Script for taking a CSV of tags and uploading each tag as node into the given Neo4j database.'''
from neo4j import GraphDatabase
import sys
import os
import pandas as pd


def connect():
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


def generate_tags(csv_path):
    tags_df = pd.read_csv(csv_path)
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


def create_tag_node(tx, tag):
    tags_string = ':Tag'  # have all tag nodes have default label :Tags
    if tag['labels']:
        tags_string = tags_string + ':' + ':'.join(tag['labels'])
    query = f"""CREATE (new_tag{tags_string} {{Name: "{tag['Name']}"}})"""
    tx.run(query)


def main(csv_path):
    driver = connect()
    with driver.session() as session:
        for tag in generate_tags(csv_path):
            session.write_transaction(create_tag_node, tag)


if __name__ == '__main__':
    csv_path = sys.argv[1]
    main(csv_path)
