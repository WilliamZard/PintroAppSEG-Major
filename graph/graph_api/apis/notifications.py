from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from flask import make_response
from .neo4j_ops import create_session, get_notifications
from .request import REQUEST_RELATIONSHIPS

REVERSED_REQUEST_RELATIONSHIPS = {
    value: key for key, value in REQUEST_RELATIONSHIPS.items()}

api = Namespace('notifications',
                title='Endpoint for operation on notifications.')


class NotificationSchema(Schema):
    requester_email = fields.Email()
    recipient_email = fields.Email()
    relationship_type = fields.Str()


notifications = api.model('Notification', {
    'requster_email': restx_fields.String(),
    'recipient_email': restx_fields.String(),
    'relationship_type': restx_fields.String(),
})

notifications_schema = NotificationSchema()


@api.route('/<string:user_email>')
@api.produces('application/json')
class Notifications(Resource):
    def get(self, user_email):
        '''Get all notification of the given user.'''

        with create_session() as session:
            response = session.read_transaction(get_notifications, user_email)
            if response:
                data = [{key: REVERSED_REQUEST_RELATIONSHIPS[notification[key]] if notification[key] in REVERSED_REQUEST_RELATIONSHIPS else notification[key] for key in notification}
                        for notification in response.data()]
                return notifications_schema.dump(data, many=True)
            return make_response('', 400)
