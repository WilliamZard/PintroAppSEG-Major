# USERS
# TODO: what about using a dictionary to describe data needed for each test? Could give it some structure.
USERS_PROPERTIES = [
    "password",
    "profile_image",
    "education",
    "full_name",
    "gender",
    "phone",
    "short_bio",
    "location",
    "job_title",
    "preferred_name",
    "email",
    "story",
    "tags"]

VALID_USER_TAGS = {'GOT': ['King Slayer'], 'KCL': ['Space Explorer']}
VALID_USER = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'Duke Wellington', 'male', '911',
                                         'not godless', 'strand', 'Duke', 'Duke', 'not_ucl@kcl.ac.uk', 'What is GKT?', VALID_USER_TAGS]))
VALID_USER_TO_BE_UPDATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Home', 'DTrump', 'male?', '000',
                                                       'genius', 'whit house', 'Commander n sth', 'MrPres', 'genius@fakenews.cnn', 'Covfefe']))
VALID_USER_TO_BE_UPDATED_NEW_FIELDS = dict(zip(USERS_PROPERTIES, ['0000', 'new_image', 'Care Home', 'Donald Trump', 'masculine', '999',
                                                                  'retired genius', 'Mar O Lago', 'Former Best President', 'GOAT', 'genius@fakenews.cnn', 'revolutionary']))
VALID_USER_TO_BE_DELETED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'Taaj', 'man', '123',
                                                       'going places', 'Gatwick init', 'going places', 'Taaj', 'taaj@hotmail.co.uk', 'you get me?']))
VALID_USER_TO_BE_CREATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'precious', 'man', '111',
                                                       'best kiosk in town', 'Gatwickk', 'Precious', 'Precious', 'precious@gmail.com', 'Likeable and devout.']))

INVALID_USER_TO_BE_CREATED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Gatwick Airport', 'precious', 'man', '111',
                                                         'best kiosk in town', 'Gatwickk', 'Precious', 'Preciousest', 'preciousgmail.com', 'Likeable and devout.']))

USER_WITH_MULTIPLE_POSTS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'UCL', 'John', 'male', '111',
                                                       'I was a student', 'London', 'unemployed', 'Jonny', 'user_with_posts@gmail.com', 'eat, sleep, repeat.']))

USER_THAT_CREATES_POST = dict(zip(USERS_PROPERTIES, ['password', 'image', 'UCL', 'John', 'male', '111',
                                                     'I was a student', 'London', 'unemployed', 'Jonny', 'user_creates_post@gmail.com', 'eat, sleep, repeat.']))
USER_ABOUT_TO_FOLLOW = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'King Wellington', 'male', '911',
                                                   'not godless', 'strand', 'no_ucl_King', 'no_ucl_King', 'no_ucl@kcl.ac.uk', 'What is GKT?']))
USER_ABOUT_TO_BE_FOLLOWED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'kcler', 'male', '911',
                                                        'not godless', 'strand', 'kclser_King', 'kclser_King', 'kclser@kcl.ac.uk', 'What is GKT?']))
USER_FOLLOWING = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'King Wellington', 'male', '911',
                                             'not godless', 'strand', 'very_creative_King', 'very_createive_King', 'creative_email@kcl.ac.uk', 'What is GKT?']))

USER_BEING_FOLLOWED = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'King Wellington', 'male', '911',
                                                  'not godless', 'strand', 'creative_King', 'creative_King', 'very_creative_email@kcl.ac.uk', 'What is GKT?']))
USER_WITH_THREE_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'High School', 'Duke Wellington', 'male', '911',
                                                         'not godless', 'strand', 'Duke', 'Dukee', 'yes_ucl@kcl.ac.uk', 'What is GKT?']))
USER_WITH_TWO_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Bachelors', 'Leonardo Di Caprio', 'male', '000',
                                                       'I am the MVP', 'US', 'Actor', 'Lello', 'lello@gmail.com', 'I won a best movie award']))
USER_WITH_ONE_FOLLOWING = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Secondary school', 'John Jonny', 'male', '111',
                                                      'I am millionaire', 'London', 'Entrepreneur', 'Sweety', 'jj@gmail.com', 'I started as a taxi driver.']))
USER_WITH_NO_FOLLOWINGS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Diploma', 'John Kennedy', 'male', '121',
                                                      'The only one pres', 'Unknown', 'Retired', 'JFK', 'jfk@gmail.com', 'They thought they killed me.']))
USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Winter', 'John Snow', 'male', '121',
                                                                   'King of the noorth', 'Unknown', 'Up and coming', 'Snowy', 'john.snow@winteriscoming.wes', 'ay']))
USER_THAT_POSTED_POST_A = dict(zip(USERS_PROPERTIES, ['password', 'image', 'Winter', 'James Bond', 'male', '007',
                                                      'James, James Bond', 'Unknown', 'Up and coming', 'Shaken', 'james.bond@mi5.co.uk', 'Yessir']))
USER_THAT_POSTED_POST_B = dict(zip(USERS_PROPERTIES, ['password', 'image', 'UK', 'M', 'female', '121',
                                                      'Siberia', 'Unknown', 'Up and coming', 'Queen_of_numbers', 'm@m.co.uk', 'shut it 007']))

NONEXISTANT_USER_EMAIL = 'does@exist.not'
INVALID_EMAIL = 'invalidateme.now'
