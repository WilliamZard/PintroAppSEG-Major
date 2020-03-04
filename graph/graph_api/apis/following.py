from flask.json import jsonify
from flask import make_response
from flask_restx import Namespace, Resource
from flask_restx import fields as restx_fields
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from neo4j.exceptions import ConstraintError
from .utils import valid_email

from .neo4j_ops import (create_session, create_follow_relationship)


api = Namespace(
    'following', title='Operations related to the FOLLOW relationship')


@api.route('/<string:follower_email>/<string:following_email>')
class Following(Resource):
    def post(self, follower_email, following_email):
        with create_session() as session:
            response = session.write_transaction(
                create_follow_relationship, follower_email, following_email)
            if response.summary().counters.relationships_created == 1:
                return make_response('', 201)
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
