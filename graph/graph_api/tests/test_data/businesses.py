# BUSINESSES
from .tags import COLES_TAG, KING_SLAYER_TAG
from collections import namedtuple
# TODO: what about using a dictionary to describe data needed for each test? Could give it some structure.
BUSINESS_PROPERTIES = [
    "password",
    "profile_image",
    "full_name",
    "phone",
    "short_bio",
    "location",
    "email",
    "story",
    "tags"]
BUSINESS_DEFAULTS = [
    "Default Password",
    "Default Image",
    "Default Full Name",
    "Default Phone",
    "Default Short Bio",
    "Default Location",
    "Default Email",
    "Default Story",
    "Default Tags"
]

Business = namedtuple('Business', BUSINESS_PROPERTIES,
                      defaults=BUSINESS_DEFAULTS)

VALID_BUSINESS = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'SaraLovelace', '911',
                                                'not godless', 'strand', 'not_ucl@kcl.ac.uk', 'What is GKT?', []]))

VALID_BUSINESS_TO_BE_UPDATED = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'DTrump', '000',
                                                              'genius', 'white house', 'genius@fakenews.cnn', 'Covfefe', []]))

VALID_BUSINESS_TO_BE_UPDATED_NEW_FIELDS = dict(zip(BUSINESS_PROPERTIES, ['0000', 'new_image', 'DonaldTrump', '999',
                                                                         'retired genius', 'Mar O Lago', 'genius@fakenews.cnn', 'revolutionary', []]))
VALID_BUSINESS_TO_BE_DELETED = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'Taaj', '123',
                                                              'going places', 'Gatwick init', 'taaj@hotmail.co.uk', 'you get me?', []]))
VALID_BUSINESS_TO_BE_CREATED_TAGS = [
    COLES_TAG['uuid'], KING_SLAYER_TAG['uuid']]
VALID_BUSINESS_TO_BE_CREATED = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'Precious', '111',
                                                              'best kiosk in town', 'Gatwickk', 'precious@gmail.com', 'Likeable and devout.', VALID_BUSINESS_TO_BE_CREATED_TAGS]))

INVALID_BUSINESS_TO_BE_CREATED = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'precious', '111',
                                                                'best kiosk in town', 'Gatwickk', 'preciousgmail.com', 'Likeable and devout.', []]))

BUSINESS_WITH_MULTIPLE_POSTS = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'John',  '111',
                                                              'I was a student', 'London', 'user_with_posts@gmail.com', 'eat, sleep, repeat.', []]))

BUSINESS_THAT_CREATES_POST = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'John1', '111',
                                                            'I was a student', 'London', 'user_creates_post@gmail.com', 'eat, sleep, repeat.', []]))

BUSINESS_ABOUT_TO_FOLLOW = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'KingtjWellington', '911',
                                                          'not godless', 'strand', 'no_ucl_business@kcl.ac.uk', 'What is GKT?', []]))

BUSINESS_ABOUT_TO_BE_FOLLOWED = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'kcler', '911',
                                                               'not godless', 'strand', 'kclser@kcl.ac.uk', 'What is GKT?', []]))

BUSINESS_FOLLOWING = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'KingWellingtonaa', '911',
                                                    'not godless', 'strand', 'business_creative_email@kcl.ac.uk', 'What is GKT?', []]))

BUSINESS_BEING_FOLLOWED = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'KingWellingtonbbb', '911',
                                                         'not godless', 'strand', 'very_creative_email@kcl.ac.uk', 'What is GKT?', []]))

BUSINESS_WITH_THREE_FOLLOWINGS = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'DukeWellingtona', '911',
                                                                'not godless', 'strand', 'yes_ucl@kcl.ac.uk', 'What is GKT?', []]))

BUSINESS_WITH_TWO_FOLLOWINGS = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'LeonardoDiCaprio', '000',
                                                              'I am the MVP', 'US', 'lello@gmail.com', 'I won a best movie award', []]))

BUSINESS_WITH_ONE_FOLLOWING = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'JohnJonnyaaa', '111',
                                                             'I am millionaire', 'London', 'business_jj@gmail.com', 'I started as a taxi driver.', []]))

BUSINESS_WITH_NO_FOLLOWINGS = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'JohnKennedygkdf', '121',
                                                             'The only one pres', 'Unknown', 'jfk@gmail.com', 'They thought they killed me.', []]))

BUSINESS_WITH_FOLLOWINGS_THAT_HAVE_POSTS = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'JohnSnow', '121',
                                                                          'King of the noorth', 'Unknown', 'john.snow@winteriscoming.wes', 'ay', []]))

BUSINESS_THAT_POSTED_POST_A = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'JamesBond', '007',
                                                             'James, James Bond', 'Unknown', 'james.bond@mi5.co.uk', 'Yessir', []]))

BUSINESS_THAT_POSTED_POST_B = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'M', '121',
                                                             'Siberia', 'Unknown', 'm@m.co.uk', 'shut it 007', []]))

AFFILIATION_REQUESTER_A = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'evilcorp', '121',
                                                         'Siberia', 'Unknown', 'evil@corp.co.uk', 'shut it 007', []]))

AFFILIATION_REQUESTER_B = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'umbrellacorp', '121',
                                                         'Siberia', 'Unknown', 'umbrella@corp.co.uk', 'shut it 007', []]))
BUSINESS_REQUESTING_AFFILIATION_TO_USER = dict(zip(BUSINESS_PROPERTIES, ['password', 'image', 'ronacorp', '121',
                                                                         'Siberia', 'Unknown', 'rona@corp.co.uk', 'shut it 007', []]))
NONEXISTANT_BUSINESS_EMAIL = 'does@exist.not'

INVALID_EMAIL = 'invalidateme.now'
