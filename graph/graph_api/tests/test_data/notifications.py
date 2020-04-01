from collections import namedtuple
NOTIFICATION_PROPERTIES = [
    'requester_email',
    'recipient_email',
    'relationship_type',
    'created_at',
]


NOTIFICATION_DEFAULTS = [
    'requester_email',
    'recipient_email',
    'relationship_type',
    'created_at'
]

Notification = namedtuple(
    'Notification', NOTIFICATION_PROPERTIES, defaults=NOTIFICATION_DEFAULTS)
