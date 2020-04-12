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
    "tags",
    "date_founded",
    "company_size",
    "funding",
    "team_members",
    "seeking_investment",
    "currently_hiring"
]
BUSINESS_DEFAULTS = [
    "Default Password",
    "",
    "Default Full Name",
    "Default Phone",
    "Default Short Bio",
    "Default Location",
    "Default Email",
    "Default Story",
    [],
    "Default Date Founded",
    "Default Company Size",
    "Default Funding",
    [],
    "Default Seeking Investment",
    "Default Currently Hiring",
]

Business = namedtuple('Business', BUSINESS_PROPERTIES,
                      defaults=BUSINESS_DEFAULTS)
