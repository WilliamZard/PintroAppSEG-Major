# POSTS
POST_PROPERTIES = ["content"]
# The first 2 posts will be assigned to USER_WITH_MULTIPLE_POSTS
USER_POST_A = dict(zip(POST_PROPERTIES, ['post2']))
USER_POST_B = dict(zip(POST_PROPERTIES, ['post1']))
# Third post is for posting tests
USER_POST_C = dict(zip(POST_PROPERTIES, ['post3']))

POST_UPDATE_A = {
    'new_content': 'Hey I have just update my post content. This is POST_UPDATE_A'}
POST_UPDATE_B = {
    'new_content': 'Hey I have just update my post content. This is POST_UPDATE_B'}
