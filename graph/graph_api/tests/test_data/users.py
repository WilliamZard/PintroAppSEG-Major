# # USERS
# from .tags import COLES_TAG, KING_SLAYER_TAG
# # TODO: what about using a dictionary to describe data needed for each test? Could give it some structure.

# active = True

# USERS_PROPERTIES = [
#     "password",
#     "profile_image",
#     "education",
#     "full_name",
#     "gender",
#     "phone",
#     "short_bio",
#     "location",
#     "job_title",
#     "preferred_name",
#     "email",
#     "story",
#     "tags",
#     "active"]

# VALID_USER_TAGS = {'King Slayer': [
#     'GOT', 'Tag'], 'Space Explorer': ['Tag', 'KCL']}
# VALID_USER = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'Duke Wellington', 'male', '911',
#                                          'not godless', 'strand', 'Duke', 'Duke', 'not_ucl@kcl.ac.uk', 'What is GKT?', VALID_USER_TAGS, str(active)]))
# VALID_USER_TO_BE_UPDATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Home', 'DTrump', 'male?', '000',
#                                                        'genius', 'whit house', 'Commander n sth', 'MrPres', 'genius@fakenews.cnn', 'Covfefe', {}, str(active)]))
# VALID_USER_TO_BE_UPDATED_NEW_TAG_UUIDS = [COLES_TAG['uuid']]
# VALID_USER_TO_BE_UPDATED_NEW_FIELDS = dict(zip(USERS_PROPERTIES, ['0000', 'new_image', 'Care Home', 'Donald Trump', 'masculine', '999',
#                                                                   'retired genius', 'Mar O Lago', 'Former Best President', 'GOAT', 'genius@fakenews.cnn', 'revolutionary', VALID_USER_TO_BE_UPDATED_NEW_TAG_UUIDS, str(active)]))
# VALID_USER_TO_BE_DELETED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'Taaj', 'man', '123',
#                                                        'going places', 'Gatwick init', 'going places', 'Taaj', 'taaj@hotmail.co.uk', 'you get me?', {}, str(active)]))
# VALID_USER_TO_BE_CREATED_TAGS = [COLES_TAG['uuid'], KING_SLAYER_TAG['uuid']]
# VALID_USER_TO_BE_CREATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'precious', 'man', '111',
#                                                        'best kiosk in town', 'Gatwickk', 'Precious', 'Precious', 'precious@gmail.com', 'Likeable and devout.', VALID_USER_TO_BE_CREATED_TAGS, str(active)]))

# INVALID_USER_TO_BE_CREATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'precious', 'man', '111',
#                                                          'best kiosk in town', 'Gatwickk', 'Precious', 'Preciousest', 'preciousgmail.com', 'Likeable and devout.', {}, str(active)]))

# USER_WITH_MULTIPLE_POSTS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'UCL', 'John', 'male', '111',
#                                                        'I was a student', 'London', 'unemployed', 'Jonny', 'user_with_posts@gmail.com', 'eat, sleep, repeat.', {}, str(active)]))

# USER_THAT_CREATES_POST = dict(zip(USERS_PROPERTIES, ['password', 'image', 'UCL', 'John', 'male', '111',
#                                                      'I was a student', 'London', 'unemployed', 'Jonny', 'user_creates_post@gmail.com', 'eat, sleep, repeat.', {}, str(active)]))
# USER_ABOUT_TO_FOLLOW = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'King Wellington', 'male', '911',
#                                                    'not godless', 'strand', 'no_ucl_King', 'no_ucl_King', 'no_ucl@kcl.ac.uk', 'What is GKT?', {}, str(active)]))
# USER_ABOUT_TO_BE_FOLLOWED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'kcler', 'male', '911',
#                                                         'not godless', 'strand', 'kclser_King', 'kclser_King', 'kclser@kcl.ac.uk', 'What is GKT?', {}, str(active)]))
# USER_FOLLOWING = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'King Wellington', 'male', '911',
#                                              'not godless', 'strand', 'very_creative_King', 'very_createive_King', 'creative_email@kcl.ac.uk', 'What is GKT?', {}, str(active)]))

