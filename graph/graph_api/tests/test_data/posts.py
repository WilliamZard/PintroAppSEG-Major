import uuid
import datetime
from .users import USER_WITH_MULTIPLE_POSTS

# cypher datetime object requires T between date and time components
# and uses nanosecond precision
# and uses Z as shorthand for UTC time
# hence additional string operations below
NOW = str(datetime.datetime.now()).replace(' ', 'T') + '000Z'


# POSTS
POST_PROPERTIES = [
    "content",
    "created",
    "modified",
    "uuid",
]

# TODO: adjust existing_user data to fit data model
EXISTING_POST = dict(
    zip(POST_PROPERTIES, ['content x', NOW, NOW, uuid.uuid4()]))
NON_EXISTING_POST_UUID = 'uuid'

POST_TO_BE_UPDATED_THAT_EXISTS = dict(
    zip(POST_PROPERTIES, ['content y', NOW, NOW, uuid.uuid4()]))

POST_TO_BE_CREATED = {'content': 'content z',
                      'user_email': USER_WITH_MULTIPLE_POSTS['email']}

UUID_OF_POST_TO_BE_DELETED = uuid.uuid4()
POST_TO_BE_DELETED_THAT_EXISTS = dict(
    zip(POST_PROPERTIES, ['content y', NOW, NOW, UUID_OF_POST_TO_BE_DELETED]))

POST_UPDATE_A = {
    'new_content': 'Hey I have just update my post content. This is POST_UPDATE_A'}
POST_UPDATE_B = {
    'new_content': 'Hey I have just update my post content. This is POST_UPDATE_B'}

USER_POST_A = dict(
    zip(POST_PROPERTIES, ['Post A Content', NOW, NOW, uuid.uuid4()]))
USER_POST_B = dict(
    zip(POST_PROPERTIES, ['Post B Content', NOW, NOW, uuid.uuid4()]))

"""
# The first 2 posts will be assigned to USER_WITH_MULTIPLE_POSTS
USER_POST_A = dict(zip(POST_PROPERTIES, ['post2']))
USER_POST_B = dict(zip(POST_PROPERTIES, ['post1']))

# Third post is for posting tests
USER_POST_C = dict(zip(POST_PROPERTIES, ['post3']))
USER_WITH_THREE_FOLLOWINGS_POST_A = dict(
    zip(POST_PROPERTIES, ['USER_WITH_THREE_FOLLOWINGS first post']))
USER_WITH_THREE_FOLLOWINGS_POST_B = dict(
    zip(POST_PROPERTIES, ['USER_WITH_THREE_FOLLOWINGS second post']))

USER_WITH_TWO_FOLLOWINGS_POST_A = dict(
    zip(POST_PROPERTIES, ['USER_WITH_TWO_FOLLOWINGS first post']))
USER_WITH_TWO_FOLLOWINGS_POST_B = dict(
    zip(POST_PROPERTIES, ['USER_WITH_TWO_FOLLOWINGS second post']))
USER_WITH_TWO_FOLLOWINGS_POST_C = dict(
    zip(POST_PROPERTIES, ['USER_WITH_TWO_FOLLOWINGS third post']))

USER_WITH_ONE_FOLLOWING_POST_A = dict(
    zip(POST_PROPERTIES, ['USER_WITH_ONE_FOLLOWING first post']))

USER_WITH_NO_FOLLOWINGS_POST_A = dict(
    zip(POST_PROPERTIES, ['USER_WITH_NO_FOLLOWINGS first post']))
USER_WITH_NO_FOLLOWINGS_POST_B = dict(
    zip(POST_PROPERTIES, ['USER_WITH_NO_FOLLOWINGS second post']))"""
