import json

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from app import create_app
from apis.users import *


spec = APISpec(
    title="Piintro's Graph API",
    version='0.1',
    openapi_version='3.0.2',
    info=dict(
        description='You know, for devs'
    ),
    plugins=[MarshmallowPlugin(), FlaskPlugin()]
)

spec.components.schema('Users', schema=UserSchema)

# We need a working context for apispec introspection.
app = create_app()

with app.test_request_context():
    spec.path(view=get_user)
    spec.path(view=delete_user)

# We're good to go! Save this to a file for now.
with open('swagger.json', 'w') as f:
    json.dump(spec.to_dict(), f)

with open('swagger.yaml', 'w') as f:  # TODO: no need for json.dump here
    json.dump(spec.to_yaml(), f)
