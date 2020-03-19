# USERS
from collections import namedtuple
from .tags import COLES_TAG, KING_SLAYER_TAG
# TODO: what about using a dictionary to describe data needed for each test? Could give it some structure.

active = True

USERS_PROPERTIES = [
    'full_name', 'preferred_name', 'profile_image', 'short_bio', 'gender', 'story',
    'email', 'phone_number', 'job_title', 'current_company', 'years_in_industry',
    'Industry', 'previous_company', 'previous_company_year_finished', 'university',
    'university_year_finished', 'academic_Level', 'location', 'date_of_birth', 'passions',
    'help_others', 'active']
USER_DEFAULTS = [
    'Default Name', 'Defaulter', 'Default Image', 'Default Short Bio', 'Default Gender',
    'Default Story', 'default@default.com', 000, 'Default Job Title', 'Default Current Company',
    100, 'Default Industry', 'Default previous company', 10, 'Default University', 1812,
    'Default Academic Level', 'Default Location', '01/01/1812', [], [], 'True']

User = namedtuple('User', USERS_PROPERTIES, defaults=USER_DEFAULTS)

# TODO: fill in tags
VALID_USER_PASSIONS = []
VALID_USER_SKILLS = []
VALID_USER = User(full_name='Duke Wellington', email='duke@wellington.com',
                  passions=VALID_USER_PASSIONS, help_others=VALID_USER_SKILLS)._asdict()

VALID_USER_TO_BE_UPDATED = User(
    full_name='Donald Trump', email='genius@fakenews.cnn')._asdict()

VALID_USER_TO_BE_UPDATED_NEW_TAG_UUIDS = [COLES_TAG['uuid']]
VALID_USER_TO_BE_UPDATED_NEW_FIELDS = User(
    profile_image='new_image', full_name='Donald Trump', gender='masculine',
    phone_number='999', short_bio='retired genius', location='Mar O Lago', job_title='Former Best President',
    preferred_name='GOAT', help_others=VALID_USER_TO_BE_UPDATED_NEW_TAG_UUIDS
)._asdict()
VALID_USER_TO_BE_DELETED = User(
    university='Gatwick Airpot', full_name='taaj', email='taaj@hotmail.co.uk')._asdict()
VALID_USER_TO_BE_CREATED_TAGS = [COLES_TAG['uuid'], KING_SLAYER_TAG['uuid']]
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
