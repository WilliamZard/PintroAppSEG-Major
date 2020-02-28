# TODO: pandas should not needed in production and is a heavy library. Find a way to only use it in testing.
import datetime
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
# POSTED_PROPERTIES= ["date"]
POST_PROPERTIES = ["content"]
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

USER_WITH_MULTIPLE_POSTS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'UCL', 'John', 'male', '111',
                                                         'I was a student', 'London', 'unemployed', 'Jonny', 'user_with_posts@gmail.com', 'eat, sleep, repeat.']))                                                        
# The first 2 posts will be assigned to USER_WITH_MULTIPLE_POSTS
USER_POST_A = dict(zip(POST_PROPERTIES, ['post2']))
USER_POST_B = dict(zip(POST_PROPERTIES, ['post1']))
USER_POST_C = dict(zip(POST_PROPERTIES, ['post3']))# Third post is for posting tests

POST_UPDATE_A = {'new_content': 'Hey I have just update my post content. This is POST_UPDATE_A'}
POST_UPDATE_B = {'new_content': 'Hey I have just update my post content. This is POST_UPDATE_B'}

USER_WITH_THREE_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'Duke Wellington', 'male', '911',
                                         'not godless', 'strand', 'Duke', 'Duke', 'yes_ucl@kcl.ac.uk', 'What is GKT?']))
USER_WITH_TWO_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Bachelor\'s', 'Leonardo Di Caprio', 'male', '000',
                                         'I am the MVP', 'US', 'Actor', 'Lello', 'lello@gmail.com', 'I won an Oscar']))
USER_WITH_ONE_FOLLOWING = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Secondary school', 'John Jonny', 'male', '111',
                                         'I am millionaire', 'London', 'Entrepreneur', 'Sweet guy', 'jj@gmail.com', 'I started as a taxi driver.']))
USER_WITH_NO_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Diploma', 'John Kennedy', 'male', '121',
                                         'The only one pres', 'Unknown', 'Retired', 'JFK', 'jfk@gmail.com', 'They thought they killed me.']))  

USER_WITH_THREE_FOLLOWINGS_POST_A = dict(zip(POST_PROPERTIES, ['USER_WITH_THREE_FOLLOWINGS first post']))
USER_WITH_THREE_FOLLOWINGS_POST_B = dict(zip(POST_PROPERTIES, ['USER_WITH_THREE_FOLLOWINGS second post']))

USER_WITH_TWO_FOLLOWINGS_POST_A = dict(zip(POST_PROPERTIES, ['USER_WITH_TWO_FOLLOWINGS first post']))                                      
USER_WITH_TWO_FOLLOWINGS_POST_B = dict(zip(POST_PROPERTIES, ['USER_WITH_TWO_FOLLOWINGS second post']))
USER_WITH_TWO_FOLLOWINGS_POST_C = dict(zip(POST_PROPERTIES, ['USER_WITH_TWO_FOLLOWINGS third post']))

USER_WITH_ONE_FOLLOWING_POST_A = dict(zip(POST_PROPERTIES, ['USER_WITH_ONE_FOLLOWING first post']))

USER_WITH_NO_FOLLOWINGS_POST_A = dict(zip(POST_PROPERTIES, ['USER_WITH_NO_FOLLOWINGS first post']))
USER_WITH_NO_FOLLOWINGS_POST_B = dict(zip(POST_PROPERTIES, ['USER_WITH_NO_FOLLOWINGS second post']))

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
    if rewrite_test_data or not os.path.isfile(GIULIO_IMPORT_DIR + test_data_file):
        print('writing test data')
        # NOTE: very bad practise importing test functionality into a production file.
        # TODO: refactor this.
        generate_test_data_csv()
    driver = connect()
    with driver.session() as session:
        session.write_transaction(create_unique_email_constraint)
        session.write_transaction(create_user_email_existence_constraint)
        session.write_transaction(create_post_content_existence_constraint)
        session.write_transaction(create_test_data, test_data_file)
        session.write_transaction(create_posts_to_people_in_test_db)
        session.write_transaction(create_follows_relationships_to_people_in_test_db)
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
        VALID_USER_TO_BE_UPDATED,
        VALID_USER_TO_BE_DELETED,
        USER_WITH_MULTIPLE_POSTS,
        USER_WITH_THREE_FOLLOWINGS,
        USER_WITH_TWO_FOLLOWINGS,
        USER_WITH_ONE_FOLLOWING,
        USER_WITH_NO_FOLLOWINGS  
    ]
    test_df = pd.DataFrame(data, columns=USERS_PROPERTIES)
    print(test_df)

    # TODO: populating db currently requires data CSV to bin a specific Neo4j related location
    # This is bad as it descreases portability between different machines
    # Fix this
    test_df.to_csv('test_data.csv', index=False)


