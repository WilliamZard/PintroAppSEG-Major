# TODO: pandas should not needed in production and is a heavy library. Find a way to only use it in testing.
import datetime
import os
from neo4j import GraphDatabase


from .test_data.users import *
from .test_data.businesses import *
from .test_data.spaces import *
from .test_data.posts import *
from .test_data.tags import *
from .test_data.businesses import *
from .test_data.spaces import *
from .test_data.chatrooms import *
from .test_data.notifications import *

USERS_TO_TEST = [
    DEACTIVATED_USER,
    ACTIVATED_USER,
    VALID_USER,
    VALID_USER_TO_BE_UPDATED,
    VALID_USER_TO_BE_DELETED,
    USER_WITH_MULTIPLE_POSTS,
    USER_WITH_THREE_FOLLOWINGS,
    USER_WITH_TWO_FOLLOWINGS,
    USER_WITH_ONE_FOLLOWING,
    USER_WITH_NO_FOLLOWINGS,
    FOLLOW_REQUESTER_A,
    FOLLOW_REQUESTER_B,
    FOLLOW_REQUEST_RECIPIENT,
    USER_FOLLOWING,
    USER_BEING_FOLLOWED,
    USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS,
    USER_THAT_POSTED_POST_A,
    USER_THAT_POSTED_POST_B,
    AFFILIATION_REQUEST_RECIPIENT,
    USER_WITH_NOTIFICATIONS,
    USER_REQUESTING_USER_WITH_NOTIFICATIONS_A
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
        session.write_transaction(_run_query, DROP_SEARCH_USER_INDEX)
        session.write_transaction(_run_query, DROP_SEARCH_BUSINESS_INDEX)
        session.write_transaction(_run_query, DROP_SEARCH_SPACE_INDEX)


def _run_query(tx, query):
    return tx.run(query)


# TODO: restructure this
CREATE_TEST_DATA = ""
for USER in USERS_TO_TEST:
    CREATE_TEST_DATA += "CREATE (" + USER['preferred_name'] + ":Person { "
    CREATE_TEST_DATA += "password: \'" + USER['password'] + "\' , "
    CREATE_TEST_DATA += "profile_image: \'" + USER['profile_image'] + "\' , "
    CREATE_TEST_DATA += "full_name: \'" + USER['full_name'] + "\' , "
    CREATE_TEST_DATA += "gender: \'" + USER['gender'] + "\' , "
    CREATE_TEST_DATA += "phone: \'" + USER['phone'] + "\' , "
    CREATE_TEST_DATA += "short_bio: \'" + USER['short_bio'] + "\' , "
    CREATE_TEST_DATA += "location: \'" + USER['location'] + "\' , "
    CREATE_TEST_DATA += "job_title: \'" + USER['job_title'] + "\' , "
    CREATE_TEST_DATA += "preferred_name: \'" + USER['preferred_name'] + "\' , "
    CREATE_TEST_DATA += "email: \'" + str(USER['email']) + "\' , "
    CREATE_TEST_DATA += "education: \'" + USER['education'] + "\' , "
    CREATE_TEST_DATA += "active: \'" + USER['active'] + "\' , "
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

FOLLOWS_AA = f"""
    MATCH (user_a:Person {{email:'{USER_FOLLOWING['email']}'}})
    MATCH (user_b:Person {{email:'{USER_BEING_FOLLOWED['email']}'}})
    CREATE (user_a)-[:FOLLOWS]->(user_b)
"""

CREATE_FOLLOW_REQUESTS = f"""
    MATCH (user_a:Person {{email:'{FOLLOW_REQUESTER_A['email']}'}})
    MATCH (user_b:Person {{email:'{FOLLOW_REQUESTER_B['email']}'}})
    MATCH (user_c:Person {{email:'{FOLLOW_REQUEST_RECIPIENT['email']}'}})
    CREATE (user_a)-[:REQUESTED_FOLLOW]->(user_c)
    CREATE (user_b)-[:REQUESTED_FOLLOW]->(user_c)
"""

CREATE_FOLLOW_REQUEST_FOR_NOTIFICATION_TEST = f"""
    MATCH (user_a:Person {{email:'{USER_REQUESTING_USER_WITH_NOTIFICATIONS_A['email']}'}})
    MATCH (user_b:Business {{email:'{BUSINESS_REQUESTING_AFFILIATION_TO_USER['email']}'}})
    MATCH (user_c:Person {{email:'{USER_WITH_NOTIFICATIONS['email']}'}})
    CREATE (user_a)-[:REQUESTED_FOLLOW]->(user_c)
    CREATE (user_b)-[:REQUESTED_AFFILIATION]->(user_c)
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

CREATE_AFFILIATION_REQUESTS = f"""
    MATCH (user_a:Business {{email:'{AFFILIATION_REQUESTER_A['email']}'}})
    MATCH (user_b:Business {{email:'{AFFILIATION_REQUESTER_B['email']}'}})
    MATCH (user_c:Person {{email:'{AFFILIATION_REQUEST_RECIPIENT['email']}'}})
    CREATE (user_a)-[:REQUESTED_AFFILIATION]->(user_c)
    CREATE (user_b)-[:REQUESTED_AFFILIATION]->(user_c)
"""

CONSTRAINT_USER_EMAIL_UNIQUE = "CREATE CONSTRAINT ON(user: Person) ASSERT user.email IS UNIQUE"
CONSTRAINT_USER_EMAIL_EXISTS = "CREATE CONSTRAINT ON(user: Person) ASSERT EXISTS (user.email)"
CONSTRAINT_POST_CONTENT_EXISTS = "CREATE CONSTRAINT ON(post: Post) ASSERT EXISTS (post.content)"

DELETE_ALL_NODES = "MATCH(n) DETACH DELETE n"

TAGS = [KING_SLAYER_TAG, COLES_TAG]
TAG_LABELS = [KING_SLAYER_LABELS, COLES_LABELS]

create_tag_queries = []
for tag, tag_labels in zip(TAGS, TAG_LABELS):
    labels = ':'.join(tag_labels)
    query = f"""CREATE (new_tag:{labels} {{name: "{tag['name']}", created: datetime("{tag['created']}"), uuid: "{tag['uuid']}"}})"""
    create_tag_queries.append(query)

ASSOCIATE_VALID_USER_TO_THEIR_TAGS = f"""
MATCH (valid_user:Person {{email: '{VALID_USER['email']}'}})
MATCH (tag_a:Tag {{uuid: '{COLES_TAG['uuid']}'}})
MATCH (tag_b:Tag {{uuid: '{KING_SLAYER_TAG['uuid']}'}})
CREATE (valid_user)-[:TAGGED]->(tag_a)
CREATE (valid_user)-[:TAGGED]->(tag_b)
"""

BUSINESSES_TO_TEST = [
    VALID_BUSINESS,
    VALID_BUSINESS_TO_BE_UPDATED,
    VALID_BUSINESS_TO_BE_DELETED,
    BUSINESS_WITH_MULTIPLE_POSTS,
    BUSINESS_WITH_THREE_FOLLOWINGS,
    BUSINESS_WITH_TWO_FOLLOWINGS,
    BUSINESS_WITH_ONE_FOLLOWING,
    BUSINESS_WITH_NO_FOLLOWINGS,
    BUSINESS_ABOUT_TO_FOLLOW,
    BUSINESS_ABOUT_TO_BE_FOLLOWED,
    BUSINESS_FOLLOWING,
    BUSINESS_BEING_FOLLOWED,
    BUSINESS_WITH_FOLLOWINGS_THAT_HAVE_POSTS,
    AFFILIATION_REQUESTER_A,
    AFFILIATION_REQUESTER_B,
    BUSINESS_REQUESTING_AFFILIATION_TO_USER
]

# TODO: restructure this
CREATE_TEST_BUSINESS_DATA = ""
for BUSINESS in BUSINESSES_TO_TEST:
    CREATE_TEST_BUSINESS_DATA += "CREATE (" + \
        BUSINESS['full_name'] + ":Business { "
    CREATE_TEST_BUSINESS_DATA += "full_name: \'" + \
        BUSINESS['full_name'] + "\' , "
    CREATE_TEST_BUSINESS_DATA += "password: \'" + \
        BUSINESS['password'] + "\' , "
    CREATE_TEST_BUSINESS_DATA += "profile_image: \'" + \
        BUSINESS['profile_image'] + "\' , "
    CREATE_TEST_BUSINESS_DATA += "phone: \'" + BUSINESS['phone'] + "\' , "
    CREATE_TEST_BUSINESS_DATA += "short_bio: \'" + \
        BUSINESS['short_bio'] + "\' , "
    CREATE_TEST_BUSINESS_DATA += "location: \'" + \
        BUSINESS['location'] + "\' , "
    CREATE_TEST_BUSINESS_DATA += "email: \'" + BUSINESS['email'] + "\' , "
    CREATE_TEST_BUSINESS_DATA += "story: \'" + BUSINESS['story'] + "\'}) \n"


CONSTRAINT_BUSINESS_EMAIL_UNIQUE = "CREATE CONSTRAINT ON(user: Business) ASSERT user.email IS UNIQUE"


SPACES_TO_TEST = [
    VALID_SPACE,
    VALID_SPACE_TO_BE_UPDATED,
    VALID_SPACE_TO_BE_DELETED,
    SPACE_WITH_MULTIPLE_POSTS,
    SPACE_WITH_THREE_FOLLOWINGS,
    SPACE_WITH_TWO_FOLLOWINGS,
    SPACE_WITH_ONE_FOLLOWING,
    SPACE_WITH_NO_FOLLOWINGS,
    SPACE_ABOUT_TO_FOLLOW,
    SPACE_ABOUT_TO_BE_FOLLOWED,
    SPACE_FOLLOWING,
    SPACE_BEING_FOLLOWED,
    SPACE_WITH_FOLLOWINGS_THAT_HAVE_POSTS
]


CREATE_TEST_SPACE_DATA = ""
for SPACE in SPACES_TO_TEST:
    CREATE_TEST_SPACE_DATA += "CREATE (" + SPACE['full_name'] + ":Space { "
    CREATE_TEST_SPACE_DATA += "full_name: \'" + SPACE['full_name'] + "\' , "
    CREATE_TEST_SPACE_DATA += "password: \'" + SPACE['password'] + "\' , "
    CREATE_TEST_SPACE_DATA += "profile_image: \'" + \
        SPACE['profile_image'] + "\' , "
    CREATE_TEST_SPACE_DATA += "phone: \'" + SPACE['phone'] + "\' , "
    CREATE_TEST_SPACE_DATA += "short_bio: \'" + SPACE['short_bio'] + "\' , "
    CREATE_TEST_SPACE_DATA += "location: \'" + SPACE['location'] + "\' , "
    CREATE_TEST_SPACE_DATA += "email: \'" + SPACE['email'] + "\'}) \n"


CREATE_EXISTING_CHATROOM_DATA = ""
for CHAT in CHATROOMS:
    print(CHAT)
    CREATE_EXISTING_CHATROOM_DATA += "CREATE (:Chatroom { "
    CREATE_EXISTING_CHATROOM_DATA += "chat_id: \'" + CHAT + "\'}) \n"
for USER in CHATROOM_USERS:
    CREATE_EXISTING_CHATROOM_DATA += "CREATE (" + \
        USER['preferred_name'] + ":Person { "
    CREATE_EXISTING_CHATROOM_DATA += "password: \'" + \
        USER['password'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "profile_image: \'" + \
        USER['profile_image'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "full_name: \'" + \
        USER['full_name'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "gender: \'" + USER['gender'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "phone: \'" + USER['phone'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "short_bio: \'" + \
        USER['short_bio'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "location: \'" + \
        USER['location'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "job_title: \'" + \
        USER['job_title'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "preferred_name: \'" + \
        USER['preferred_name'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "email: \'" + USER['email'] + "\' , "
    CREATE_EXISTING_CHATROOM_DATA += "story: \'" + USER['story'] + "\'}) \n"

CREATE_CHATROOM_RELATIONSHIPS_A = (
    f"MATCH (user_a:Person {{email: '{CHATROOM_USERS[0]['email']}'}})\n"
    f"MATCH (user_b:Person {{email: '{CHATROOM_USERS[1]['email']}'}})\n"
    f"MATCH (chat:Chatroom {{chat_id: '{CHATROOMS[0]}'}})\n"
    "CREATE (user_a)-[:CHATS_IN]->(chat)\n"
    "CREATE (user_b)-[:CHATS_IN]->(chat)"
)
CREATE_CHATROOM_RELATIONSHIPS_B = (
    f"MATCH (user_a:Person {{email: '{CHATROOM_USERS[0]['email']}'}})\n"
    f"MATCH (user_b:Person {{email: '{CHATROOM_USERS[2]['email']}'}})\n"
    f"MATCH (chat:Chatroom {{chat_id: '{CHATROOMS[1]}'}})\n"
    "CREATE (user_a)-[:CHATS_IN]->(chat)\n"
    "CREATE (user_b)-[:CHATS_IN]->(chat)"
)

CREATE_TO_BE_DELETED_CHATROOM_DATA = "CREATE (:Chatroom { "
CREATE_TO_BE_DELETED_CHATROOM_DATA += "chat_id: \'" + \
    VALID_CHATROOM_TO_BE_DELETED + "\'}) \n"
for USER in VALID_CHATROOM_TO_BE_DELETED_USERS:
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "CREATE (" + \
        USER['preferred_name'] + ":Person { "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "password: \'" + \
        USER['password'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "profile_image: \'" + \
        USER['profile_image'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "full_name: \'" + \
        USER['full_name'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "gender: \'" + \
        USER['gender'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "phone: \'" + USER['phone'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "short_bio: \'" + \
        USER['short_bio'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "location: \'" + \
        USER['location'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "job_title: \'" + \
        USER['job_title'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "preferred_name: \'" + \
        USER['preferred_name'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "email: \'" + USER['email'] + "\' , "
    CREATE_TO_BE_DELETED_CHATROOM_DATA += "story: \'" + \
        USER['story'] + "\'}) \n"

CREATE_CHATROOM_RELATIONSHIPS_C = (
    f"MATCH (user_a:Person {{email: '{VALID_CHATROOM_TO_BE_DELETED_USERS[0]['email']}'}})\n"
    f"MATCH (user_b:Person {{email: '{VALID_CHATROOM_TO_BE_DELETED_USERS[1]['email']}'}})\n"
    f"MATCH (chat:Chatroom {{chat_id: '{VALID_CHATROOM_TO_BE_DELETED}'}})\n"
    "CREATE (user_a)-[:CHATS_IN]->(chat)\n"
    "CREATE (user_b)-[:CHATS_IN]->(chat)"
)

CREATE_TO_BE_CREATED_CHATROOM_DATA = ""
for USER in CHATROOM_TO_BE_CREATED_USERS:
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "CREATE (" + \
        USER['preferred_name'] + ":Person { "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "password: \'" + \
        USER['password'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "profile_image: \'" + \
        USER['profile_image'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "full_name: \'" + \
        USER['full_name'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "gender: \'" + \
        USER['gender'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "phone: \'" + USER['phone'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "short_bio: \'" + \
        USER['short_bio'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "location: \'" + \
        USER['location'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "job_title: \'" + \
        USER['job_title'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "preferred_name: \'" + \
        USER['preferred_name'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "email: \'" + USER['email'] + "\' , "
    CREATE_TO_BE_CREATED_CHATROOM_DATA += "story: \'" + \
        USER['story'] + "\'}) \n"


CONSTRAINT_SPACE_EMAIL_UNIQUE = "CREATE CONSTRAINT ON(user: Space) ASSERT user.email IS UNIQUE"

CREATE_SEARCH_USER_INDEX = "CALL db.index.fulltext.createNodeIndex('SearchUserIndex', ['Person'], ['full_name', 'email', 'short_bio', 'story'])"
DROP_SEARCH_USER_INDEX = "CALL db.index.fulltext.drop(\"SearchUserIndex\")"

CREATE_SEARCH_BUSINESS_INDEX = "CALL db.index.fulltext.createNodeIndex('SearchBusinessIndex', ['Business'], ['full_name', 'email', 'short_bio', 'story'])"
DROP_SEARCH_BUSINESS_INDEX = "CALL db.index.fulltext.drop(\"SearchBusinessIndex\")"

CREATE_SEARCH_SPACE_INDEX = "CALL db.index.fulltext.createNodeIndex('SearchSpaceIndex', ['Space'], ['full_name', 'email', 'short_bio', 'story'])"
DROP_SEARCH_SPACE_INDEX = "CALL db.index.fulltext.drop(\"SearchSpaceIndex\")"

CONSTRAINT_CHATROOM_ID_UNIQUE = "CREATE CONSTRAINT ON(chat: Chatroom) ASSERT chat.chat_id IS UNIQUE"

queries = [
    CREATE_SEARCH_USER_INDEX,
    CREATE_SEARCH_BUSINESS_INDEX,
    CREATE_SEARCH_SPACE_INDEX,
    CONSTRAINT_POST_CONTENT_EXISTS,
    CONSTRAINT_USER_EMAIL_EXISTS,
    CONSTRAINT_USER_EMAIL_UNIQUE,
    CONSTRAINT_SPACE_EMAIL_UNIQUE,
    CREATE_TEST_SPACE_DATA,
    CONSTRAINT_BUSINESS_EMAIL_UNIQUE,
    CREATE_TEST_BUSINESS_DATA,
    CREATE_TEST_DATA,
    FOLLOWS_AA,
    CREATE_POSTS,
    CREATE_FOLLOWS_FOR_POSTS_USERS,
    RELATIONSHIPS_FOLLOWS_USER_A,
    RELATIONSHIPS_FOLLOWS_USER_B,
    RELATIONSHIPS_FOLLOWS_USER_C,
    *create_tag_queries,
    ASSOCIATE_VALID_USER_TO_THEIR_TAGS,
    CREATE_FOLLOW_REQUESTS,
    CREATE_AFFILIATION_REQUESTS,
    CONSTRAINT_CHATROOM_ID_UNIQUE,
    CREATE_EXISTING_CHATROOM_DATA,
    CREATE_CHATROOM_RELATIONSHIPS_A,
    CREATE_CHATROOM_RELATIONSHIPS_B,
    CREATE_TO_BE_DELETED_CHATROOM_DATA,
    CREATE_CHATROOM_RELATIONSHIPS_C,
    CREATE_TO_BE_CREATED_CHATROOM_DATA,
]
