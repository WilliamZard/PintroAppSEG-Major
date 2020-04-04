from collections import namedtuple
SPACE_PROPERTIES = [
    "password",
    "profile_image",
    "full_name",
    "phone",
    "short_bio",
    "location",
    "email"]

SPACE_DEFAULTS = [
    "Default Password",
    "",
    "Default Full Name",
    "Default Phone",
    "Default Short Bio",
    "Default Location",
    "Default Email"]

Space = namedtuple('Space', SPACE_PROPERTIES, defaults=SPACE_DEFAULTS)
