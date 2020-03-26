from .users import USER_WITH_NOTIFICATIONS, USER_REQUESTING_USER_WITH_NOTIFICATIONS_A
from .businesses import BUSINESS_REQUESTING_AFFILIATION_TO_USER
from collections import namedtuple
# TODO: add created property to relationships
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
NOTIFICATION_A = dict(zip(NOTIFICATION_PROPERTIES, [
                      USER_REQUESTING_USER_WITH_NOTIFICATIONS_A['email'], USER_WITH_NOTIFICATIONS['email'], 'follow']))

NOTIFICATION_B = dict(zip(NOTIFICATION_PROPERTIES, [
                      BUSINESS_REQUESTING_AFFILIATION_TO_USER['email'], USER_WITH_NOTIFICATIONS['email'], 'affiliation']))
