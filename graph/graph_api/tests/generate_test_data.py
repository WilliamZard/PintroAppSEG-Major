# TODO: pandas should not needed in production and is a heavy library. Find a way to only use it in testing.
import datetime
import os
from neo4j import GraphDatabase
from .test_data.users import *
from .test_data.posts import *
from .test_data.tags import *
# TODO: organise test data. Different script?

USERS_TO_TEST = [
    VALID_USER,
    VALID_USER_TO_BE_UPDATED,
    VALID_USER_TO_BE_DELETED,
    USER_WITH_MULTIPLE_POSTS,
    USER_WITH_THREE_FOLLOWINGS,
    USER_WITH_TWO_FOLLOWINGS,
    USER_WITH_ONE_FOLLOWING,
    USER_WITH_NO_FOLLOWINGS,
    USER_ABOUT_TO_FOLLOW,
    USER_ABOUT_TO_BE_FOLLOWED,
    USER_FOLLOWING,
    USER_BEING_FOLLOWED,
    USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS,
    USER_THAT_POSTED_POST_A,
    USER_THAT_POSTED_POST_B
]


def connect():
    uri = os.getenv('NEO4J_URI')
    db_user = 'neo4j'
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(db_user, password))
    return driver


def populate_db(rewrite_test_data=False):
    driver = connect()
    with driver.session() as session:
        for query in queries:
            session.write_transaction(_run_query, query)
    # TODO: do this properly. Move all db stuff connect() function. Use yield.
    driver.close()


def clear_db():
    driver = connect()
    with driver.session() as session:
        print("about to delete")
        session.write_transaction(_run_query, DELETE_ALL_NODES)


def _run_query(tx, query):
    return tx.run(query)


# TODO: restructure this
CREATE_TEST_DATA = ""
for USER in USERS_TO_TEST:
    CREATE_TEST_DATA += "CREATE (" + USER['preferred_name'] + ":Person { "
    CREATE_TEST_DATA += "password: \'" + USER['password'] + "\' , "
    CREATE_TEST_DATA += "profile_image: \'" + USER['profile_image'] + "\' , "
    CREATE_TEST_DATA += "education: \'" + USER['education'] + "\' , "
    CREATE_TEST_DATA += "full_name: \'" + USER['full_name'] + "\' , "
    CREATE_TEST_DATA += "gender: \'" + USER['gender'] + "\' , "
    CREATE_TEST_DATA += "phone: \'" + USER['phone'] + "\' , "
    CREATE_TEST_DATA += "short_bio: \'" + USER['short_bio'] + "\' , "
    CREATE_TEST_DATA += "location: \'" + USER['location'] + "\' , "
    CREATE_TEST_DATA += "job_title: \'" + USER['job_title'] + "\' , "
    CREATE_TEST_DATA += "preferred_name: \'" + USER['preferred_name'] + "\' , "
    CREATE_TEST_DATA += "email: \'" + USER['email'] + "\' , "
    CREATE_TEST_DATA += "story: \'" + USER['story'] + "\'}) \n"

