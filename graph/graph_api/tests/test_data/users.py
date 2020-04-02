from collections import namedtuple
# TODO: what about using a dictionary to describe data needed for each test? Could give it some structure.

USERS_PROPERTIES = [
    'full_name', 'preferred_name', 'profile_image', 'short_bio', 'gender', 'story',
    'email', 'phone_number', 'job_title', 'current_company', 'years_in_industry',
    'industry', 'previous_company', 'previous_company_year_finished', 'university',
    'university_year_finished', 'academic_level', 'location', 'date_of_birth', 'passions',
    'help_others', 'active']
USER_DEFAULTS = [
    'Default Name', 'Defaulter', '', 'Default Short Bio', 'Default Gender',
    'Default Story', 'default@default.com', '000', 'Default Job Title', 'Default Current Company',
    '100', 'Default Industry', 'Default previous company', '10', 'Default University', '1812',
    'Default Academic Level', 'Default Location', '01/01/1812', [], [], 'True']

User = namedtuple('User', USERS_PROPERTIES, defaults=USER_DEFAULTS)
