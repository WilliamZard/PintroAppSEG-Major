import uuid
import datetime
from collections import namedtuple

# TODO: this is duplicated across testing scripts. Refactor.
NOW = str(datetime.datetime.now()).replace(' ', 'T') + '000' + '+00:00'
TAG_PROPERTIES = ['uuid', 'created', 'name']
TAG_DEFAULTS = [str(uuid.uuid4()), NOW, 'Default Name']

Tag = namedtuple('Tag', TAG_PROPERTIES, defaults=TAG_DEFAULTS)
"""
# Using custom labels for testing to keep things simple
LABEL_TAG = 'Tag'
LABEL_SKILL = 'Skill'
LABEL_PASSION = 'Passion'
KING_SLAYER_TAG = dict(
    zip(TAG_PROPERTIES, [str(uuid.uuid4()), NOW, 'King Slayer']))
KING_SLAYER_LABELS = {LABEL_SKILL, LABEL_TAG}
COLES_TAG = dict(
    zip(TAG_PROPERTIES, [str(uuid.uuid4()), NOW, 'Space Explorer']))
COLES_LABELS = {LABEL_TAG, LABEL_PASSION}
"""