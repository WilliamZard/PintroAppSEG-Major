# TODO: seperate testing and production database creation logic. Right now it's all in neo4j_ops, which is bad.
from ast import literal_eval
import json
import pytest
from flask.json import jsonify
from .generate_test_data import User

from .conftest import app, populate_db
from .generate_test_data import (INVALID_USER_TO_BE_CREATED,
                                 VALID_USER,
                                 VALID_USER_TO_BE_CREATED,
                                 VALID_USER_TO_BE_DELETED,
                                 VALID_USER_TO_BE_UPDATED,
                                 VALID_USER_TO_BE_UPDATED_NEW_FIELDS,
                                 USER_WITH_THREE_FOLLOWINGS,
                                 USER_WITH_TWO_FOLLOWINGS,
                                 USER_WITH_ONE_FOLLOWING,
                                 USER_WITH_NO_FOLLOWINGS, USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS,
                                 USER_POST_A, USER_POST_B, AFFILIATION_REQUESTER_A, DEACTIVATED_USER, ACTIVATED_USER, USER_THAT_POSTED_POST_A, USER_THAT_POSTED_POST_B)


@pytest.mark.GET_user
class TestGET:
    def test_GET_user_with_valid_email_that_exists(self, app, populate_db):
        valid_user = User(full_name='Duke Wellington',
                          email='duke@wellington.com')._asdict()
        # TODO: review how to handle tags at some point.
        valid_user.pop('passions')
        valid_user.pop('help_others')
        valid_user_node = {'properties': dict(valid_user), 'labels': 'Person'}
        populate_db(nodes_to_create=[valid_user_node])

        response = app.get(f"/users/{VALID_USER['email']}")
        assert response.status == '200 OK'
        json_response = json.loads(response.get_json())
        assert len(json_response) == len(VALID_USER)
        for key, value in VALID_USER.items():
            assert key in json_response
            assert value == json_response[key]

    def test_GET_user_with_valid_email_that_does_not_exist(self, app):
        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_GET_user_with_invalid_email(self, app):
        INVALID_EMAIL = 'invalidateme.now'
        response = app.get(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.DELETE_user
class TestDelete:
    # TODO: add tests for ensuring post nodes were deleted
    # TODO: add tests for ensuring all relationships were deleted
    def test_DELETE_user_with_valid_email_that_exists(self, app, populate_db):
        user = User(
            university='Gatwick Airpot', full_name='taaj', email='taaj@hotmail.co.uk')._asdict()
        # TODO: review how to handle tags at some point.
        user.pop('passions')
        user.pop('help_others')
        user_node = {'properties': dict(user), 'labels': 'Person'}
        populate_db(nodes_to_create=[user_node])

        response = app.delete(f"/users/{user['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        # Assert user was actually deleted in the database
        response = app.get(f"/users/{user['email']}")
        assert response.status == '404 NOT FOUND'

    def test_DELETE_user_with_valid_email_that_does_not_exist(self, app):
        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        response = app.delete(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_DELETE_user_with_invalid_email(self, app):
        INVALID_EMAIL = 'invalidateme.now'
        response = app.delete(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.PUT_user
class TestPut:
    def test_PUT_user_with_valid_email_that_exists(self, app, populate_db):
        user = User(
            full_name='Donald Trump', email='genius@fakenews.cnn')._asdict()
        # TODO: review how to handle tags at some point.
        user.pop('passions')
        user.pop('help_others')
        user_node = {'properties': dict(user), 'labels': 'Person'}
        populate_db(nodes_to_create=[user_node])

        new_user_fields = dict(
            profile_image='new_image', full_name='Donald Trump', gender='masculine',
            phone_number='999', short_bio='retired genius', location='Mar O Lago', job_title='Former Best President',
            preferred_name='GOAT'
        )

        email = user['email']
        response = app.put(
            f"/users/{email}", json=new_user_fields)
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        # TODO: complete these assertions.
        """
        response = app.get(f"/users/{email}")
        assert response.status == '200 OK'
        json = dict(response.get_json())
        print(json)
        assert len(json) == 13
        for key, value in VALID_USER_TO_BE_UPDATED_NEW_FIELDS.items():
            assert key in json
            assert value == json[key]"""

    def test_PUT_user_with_valid_email_that_does_not_exist(self, app):
        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        new_user_fields = dict(
            phone_number='999', short_bio='retired genius', location='Mar O Lago', job_title='Former Best President',
        )
        response = app.put(
            f"/users/{NONEXISTANT_USER_EMAIL}", json=new_user_fields)
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_PUT_user_with_invalid_email(self, app):
        INVALID_EMAIL = 'invalidateme.now'
        new_user_fields = dict(
            phone_number='999', short_bio='retired genius', location='Mar O Lago', job_title='Former Best President',
        )

        response = app.put(
            f"/users/{INVALID_EMAIL}", json=new_user_fields)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

    # TODO: add test for validating payload


@pytest.mark.POST_user
class TestPost:
    def test_POST_user_with_valid_payload_that_does_not_exist(self, app):
        response = app.post(
            "/users/", json=VALID_USER_TO_BE_CREATED)
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert user was actually created in the database
        response = app.get(f"/users/{VALID_USER_TO_BE_CREATED['email']}")
        assert response.status == '200 OK'
        json = dict(response.get_json())
        assert len(json) == 14
        for key, value in VALID_USER_TO_BE_CREATED.items():
            assert key in json
            # TODO: remove need for below if statement
            # This is in place as the GET function for users needs work to return the correct tags data
            # Should be a dictionary like {tag1: tag1_labels, tag2: tag2_labels}
            if key != 'tags':
                assert value == json[key]

    def test_POST_user_with_valid_payload_that_exists(self, app):
        response = app.post(
            "/users/", json=VALID_USER_TO_BE_CREATED)
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_POST_user_with_invalid_payload(self, app):
        response = app.post(
            "/users/", json=INVALID_USER_TO_BE_CREATED)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'


@pytest.mark.GET_user_followers
class TestUsersGETFollowers:
    def test_GET_followers_of_existing_user(self, app):
        response = app.get(
            f"/users/{USER_WITH_ONE_FOLLOWING['email']}/followers")
        assert response.status == '200 OK'
        results = [{'full_name': user['full_name'], 'email': user['email']}
                   for user in [USER_WITH_TWO_FOLLOWINGS, USER_WITH_THREE_FOLLOWINGS]]
        assert response.data == jsonify(results).data

    def test_GET_followers_of_non_existing_user(self, app):
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}/followers")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_GET_followers_of_user_with_no_followers(self, app):
        raise NotImplementedError


@pytest.mark.GET_user_followings
class TestUsersGETFollowings:
    def test_GET_followings_of_existing_user(self, app):
        response = app.get(
            f"/users/{USER_WITH_TWO_FOLLOWINGS['email']}/followings")
        assert response.status == '200 OK'
        json = response.json
        user_with_one_following_reduced = {
            'full_name': USER_WITH_ONE_FOLLOWING['full_name'], 'email': USER_WITH_ONE_FOLLOWING['email']}
        user_with_no_followings_reduced = {
            'full_name': USER_WITH_NO_FOLLOWINGS['full_name'], 'email': USER_WITH_NO_FOLLOWINGS['email']}
        assert len(json) == 2
        assert user_with_one_following_reduced in json
        assert user_with_no_followings_reduced in json

    def test_GET_followings_of_non_existing_user(self, app):
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}/followings")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_GET_followings_of_user_with_no_followers(self, app):
        raise NotImplementedError


@pytest.mark.GET_user_followings_posts
class TestUsersGETFollowingsPosts:
    def test_GET_all_posts_of_all_followers(self, app):
        response = app.get(
            f"/users/{USER_WITH_FOLLOWINGS_THAT_HAVE_POSTS['email']}/followings/posts")
        assert response.status == '200 OK'
        json = response.get_json()
        USER_POST_A['email'] = USER_THAT_POSTED_POST_A['email']
        USER_POST_B['email'] = USER_THAT_POSTED_POST_B['email']
        assert len(json) == 2
        assert USER_POST_A in json
        assert USER_POST_B in json

    @pytest.mark.xfail
    def test_get_all_posts_of_all_followers_of_non_existing_user(self, app):
        raise NotImplementedError

    # TODO: consider tests at different cardinalities


@pytest.mark.PUT_user_activation
class TestUserPUTActivation:
    def test_PUT_deactivated_users(self, app):
        response = app.put(
            f"/users/deactivate/{DEACTIVATED_USER['email']}")
        assert response.status == '204 NO CONTENT'

    def test_PUT_activated_users(self, app):
        response = app.put(
            f"/users/activate/{ACTIVATED_USER['email']}")
        assert response.status == '204 NO CONTENT'
