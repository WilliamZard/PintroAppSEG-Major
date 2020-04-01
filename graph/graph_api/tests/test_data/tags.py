import datetime
from collections import namedtuple

# TODO: this is duplicated across testing scripts. Refactor.
NOW = str(datetime.datetime.now()).replace(' ', 'T') + '000' + '+00:00'
TAG_PROPERTIES = ['created', 'name']
TAG_DEFAULTS = [NOW, 'Default Name']

Tag = namedtuple('Tag', TAG_PROPERTIES, defaults=TAG_DEFAULTS)