# USER_BEING_FOLLOWED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'King Wellington', 'male', '911',
#                                                   'not godless', 'strand', 'creative_King', 'creative_King', 'very_creative_email@kcl.ac.uk', 'What is GKT?', {}, str(active)]))
# USER_WITH_THREE_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'Duke Wellington', 'male', '911',
#                                                          'not godless', 'strand', 'Duke', 'Dukee', 'yes_ucl@kcl.ac.uk', 'What is GKT?', {}, str(active)]))
# USER_WITH_TWO_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Bachelors', 'Leonardo Di Caprio', 'male', '000',
#                                                        'I am the MVP', 'US', 'Actor', 'Lello', 'lello@gmail.com', 'I won a best movie award', {}, str(active)]))
# USER_WITH_ONE_FOLLOWING = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Secondary school', 'John Jonny', 'male', '111',
#                                                       'I am millionaire', 'London', 'Entrepreneur', 'Sweety', 'jj@gmail.com', 'I started as a taxi driver.', {}, str(active)]))
# USER_WITH_NO_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Diploma', 'John Kennedy', 'male', '121',
#                                                       'The only one pres', 'Unknown', 'Retired', 'JFK', 'jfk@gmail.com', 'They thought they killed me.', {}, str(active)]))
# USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Winter', 'John Snow', 'male', '121',
#                                                                    'King of the noorth', 'Unknown', 'Up and coming', 'Snowy', 'john.snow@winteriscoming.wes', 'ay',{}, str(active)]))
# USER_THAT_POSTED_POST_A = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Winter', 'James Bond', 'male', '007',
#                                                       'James, James Bond', 'Unknown', 'Up and coming', 'Shaken', 'james.bond@mi5.co.uk', 'Yessir',{}, str(active)]))
# USER_THAT_POSTED_POST_B = dict(zip(USERS_PROPERTIES, ['password', 'image', 'UK', 'M', 'female', '121',
#                                                       'Siberia', 'Unknown', 'Up and coming', 'Queen_of_numbers', 'm@m.co.uk', 'shut it 007', {}, str(active)]))

# DEACTIVATED_USER = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'Dule Weington', 'male', '911',
#                                          'not godless', 'strand', 'Dule', 'Dule', 'nothing_ucl@kcl.ac.uk', 'What is GKT?', {}, str(not active)]))

# ACTIVATED_USER = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'Sule Wule', 'male', '911',
#                                          'not godless', 'strand', 'Sule', 'Sule', 'Sule_wule@kcl.ac.uk', 'What is GKT?', {}, str(active)]))



# NONEXISTANT_USER_EMAIL = 'does@exist.not'
# INVALID_EMAIL = 'invalidateme.now'
# USERS
from collections import namedtuple
# TODO: what about using a dictionary to describe data needed for each test? Could give it some structure.

active = True

USERS_PROPERTIES = [
    'full_name', 'preferred_name', 'profile_image', 'short_bio', 'gender', 'story',
    'email', 'phone_number', 'job_title', 'current_company', 'years_in_industry',
    'industry', 'previous_company', 'previous_company_year_finished', 'university',
    'university_year_finished', 'academic_level', 'location', 'date_of_birth', 'passions',
    'help_others', 'active']
USER_DEFAULTS = [
    'Default Name', 'Defaulter', 'Default Image', 'Default Short Bio', 'Default Gender',
    'Default Story', 'default@default.com', '000', 'Default Job Title', 'Default Current Company',
    100, 'Default Industry', 'Default previous company', '10', 'Default University', 1812,
    'Default Academic Level', 'Default Location', '01/01/1812', [], [], 'True']

User = namedtuple('User', USERS_PROPERTIES, defaults=USER_DEFAULTS)


FOLLOW_REQUESTER_A = User(email='no_ucl@kcl.ac.uk')._asdict()

