from collections import namedtuple
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
    []
]

Business = namedtuple('Business', BUSINESS_PROPERTIES,
                      defaults=BUSINESS_DEFAULTS)
