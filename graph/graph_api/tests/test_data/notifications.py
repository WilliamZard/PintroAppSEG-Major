from collections import namedtuple
NOTIFICATION_PROPERTIES = [
    'requester_email',
    'recipient_email',
    'relationship_type'
]


NOTIFICATION_DEFAULTS = [
    'requester_email',
    'recipient_email',
    'relationship_type'
]

Notification = namedtuple(
    'Notification', NOTIFICATION_PROPERTIES, defaults=NOTIFICATION_DEFAULTS)
