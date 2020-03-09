from .users import *
from .spaces import *
from .businesses import *

VALID_MATCHING_NAME_OR_EMAIL_SEARCH ={
    'request':{
        "query" : "John"
    },
    'result' : [
        USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS,
        USER_WITH_ONE_FOLLOWING,
        USER_WITH_NO_FOLLOWINGS,
        USER_WITH_MULTIPLE_POSTS,
        BUSINESS_WITH_MULTIPLE_POSTS
    ]
} 


SINGLE_CHAR_SEARCH = {
    'request':{
        "query" : "c"
    },
    'result' : []
} 

EMPTY_STRING_SEARCH = {
    'request':{
        "query" : ""
    },
    'result' : []
}

UNMATHCING_SEARCH = {
    'request':{
        "query" : "kxwq"
    },
    'result' : []
}

MATCHING_STORY_OR_EVENTS_SEARCH = {
    'request':{
        "query" : "what is GKT"
    },
    'result' : [
        VALID_BUSINESS,
        BUSINESS_ABOUT_TO_BE_FOLLOWED,
        BUSINESS_WITH_THREE_FOLLOWINGS,
        BUSINESS_BEING_FOLLOWED,
        BUSINESS_ABOUT_TO_FOLLOW,
        BUSINESS_FOLLOWING,
        USER_FOLLOWING,
        USER_WITH_THREE_FOLLOWINGS,
        USER_ABOUT_TO_BE_FOLLOWED,
        USER_ABOUT_TO_FOLLOW,
        USER_BEING_FOLLOWED,
        VALID_USER
    ]
}


MATCHING_SHORT_BIO_SEARCH = {
    'request':{
        "query" : "not godless"
    },
    'result' : [
        SPACE_ABOUT_TO_BE_FOLLOWED,
        SPACE_BEING_FOLLOWED,
        SPACE_ABOUT_TO_FOLLOW,
        VALID_SPACE,
        SPACE_FOLLOWING,
        SPACE_WITH_THREE_FOLLOWINGS,
        VALID_BUSINESS,
        BUSINESS_ABOUT_TO_BE_FOLLOWED,
        BUSINESS_WITH_THREE_FOLLOWINGS,
        BUSINESS_BEING_FOLLOWED,
        BUSINESS_ABOUT_TO_FOLLOW,
        BUSINESS_FOLLOWING,
        USER_FOLLOWING,
        USER_WITH_THREE_FOLLOWINGS,
        USER_ABOUT_TO_BE_FOLLOWED,
        USER_ABOUT_TO_FOLLOW,
        USER_BEING_FOLLOWED,
        VALID_USER
    ]
}