CREATE_POSTS = f"""
    MATCH (user_a:Person {{email:'{USER_WITH_MULTIPLE_POSTS['email']}'}})
    MATCH (user_b:Person {{email:'{USER_THAT_POSTED_POST_A['email']}'}})
    MATCH (user_c:Person {{email:'{USER_THAT_POSTED_POST_B['email']}'}})

    CREATE (post_a:Post {{uuid: '{EXISTING_POST['uuid']}',
        content:'{EXISTING_POST['content']}',
        created: datetime('{EXISTING_POST['created']}'),
        modified: datetime('{EXISTING_POST['modified']}')
        }})
    CREATE (post_b:Post {{uuid: '{POST_TO_BE_UPDATED_THAT_EXISTS['uuid']}',
        content:'{POST_TO_BE_UPDATED_THAT_EXISTS['content']}',
        created: datetime('{POST_TO_BE_UPDATED_THAT_EXISTS['created']}'),
        modified: datetime('{POST_TO_BE_UPDATED_THAT_EXISTS['modified']}')
        }})

    CREATE (post_c:Post {{uuid: '{POST_TO_BE_DELETED_THAT_EXISTS['uuid']}',
        content:'{POST_TO_BE_DELETED_THAT_EXISTS['content']}',
        created: datetime('{POST_TO_BE_DELETED_THAT_EXISTS['created']}'),
        modified: datetime('{POST_TO_BE_DELETED_THAT_EXISTS['modified']}')
        }})

    CREATE (post_d:Post {{uuid: '{USER_POST_A['uuid']}',
        content:'{USER_POST_A['content']}',
        created: datetime('{USER_POST_A['created']}'),
        modified: datetime('{USER_POST_A['modified']}')
        }})
    
    CREATE (post_e:Post {{uuid: '{USER_POST_B['uuid']}',
        content:'{USER_POST_B['content']}',
        created: datetime('{USER_POST_B['created']}'),
        modified: datetime('{USER_POST_B['modified']}')
        }})
    
    CREATE (user_a)-[:POSTED]->(post_a)
    CREATE (user_a)-[:POSTED]->(post_b)
    CREATE (user_a)-[:POSTED]->(post_c)

    CREATE (user_b)-[:POSTED]->(post_d)
    CREATE (user_c)-[:POSTED]->(post_e)
"""

CREATE_FOLLOWS_FOR_POSTS_USERS = f"""
    MATCH (user_a:Person {{email:'{USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS['email']}'}})
    MATCH (user_b:Person {{email:'{USER_THAT_POSTED_POST_A['email']}'}})
    MATCH (user_c:Person {{email:'{USER_THAT_POSTED_POST_B['email']}'}})
    CREATE (user_a)-[:FOLLOWS]->(user_b)
    CREATE (user_a)-[:FOLLOWS]->(user_c)
"""

"""
# TODO: decompose this string
CREATE_POSTS = fMATCH(user_a: Person {{email: '{USER_WITH_THREE_FOLLOWINGS['email']}'}})
                MATCH(user_b: Person {{email: '{USER_WITH_TWO_FOLLOWINGS['email']}'}})
                MATCH(user_c: Person {{email: '{USER_WITH_ONE_FOLLOWING['email']}'}})
                MATCH(user_d: Person {{email: '{USER_WITH_NO_FOLLOWINGS['email']}'}})
                MATCH(user_e: Person {{email: '{USER_WITH_MULTIPLE_POSTS['email']}'}})

                CREATE(post_a: Post {{id: apoc.create.uuid(), content: '{USER_WITH_THREE_FOLLOWINGS_POST_A['content']}'}})
                CREATE(post_b: Post {{id: apoc.create.uuid(), content: '{USER_WITH_THREE_FOLLOWINGS_POST_B['content']}'}})
                CREATE(user_a)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,1)}'}}] -> (post_a)
                CREATE(user_a)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,2)}'}}] -> (post_b)

                CREATE(post_c: Post {{id: apoc.create.uuid(), content: '{USER_WITH_TWO_FOLLOWINGS_POST_A['content']}'}})
                CREATE(post_d: Post {{id: apoc.create.uuid(), content: '{USER_WITH_TWO_FOLLOWINGS_POST_B['content']}'}})
                CREATE(post_e: Post {{id: apoc.create.uuid(), content: '{USER_WITH_TWO_FOLLOWINGS_POST_C['content']}'}})
                CREATE(user_b)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,3)}'}}] -> (post_c)
                CREATE(user_b)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,4)}'}}] -> (post_d)
                CREATE(user_b)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,5)}'}}] -> (post_e)

                CREATE(post_f: Post {{id: apoc.create.uuid(), content: '{USER_WITH_ONE_FOLLOWING_POST_A['content']}'}})
                CREATE(user_c)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,6)}'}}] -> (post_f)

                CREATE(post_g: Post {{id: apoc.create.uuid(), content: '{USER_WITH_NO_FOLLOWINGS_POST_A['content']}'}})
                CREATE(post_h: Post {{id: apoc.create.uuid(), content: '{USER_WITH_NO_FOLLOWINGS_POST_B['content']}'}})
                CREATE(user_d)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,7)}'}}] -> (post_g)
                CREATE(user_d)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,8)}'}}] -> (post_h)

                CREATE(post_j: Post {{id: apoc.create.uuid(), content: '{USER_POST_A['content']}'}})
                CREATE(post_k: Post {{id: apoc.create.uuid(), content: '{USER_POST_B['content']}'}})
                CREATE(user_e)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,9)}'}}] -> (post_j)
                CREATE(user_e)-[:POSTED {{date: '{datetime.datetime.now() + datetime.timedelta(0,10)}'}}] -> (post_k)
             """
