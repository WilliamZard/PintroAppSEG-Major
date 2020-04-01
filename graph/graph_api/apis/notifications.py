from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from flask import make_response
from .neo4j_ops import create_session, get_notifications
from .request import REQUEST_RELATIONSHIPS
from flask.json import jsonify

REVERSED_REQUEST_RELATIONSHIPS = {
    value: key for key, value in REQUEST_RELATIONSHIPS.items()}

api = Namespace('notifications',
                title='Endpoint for operation on notifications.')

notifications = api.model('Notification', {
    'requster_email': restx_fields.String(),
    'recipient_email': restx_fields.String(),
    'relationship_type': restx_fields.String(),
    'created_at': restx_fields.Float(),
})


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

            data.sort(key=lambda n: n['created_at'] * -1)
            return jsonify(data)
        return make_response('', 400)
