import uuid
import datetime
from collections import namedtuple

# TODO: this is duplicated across testing scripts. Refactor.
NOW = str(datetime.datetime.now()).replace(' ', 'T') + '000' + '+00:00'
TAG_PROPERTIES = ['uuid', 'created', 'name']
TAG_DEFAULTS = [str(uuid.uuid4()), NOW, 'Default Name']

Tag = namedtuple('Tag', TAG_PROPERTIES, defaults=TAG_DEFAULTS)
