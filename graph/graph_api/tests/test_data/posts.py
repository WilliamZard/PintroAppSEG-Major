import uuid
import datetime

from collections import namedtuple

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
POST_DEFAULTS = ['default_content', NOW, NOW, str(uuid.uuid4())]

Post = namedtuple('Post', POST_PROPERTIES, defaults=POST_DEFAULTS)