def create_test_data(tx, test_data):
    print("creating")
    # TODO: when database gets more complex, will need to start populating constraints as well
    # https://neo4j.com/docs/getting-started/current/cypher-intro/load-csv/
    query = f'LOAD CSV WITH HEADERS FROM "file:///{test_data}" AS csvLine' + \
        f""" CREATE (u:Person {{
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
            }})
            """
    return tx.run(query)

def create_posts_to_people_in_test_db(tx):
    query = f"""MATCH (user_a:Person {{email:'{USER_WITH_THREE_FOLLOWINGS['email']}'}})
                MATCH (user_b:Person {{email:'{USER_WITH_TWO_FOLLOWINGS['email']}'}})
                MATCH (user_c:Person {{email:'{USER_WITH_ONE_FOLLOWING['email']}'}})
                MATCH (user_d:Person {{email:'{USER_WITH_NO_FOLLOWINGS['email']}'}})
                MATCH (user_e:Person {{email:'{USER_WITH_MULTIPLE_POSTS['email']}'}})
                
                CREATE (post_a:Post {{content:'{USER_WITH_THREE_FOLLOWINGS_POST_A['content']}'}})
                CREATE (post_b:Post {{content:'{USER_WITH_THREE_FOLLOWINGS_POST_B['content']}'}})
                CREATE (user_a)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,1)}'}}]->(post_a)
                CREATE (user_a)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,2)}'}}]->(post_b)

                CREATE (post_c:Post {{content:'{USER_WITH_TWO_FOLLOWINGS_POST_A['content']}'}})
                CREATE (post_d:Post {{content:'{USER_WITH_TWO_FOLLOWINGS_POST_B['content']}'}})
                CREATE (post_e:Post {{content:'{USER_WITH_TWO_FOLLOWINGS_POST_C['content']}'}})
                CREATE (user_b)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,3)}'}}]->(post_c)
                CREATE (user_b)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,4)}'}}]->(post_d)
                CREATE (user_b)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,5)}'}}]->(post_e)

                CREATE (post_f:Post {{content:'{USER_WITH_ONE_FOLLOWING_POST_A['content']}'}})
                CREATE (user_c)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,6)}'}}]->(post_f)

                CREATE (post_g:Post {{content:'{USER_WITH_NO_FOLLOWINGS_POST_A['content']}'}})
                CREATE (post_h:Post {{content:'{USER_WITH_NO_FOLLOWINGS_POST_B['content']}'}})
                CREATE (user_d)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,7)}'}}]->(post_g)
                CREATE (user_d)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,8)}'}}]->(post_h)

                CREATE (post_j:Post {{content:'{USER_POST_A['content']}'}})
                CREATE (post_k:Post {{content:'{USER_POST_B['content']}'}})
                CREATE (user_e)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,9)}'}}]->(post_j)
                CREATE (user_e)-[:POSTED {{date:'{datetime.datetime.now() + datetime.timedelta(0,10)}'}}]->(post_k)            
             """
    return tx.run(query)

def create_follows_relationships_to_people_in_test_db(tx):
    query = f"""MATCH (user_a:Person {{email:'{USER_WITH_THREE_FOLLOWINGS['email']}'}})
                MATCH (user_b:Person {{email:'{USER_WITH_TWO_FOLLOWINGS['email']}'}})
                MATCH (user_c:Person {{email:'{USER_WITH_ONE_FOLLOWING['email']}'}})
                MATCH (user_d:Person {{email:'{USER_WITH_NO_FOLLOWINGS['email']}'}})

                CREATE (user_a)-[:FOLLOWS]->(user_b)
                CREATE (user_a)-[:FOLLOWS]->(user_c)
                CREATE (user_a)-[:FOLLOWS]->(user_d)

                CREATE (user_b)-[:FOLLOWS]->(user_c)
                CREATE (user_b)-[:FOLLOWS]->(user_d)

                CREATE (user_c)-[:FOLLOWS]->(user_d)
             """
    return tx.run(query)


# TODO REFACTOR THESE FUNCTIONS TO HAVE AN ONLY ONE FUNCTION FOR ADDING ALL CONSTRAINTS TO DB.
def create_unique_email_constraint(tx):
    query = "CREATE CONSTRAINT ON(user: Person) ASSERT user.email IS UNIQUE"
    return tx.run(query)

def create_user_email_existence_constraint(tx):
    query = "CREATE CONSTRAINT ON(user: Person) ASSERT EXISTS (user.email)"
    return tx.run(query)

def create_post_content_existence_constraint(tx):
    query = "CREATE CONSTRAINT ON(post: Post) ASSERT EXISTS (post.content)"
    return tx.run(query)

def delete_all_nodes(tx):
    print("Deleting")
    query = "MATCH(n) DETACH DELETE n"
    return tx.run(query)
