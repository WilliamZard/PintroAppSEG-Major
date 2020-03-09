import uuid
import datetime

# TODO: this is duplicated across testing scripts. Refactor.
NOW = str(datetime.datetime.now()).replace(' ', 'T') + '000' + '+00:00'
TAG_PROPERTIES = ['uuid', 'created', 'name']

# Using custom labels for testing to keep things simple
LABEL_TAG = 'Tag'
LABEL_GOT = 'GOT'
LABEL_KCL = 'KCL'


KING_SLAYER = dict(
    zip(TAG_PROPERTIES, [str(uuid.uuid4()), NOW, 'King Slayer']))
KING_SLAYER_LABELS = {LABEL_TAG, LABEL_GOT}

COLES = dict(zip(TAG_PROPERTIES, [str(uuid.uuid4()), NOW, 'Space Explorer']))
COLES_LABELS = {LABEL_TAG, LABEL_KCL}
