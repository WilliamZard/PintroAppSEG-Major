from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (
    create_session, create_follow_relationship, delete_follow_relationship)


api = Namespace(
    'follow', title='Operations related to the FOLLOW relationship')


@api.route('/request/<string:follow_requester>/<string:follow_request_recipient>')
@api.produces('application/json')
class FollowRequest(Resource):
    def post(self, follow_requester, follow_request_recipient):
        '''Create a FOLLOW_REQUEST relationship, where follow_requester has requested to follow follow_request_recipient.'''
        with create_session() as session:
            response = session.write_transaction(
                create_follow_relationship, follow_requester, follow_request_recipient)
            if response.summary().counters.relationships_created == 1:
                return make_response('', 201)
            return 400

    def delete(self, follower_email, following_email):
        '''Delete the FOLLOW relationship, where follower_email follows following_email'''
        with create_session() as session:
            response = session.write_transaction(
                delete_follow_relationship, follower_email, following_email)
            if response.summary().counters.relationships_deleted == 1:
                return make_response('', 204)
            return 400


"""
# TODO: consider url different structure. users/email/followings/posts
@api.route('/posts/<string:email>')
@api.produces('application/json')
class FollowingPosts(Resource):
    def get(self, email):
        '''Get all posts of all followings of a specific user.'''
        if not valid_email(email):
            return make_response('', 422)

        with create_session() as session:
            response = session.read_transaction(get_posts_for_timeline, email)
            posts = response.records()
            if posts:
                data = []
                for post in posts:
                    extracted_post = dict(post.data()['post'].items())
                    formatted_post = post_schema.dump(extracted_post)
                    data.append(formatted_post)
                # TODO: check correct response code here
                return data
            return make_response('', 404)
"""
