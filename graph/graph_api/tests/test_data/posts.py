import uuid
import datetime
from .users import USER_WITH_MULTIPLE_POSTS

NOW = str(datetime.datetime.now())

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
# The first 2 posts will be assigned to USER_WITH_MULTIPLE_POSTS
USER_POST_A = dict(zip(POST_PROPERTIES, ['post2']))
USER_POST_B = dict(zip(POST_PROPERTIES, ['post1']))

# Third post is for posting tests
USER_POST_C = dict(zip(POST_PROPERTIES, ['post3']))

POST_UPDATE_A = {
    'new_content': 'Hey I have just update my post content. This is POST_UPDATE_A'}
POST_UPDATE_B = {
    'new_content': 'Hey I have just update my post content. This is POST_UPDATE_B'}
