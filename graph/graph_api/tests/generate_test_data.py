# TODO: pandas should not needed in production and is a heavy library. Find a way to only use it in testing.

import pandas as pd
import os
from neo4j import GraphDatabase
# TODO: format! line length is way too long
SEB_NEO4J_IMPORT_DIR = '/Users/Seb/Library/Application Support/Neo4j Desktop/Application/neo4jDatabases/database-06fda328-94b7-4295-8d15-6dd8a4d56b97/installation-3.5.14/import/'

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
VALID_USER = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'Duke Wellington', 'male', '911',
                                         'not godless', 'strand', 'Duke', 'Duke', 'not_ucl@kcl.ac.uk', 'What is GKT?']))
VALID_USER_TO_BE_UPDATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Home', 'D Trump', 'male?', '000',
                                                       'genius', 'whit house', 'Commander n sth', 'Mr Pres', 'genius@fakenews.cnn', 'Covfefe']))
VALID_USER_TO_BE_UPDATED_NEW_FIELDS = dict(zip(USERS_PROPERTIES, ['0000', 'new_image', 'Care Home', 'Donald Trump', 'masculine', '999',
                                                                  'retired genius', 'Mar O Lago', 'Former Best President', 'GOAT', 'genius@fakenews.cnn', 'revolutionary']))
VALID_USER_TO_BE_DELETED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'Taaj', 'man', '123',
                                                       'going places', 'Gatwick init', 'going places', 'just Taaj', 'taaj@hotmail.co.uk', 'you get me?']))
VALID_USER_TO_BE_CREATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'precious', 'man', '111',
                                                       'best kiosk in town', 'Gatwickk', 'Precious', 'Precious', 'precious@gmail.com', 'Likeable and devout.']))

INVALID_USER_TO_BE_CREATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'precious', 'man', '111',
                                                         'best kiosk in town', 'Gatwickk', 'Precious', 'Precious', 'preciousgmail.com', 'Likeable and devout.']))
NONEXISTANT_USER_EMAIL = 'does@exist.not'
INVALID_EMAIL = 'invalidateme.now'


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
        response = session.write_transaction(create_test_data, test_data_file)
        print(response)
    # TODO: do this properly. Move all db stuff connect() function. Use yield.
    driver.close()
    print('Database populated')


def clear_db():
    driver = connect()
    with driver.session() as session:
        print("about to delete")
        response = session.write_transaction(delete_all_nodes)


def generate_test_data_csv():
    print("generating")
    data = [
        VALID_USER,
        VALID_USER_TO_BE_DELETED
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
        """ CREATE (u:Person {
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


def delete_all_nodes(tx):
    print("Deleting")
    query = "MATCH(n) DETACH DELETE n"
    return tx.run(query)