# TODO: fill in tags
VALID_USER_PASSIONS = []
VALID_USER_SKILLS = []
VALID_USER = User(full_name='Duke Wellington', email='duke@wellington.com',
                  passions=VALID_USER_PASSIONS, help_others=VALID_USER_SKILLS)._asdict()
VALID_USER_TO_BE_UPDATED = User(
    full_name='Donald Trump', email='genius@fakenews.cnn')._asdict()
# VALID_USER_TO_BE_UPDATED_NEW_TAG_UUIDS = [COLES_TAG['uuid']]
# VALID_USER_TO_BE_UPDATED_NEW_FIELDS = User(
#     profile_image='new_image', full_name='Donald Trump', gender='masculine',
#     phone_number='999', short_bio='retired genius', location='Mar O Lago', job_title='Former Best President',
#     preferred_name='GOAT', help_others=VALID_USER_TO_BE_UPDATED_NEW_TAG_UUIDS
# )._asdict()
VALID_USER_TO_BE_DELETED = User(
    university='Gatwick Airpot', full_name='taaj', email='taaj@hotmail.co.uk')._asdict()
# VALID_USER_TO_BE_CREATED_TAGS = [COLES_TAG['uuid'], KING_SLAYER_TAG['uuid']]
VALID_USER_TO_BE_CREATED = User(
    full_name='precious', email='precious@gmail.com')._asdict()
INVALID_USER_TO_BE_CREATED = User(
    full_name='precious', email='praciousgmail.com')._asdict()
AFFILIATION_REQUEST_RECIPIENT = User(email='meo@meo.com')._asdict()
USER_WITH_MULTIPLE_POSTS = User(email='user_with_posts@gmail.com')._asdict()
USER_THAT_CREATES_POST = User(email='user_creaets_post@gmail.com')._asdict()
FOLLOW_REQUESTER_A = User(email='no_ucl@kcl.ac.uk')._asdict()
FOLLOW_REQUESTER_B = User(email='poo_cl@kcl.ac.uk')._asdict()
USER_ABOUT_TO_FOLLOW = User(email='ucl@kcl.ac.uk')._asdict()
USER_ABOUT_TO_BE_FOLLOWED = User(email='kclser@kcl.ac.uk')._asdict()
USER_FOLLOWING = User(email='creative_email@kcl.ac.uk')._asdict()
FOLLOW_REQUEST_RECIPIENT = User(email='kcler@kcl.ac.uk')._asdict()
USER_BEING_FOLLOWED = User(email='very_creative_email@kcl.ac.uk')._asdict()
USER_WITH_THREE_FOLLOWINGS = User(email='yes_ucl@kcl.ac.uk')._asdict()
USER_WITH_TWO_FOLLOWINGS = User(email='lello@gmail.com')._asdict()
USER_WITH_ONE_FOLLOWING = User(email='jj@gmail.com')._asdict()
USER_WITH_NO_FOLLOWINGS = User(email='jfk@gmail.com')._asdict()
USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS = User(
    email='johnsnow@westeros.com')._asdict()
USER_THAT_POSTED_POST_A = User(email='james.bond@mi5.co.uk')._asdict()
USER_THAT_POSTED_POST_B = User(email='m@m.co.uk')._asdict()
DEACTIVATED_USER = User(email='nothing_ucl@kcl.ac.uk')._asdict()
ACTIVATED_USER = User(email='sule_wule@kcl.ac.uk')._asdict()
USER_WITH_NOTIFICATIONS = User(email='quarantine@kcl.ac.uk')._asdict()
USER_REQUESTING_USER_WITH_NOTIFICATIONS_A = User(
    email='quarantine_partner@kcl.ac.uk')._asdict()
USER_WITH_NO_NOTIFICATIONS = User(email='covid@kcl.ac.uk')._asdict()
NONEXISTANT_USER_EMAIL = 'does@exist.not'
INVALID_EMAIL = 'invalidateme.now'
