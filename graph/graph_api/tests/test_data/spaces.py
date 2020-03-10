# SPACES
# TODO: what about using a dictionary to describe data needed for each test? Could give it some structure.
SPACE_PROPERTIES = [
    "password",
    "profile_image",
    "full_name",
    "phone",
    "short_bio",
    "location",
    "email"]

VALID_SPACE = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'Sara_A_Lovelace', '911',
                                         'not godless','strand','nothing_ucl@kcl.ac.uk','What is GKT?']))

VALID_SPACE_TO_BE_UPDATED = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'aDTrump', '000',
                                                       'genius', 'white house', 'geniusds@fakenews.cnn', 'Covfefe']))
VALID_SPACE_TO_BE_UPDATED_NEW_FIELDS = dict(zip(SPACE_PROPERTIES, ['0000', 'new_image', 'aaDonaldTrump', '999',
                                                                  'retired genius', 'Mar O Lago', 'genisdus@fakenews.cnn', 'revolutionary']))
VALID_SPACE_TO_BE_DELETED = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'Taajad', '123',
                                                       'going places', 'Gatwick inits', 'taajsd@hotmail.co.uk', 'you get me?']))
VALID_SPACE_TO_BE_CREATED = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'Precious', '111',
                                                       'best kiosk in town', 'Gatwickk', 'preciousdfv@gmail.com', 'Likeable and devout.']))

INVALID_SPACE_TO_BE_CREATED = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'precisdadous', '111',
                                                         'best kiosk in town', 'Gatwickk', 'preciousJHGtvvgmail.com', 'Likeable and devout.']))

SPACE_WITH_MULTIPLE_POSTS = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'John12',  '111',
                                                       'I was a student', 'London', 'user_with_postsfvg@gmail.com', 'eat, sleep, repeat.']))

SPACE_THAT_CREATES_POST = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'John145', '111',
                                                     'I was a student', 'London', 'user_creates_posdfbt@gmail.com', 'eat, sleep, repeat.']))

SPACE_ABOUT_TO_FOLLOW = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'KingtfsjWellington', '911',
                                                   'not godless', 'strand', 'no_ucdfvl@kcl.ac.uk', 'What is GKT?']))

SPACE_ABOUT_TO_BE_FOLLOWED = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'kdfsgcler', '911',
                                                        'not godless', 'strand', 'kclserdfv@kcl.ac.uk', 'What is GKT?']))

SPACE_FOLLOWING = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'KingWellingtonadda', '911',
                                             'not godless', 'strand','creative_emadfvil@kcl.ac.uk', 'What is GKT?']))

SPACE_BEING_FOLLOWED = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'KingasafWellingtonbbb', '911',
                                                  'not godless', 'strand', 'very_creativfvfve_email@kcl.ac.uk', 'What is GKT?']))

SPACE_WITH_THREE_FOLLOWINGS = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'assddDukeWellingtona', '911',
                                                         'not godless', 'strand', 'yesthing_ucl@kcl.ac.uk', 'What is GKT?']))

SPACE_WITH_TWO_FOLLOWINGS = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'LeonardoasffDiCaprio', '000',
                                                       'I am the MVP', 'US', 'lellodvrtv@gmail.com', 'I won a best movie award']))

SPACE_WITH_ONE_FOLLOWING = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'JohnJonnyaaatrre', '111',
                                                      'I am millionaire', 'London', 'jjevrv@gmail.com', 'I started as a taxi driver.']))

SPACE_WITH_NO_FOLLOWINGS = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'JohnKennedygkdsafgff', '121',
                                                      'The only one pres', 'Unknown', 'jfrbrgbk@gmail.com', 'They thought they killed me.']))

SPACE_WITH_FOLLOWINGS_THAT_HAVE_POSTS = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'JohnSnfgghow', '121',
                                                                   'King of the noorth', 'Unknown', 'john.snorbrbw@winteriscoming.wes', 'ay']))

SPACE_THAT_POSTED_POST_A = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'JamesBondffdn', '007',
                                                      'James, James Bond', 'Unknown', 'james.bondrbbrb@mi5.co.uk', 'Yessir']))

SPACE_THAT_POSTED_POST_B = dict(zip(SPACE_PROPERTIES, ['password', 'image', 'Mgfhbfgfv', '121',
                                                      'Siberia', 'Unknown','m@mdfr.co.uk', 'shut it 007']))

NONEXISTANT_SPACE_EMAIL = 'does@exist.not'
INVALID_EMAIL = 'invalidateme.now'