FOLLOWS_AA = f"""
    MATCH (user_a:Person {{email:'{USER_FOLLOWING['email']}'}})
    MATCH (user_b:Person {{email:'{USER_BEING_FOLLOWED['email']}'}})
    CREATE (user_a)-[:FOLLOWS]->(user_b)
"""
RELATIONSHIPS_FOLLOWS_USER_A = f"""
    MATCH (user_a:Person {{email:'{USER_WITH_THREE_FOLLOWINGS['email']}'}})
    MATCH (user_b:Person {{email:'{USER_WITH_TWO_FOLLOWINGS['email']}'}})
    MATCH (user_c:Person {{email:'{USER_WITH_ONE_FOLLOWING['email']}'}})
    MATCH (user_d:Person {{email:'{USER_WITH_NO_FOLLOWINGS['email']}'}})
    CREATE (user_a)-[:FOLLOWS]->(user_b)
    CREATE (user_a)-[:FOLLOWS]->(user_c)
    CREATE (user_a)-[:FOLLOWS]->(user_d)"""

RELATIONSHIPS_FOLLOWS_USER_B = f"""
    MATCH (user_a:Person {{email:'{USER_WITH_THREE_FOLLOWINGS['email']}'}})
    MATCH (user_b:Person {{email:'{USER_WITH_TWO_FOLLOWINGS['email']}'}})
    MATCH (user_c:Person {{email:'{USER_WITH_ONE_FOLLOWING['email']}'}})
    MATCH (user_d:Person {{email:'{USER_WITH_NO_FOLLOWINGS['email']}'}})
    CREATE (user_b)-[:FOLLOWS]->(user_c)
    CREATE (user_b)-[:FOLLOWS]->(user_d)"""

RELATIONSHIPS_FOLLOWS_USER_C = f"""
    MATCH (user_a:Person {{email:'{USER_WITH_THREE_FOLLOWINGS['email']}'}})
    MATCH (user_b:Person {{email:'{USER_WITH_TWO_FOLLOWINGS['email']}'}})
    MATCH (user_c:Person {{email:'{USER_WITH_ONE_FOLLOWING['email']}'}})
    MATCH (user_d:Person {{email:'{USER_WITH_NO_FOLLOWINGS['email']}'}})
    CREATE (user_c)-[:FOLLOWS]->(user_d)"""

CONSTRAINT_USER_EMAIL_UNIQUE = "CREATE CONSTRAINT ON(user: Person) ASSERT user.email IS UNIQUE"
CONSTRAINT_USER_EMAIL_EXISTS = "CREATE CONSTRAINT ON(user: Person) ASSERT EXISTS (user.email)"
CONSTRAINT_POST_CONTENT_EXISTS = "CREATE CONSTRAINT ON(post: Post) ASSERT EXISTS (post.content)"

DELETE_ALL_NODES = "MATCH(n) DETACH DELETE n"

queries = [
    CONSTRAINT_POST_CONTENT_EXISTS,
    CONSTRAINT_USER_EMAIL_EXISTS,
    CONSTRAINT_USER_EMAIL_UNIQUE,
    CREATE_TEST_DATA,
    FOLLOWS_AA,
    CREATE_POSTS,
    CREATE_FOLLOWS_FOR_POSTS_USERS,
    RELATIONSHIPS_FOLLOWS_USER_A,
    RELATIONSHIPS_FOLLOWS_USER_B,
    RELATIONSHIPS_FOLLOWS_USER_C
]
