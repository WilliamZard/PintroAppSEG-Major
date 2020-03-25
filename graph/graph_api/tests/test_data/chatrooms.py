from .users import User

CHATROOM_USERS = [
    User(email='email@email.com')._asdict(),
    User(email='email2@email.com')._asdict(),
    User(email='email3@email.com')._asdict(),
    User(email='email4@email.com')._asdict()
]
"""
    dict(zip(USERS_PROPERTIES, ['image', 'yes', 'mr a', 'female', '1234',
                                'Siberia', 'Unknown', 'chatter', 'CHATROOM_A', 'email@email.com', 'i sure love chatting'])),
    dict(zip(USERS_PROPERTIES, ['image', 'no', 'mr b', 'female', '2345',
                                'London', 'Unknown', 'student', 'CHATROOM_B', 'email2@email.com', 'talk very good'])),
    dict(zip(USERS_PROPERTIES, ['image', 'maybe', 'mr c', 'female', '3456',
                                'Algonquin', 'Unknown', 'homeless', 'CHATROOM_C', 'email3@email.com', 'i have no mouth'])),
    dict(zip(USERS_PROPERTIES, ['image', 'i dont know', 'mr d', 'female', '4567',
                                'Space', 'Unknown', 'homeless', 'CHATROOM_D', 'email4@email.com', 'aaaaaaa']))
]"""

CHATROOMS = [
    "CHATROOMID1",
    "CHATROOMID2"
]

NONEXISTANT_CHATROOM_ID = "I DO NOT EXIST"

VALID_CHATROOM_TO_BE_DELETED = "PLEASE DELETE ME"

VALID_CHATROOM_TO_BE_DELETED_USERS = [
    User(email='emai6@email.com')._asdict(),
    User(email='email32@email.com')._asdict()]
"""
    dict(zip(USERS_PROPERTIES, ['password', 'image', 'HFHFHF', 'mr e', 'female', '3754',
                                'New York', 'Unknown', 'CEO', 'CHATROOM_E', 'emai6@email.com', 'oh no'])),
    dict(zip(USERS_PROPERTIES, ['password', 'image', 'ASDASD', 'mr f', 'female', '982333',
                                'New York', 'Unknown', 'NEET', 'CHATROOM_F', 'email32@email.com', ':('])),
]"""

CHATROOM_TO_BE_CREATED_USERS = [
    User(email='noemail@email.com')._asdict(),
    User(email='yeseemail@email.com')._asdict()]
"""
    dict(zip(USERS_PROPERTIES, ['password', 'image', 'A NAME', 'mr g', 'female', '735333',
                                'The Moon', 'Unknown', 'none', 'CHATROOM_G', 'noemail@email.com', 'i want to talk'])),
    dict(zip(USERS_PROPERTIES, ['password', 'image', 'ANOTHER NAME', 'mr h', 'female', '43569235',
                                '????', 'Unknown', 'all', 'CHATROOM_H', 'yesemail@email.com', 'lets talk'])),
]"""
