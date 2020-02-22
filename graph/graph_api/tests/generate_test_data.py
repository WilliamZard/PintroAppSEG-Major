# TODO: pandas should not needed in production and is a heavy library. Find a way to only use it in testing.

import pandas as pd
import os
from neo4j import GraphDatabase

SEB_NEO4J_IMPORT_DIR = '/Users/Seb/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-06fda328-94b7-4295-8d15-6dd8a4d56b97/installation-3.5.14/import/'


def connect():
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


def populate_db(rewrite_test_data=False):
    print("populating")
    test_data_file = 'test_data.csv'
    if rewrite_test_data or not os.path.isfile(SEB_NEO4J_IMPORT_DIR + test_data_file):
        print('writing test data')
        # NOTE: very bad practise importing test functionality into a production file.
        # TODO: refactor this.
        generate_test_data_csv()
    driver = connect()
    with driver.session() as session:
        print("about to write")
        print(session.sync())
        response = session.write_transaction(create_test_data, test_data_file)
        print(response)
    # TODO: do this properly. Move all db stuff connect() function. Use yield.
    driver.close()
    print('Database populated')


def generate_test_data_csv():
    print("generating")
    USERS_PROPERTIES = [
        "password",
        "profile_image",
        "education",
        "full_name",
        "gender",
        "phone",
        "short_bio",
        "location",
        "job_title",
        "preferred_name",
        "email",
        "story"]
    VALID_USER = ['password', 'image', 'High School', 'Duke Wellington', 'male', '911',
                  'not godless', 'strand', 'Duke', 'Duke', 'not_ucl@kcl.ac.uk', 'What is GKT?']
    data = [
        VALID_USER
    ]
    test_df = pd.DataFrame(data, columns=USERS_PROPERTIES)
    print(test_df)

    # TODO: populating db currently requires data CSV to bin a specific Neo4j related location
    # This is bad as it descreases portability between different machines
    # Fix this
    test_df.to_csv(SEB_NEO4J_IMPORT_DIR + 'test_data.csv', index=False)


def create_test_data(tx, test_data):
    print("creating")
    # TODO: when database gets more complex, will need to start populating constraints as well
    # https://neo4j.com/docs/getting-started/current/cypher-intro/load-csv/
    query = f'LOAD CSV WITH HEADERS FROM "file:///{test_data}" AS csvLine' + \
        """ CREATE (u:User {
            password: csvLine.password,
            profile_image: csvLine.profile_image,
            education: csvLine.education,
            full_name: csvLine.full_name,
            gender: csvLine.gender,
            phone: csvLine.phone,
            short_bio: csvLine.short_bio,
            location: csvLine.location,
            job_title: csvLine.job_title,
            preferred_name: csvLine.preferred_name,
            email: csvLine.email,
            story: csvLine.story
            })"""
    return tx.run(query)
