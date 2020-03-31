import uuid
import json
from ast import literal_eval

import pytest

from .conftest import app, populate_db
from .generate_test_data import User, basic_user_node, Post, basic_post_node


@pytest.mark.GET_user
class TestGET:
    def test_GET_user_with_valid_email_that_exists(self, app, populate_db):
        # Generate test data
        valid_user = User(full_name='Duke Wellington',
                          email='duke@wellington.com')._asdict()
        # TODO: review how to handle tags at some point.
        valid_user.pop('passions')
        valid_user.pop('help_others')
        valid_user_node = {'properties': dict(valid_user), 'labels': 'Person'}
        populate_db(nodes_to_create=[valid_user_node])

        # Test
        response = app.get(f"/users/{valid_user['email']}")
        assert response.status == '200 OK'
        json_response = response.get_json()
        assert len(json_response) == len(valid_user)
        for key, value in valid_user.items():
            assert key in json_response
            assert value == json_response[key]

    def test_GET_user_with_valid_email_that_does_not_exist(self, app, populate_db):
        populate_db()

        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_GET_user_with_invalid_email(self, app, populate_db):
        populate_db()

        INVALID_EMAIL = 'invalidateme.now'
        response = app.get(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.DELETE_user
class TestDelete:
    # TODO: add tests for ensuring post nodes were deleted
    # TODO: add tests for ensuring all relationships were deleted
    def test_DELETE_user_with_valid_email_that_exists(self, app, populate_db):
        # Generate test data
        user = User(
            university='Gatwick Airpot', full_name='taaj', email='taaj@hotmail.co.uk')._asdict()
        # TODO: review how to handle tags at some point.
        user.pop('passions')
        user.pop('help_others')
        user_node = {'properties': dict(user), 'labels': 'Person'}
        populate_db(nodes_to_create=[user_node])

        # Test
        response = app.delete(f"/users/{user['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        # Assert user was actually deleted in the database
        response = app.get(f"/users/{user['email']}")
        assert response.status == '404 NOT FOUND'

    def test_DELETE_user_with_valid_email_that_does_not_exist(self, app, populate_db):
        populate_db()

        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        response = app.delete(f"/users/{NONEXISTANT_USER_EMAIL}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_DELETE_user_with_invalid_email(self, app, populate_db):
        populate_db()

        INVALID_EMAIL = 'invalidateme.now'
        response = app.delete(f"/users/{INVALID_EMAIL}")
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''


@pytest.mark.PUT_user
class TestPut:
    def test_PUT_user_with_valid_email_that_exists(self, app, populate_db):
        # Generate Test Data
        user = User(
            full_name='Donald Trump', email='genius@fakenews.cnn')._asdict()
        # TODO: review how to handle tags at some point.
        user.pop('passions')
        user.pop('help_others')
        user_node = {'properties': dict(user), 'labels': 'Person'}
        populate_db(nodes_to_create=[user_node])

        # Test
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

    def test_PUT_user_with_valid_email_that_does_not_exist(self, app, populate_db):
        # Generate test data
        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        new_user_fields = dict(
            phone_number='999', short_bio='retired genius', location='Mar O Lago', job_title='Former Best President',
        )
        populate_db()

        # Test
        response = app.put(
            f"/users/{NONEXISTANT_USER_EMAIL}", json=new_user_fields)
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_PUT_user_with_invalid_email(self, app, populate_db):
        # Generate test data
        INVALID_EMAIL = 'invalidateme.now'
        new_user_fields = dict(
            phone_number='999', short_bio='retired genius', location='Mar O Lago', job_title='Former Best President',
        )
        populate_db()

        # Test
        response = app.put(
            f"/users/{INVALID_EMAIL}", json=new_user_fields)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b''

       # TODO: add test for validating payload


@pytest.mark.POST_user
class TestPost:
    # TODO: test creating a user with tag creation
    def test_POST_user_with_valid_payload_that_does_not_exist(self, app, populate_db):
        # Generate Test Data
        user = User(
            full_name='precious', email='precious@gmail.com')._asdict()
        user.pop('passions')
        user.pop('help_others')
        populate_db()

        # Test
        response = app.post(
            "/users/", json=dict(user))
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert user was actually created in the database
        response = app.get(f"/users/{user['email']}")
        assert response.status == '200 OK'
        response = json.loads(response.get_json())
        assert len(response) == len(user)
        for key, value in user.items():
            assert key in response
            assert value == response[key]

    def test_POST_user_with_valid_payload_that_exists(self, app, populate_db):
        # Generate Test Data
        user = User(
            full_name='precious', email='precious@gmail.com')._asdict()
        user.pop('passions')
        user.pop('help_others')
        user_node = {'properties': dict(user), 'labels': 'Person'}
        populate_db(nodes_to_create=[user_node])

        # Test
        response = app.post(
            "/users/", json=dict(user))
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_POST_user_with_invalid_payload(self, app, populate_db):
        # Generate Test Data
        INVALID_USER_TO_BE_CREATED = User(
            full_name='precious', email='praciousgmail.com')._asdict()
        populate_db()

        # Test
        response = app.post(
            "/users/", json=INVALID_USER_TO_BE_CREATED)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'


@pytest.mark.GET_user_followers
class TestUsersGETFollowers:
    def test_GET_followers_of_existing_user(self, app, populate_db):
        # Generate Test Data
        # Define users
        user_with_followers = User(email='jj@gmail.com')._asdict()
        user_with_followers.pop('passions')
        user_with_followers.pop('help_others')

        user_following_a = User(email='yes_ucl@kcl.ac.uk')._asdict()
        user_following_a.pop('passions')
        user_following_a.pop('help_others')

        user_following_b = User(email='lello@gmail.com')._asdict()
        user_following_b.pop('passions')
        user_following_b.pop('help_others')
        user_nodes = [{'properties': dict(user), 'labels': 'Person'} for user in [
            user_with_followers, user_following_a, user_following_b]]

        # Definge follow relationships
        follow_a = {
            's_node_properties': {'email': user_following_a['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': user_with_followers['email']}, 'e_node_labels': 'Person',
            'relationship_type': 'FOLLOWS'}

        follow_b = {
            's_node_properties': {'email': user_following_b['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': user_with_followers['email']}, 'e_node_labels': 'Person',
            'relationship_type': 'FOLLOWS'}

        populate_db(nodes_to_create=user_nodes,
                    relationships_to_create=[follow_a, follow_b])

        # Test
        response = app.get(
            f"/users/{user_with_followers['email']}/followers")
        assert response.status == '200 OK'
        results = [{'full_name': user['full_name'], 'email': user['email']}
                   for user in [user_following_a, user_following_b]]
        response = response.get_json()
        assert len(response) == len(results)
        for user in response:
            for key, value in user.items():
                assert key in user
                assert value in user[key]

    def test_GET_followers_of_non_existing_user(self, app, populate_db):
        populate_db()
        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}/followers")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_GET_followers_of_user_with_no_followers(self, app):
        raise NotImplementedError


@pytest.mark.GET_user_followings
class TestUsersGETFollowings:
    def test_GET_followings_of_existing_user(self, app, populate_db):
        # Generate Test Data
        # Define users
        user_with_followings = User(email='jj@gmail.com')._asdict()
        user_with_followings.pop('passions')
        user_with_followings.pop('help_others')

        user_being_followed_a = User(email='yes_ucl@kcl.ac.uk')._asdict()
        user_being_followed_a.pop('passions')
        user_being_followed_a.pop('help_others')

        user_being_followed_b = User(email='lello@gmail.com')._asdict()
        user_being_followed_b.pop('passions')
        user_being_followed_b.pop('help_others')
        user_nodes = [{'properties': dict(user), 'labels': 'Person'} for user in [
            user_with_followings, user_being_followed_a, user_being_followed_b]]

        # Definge follow relationships
        follow_a = {
            's_node_properties': {'email': user_with_followings['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': user_being_followed_a['email']}, 'e_node_labels': 'Person',
            'relationship_type': 'FOLLOWS'}

        follow_b = {
            's_node_properties': {'email': user_with_followings['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': user_being_followed_b['email']}, 'e_node_labels': 'Person',
            'relationship_type': 'FOLLOWS'}

        populate_db(nodes_to_create=user_nodes,
                    relationships_to_create=[follow_a, follow_b])

        # Test
        response = app.get(
            f"/users/{user_with_followings['email']}/followings")
        assert response.status == '200 OK'
        json = response.get_json()
        user_with_one_following_reduced = {
            'full_name': user_being_followed_a['full_name'], 'email': user_being_followed_a['email']}
        user_with_no_followings_reduced = {
            'full_name': user_being_followed_b['full_name'], 'email': user_being_followed_b['email']}
        assert len(json) == 2
        assert user_with_one_following_reduced in json
        assert user_with_no_followings_reduced in json

    def test_GET_followings_of_non_existing_user(self, app, populate_db):
        populate_db()

        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}/followings")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    @pytest.mark.xfail
    def test_GET_followings_of_user_with_no_followers(self, app):
        raise NotImplementedError


@pytest.mark.GET_user_followings_posts
class TestUsersGETFollowingsPosts:
    def test_GET_all_posts_of_all_followers(self, app, populate_db):
        # create three users
        # create two posts
        # have one user follow two others
        # have those two posted posts
        # Generate Test Data
        # Define users
        user_with_followings = User(email='jj@gmail.com')._asdict()
        user_with_followings.pop('passions')
        user_with_followings.pop('help_others')

        user_being_followed_a = User(email='yes_ucl@kcl.ac.uk')._asdict()
        user_being_followed_a.pop('passions')
        user_being_followed_a.pop('help_others')

        user_being_followed_b = User(email='lello@gmail.com')._asdict()
        user_being_followed_b.pop('passions')
        user_being_followed_b.pop('help_others')
        user_nodes = list(map(basic_user_node, [
                          user_with_followings, user_being_followed_a, user_being_followed_b]))
        post_a_uuid = str(uuid.uuid4())
        post_a = Post(content='post a', uuid=post_a_uuid)._asdict()
        post_b_uuid = str(uuid.uuid4())
        post_b = Post(content='post b', uuid=post_b_uuid)._asdict()
        post_a_node = basic_post_node(post_a)
        post_b_node = basic_post_node(post_b)

        # Define follow relationships
        follow_a = {
            's_node_properties': {'email': user_with_followings['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': user_being_followed_a['email']}, 'e_node_labels': 'Person',
            'relationship_type': 'FOLLOWS'}

        follow_b = {
            's_node_properties': {'email': user_with_followings['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'email': user_being_followed_b['email']}, 'e_node_labels': 'Person',
            'relationship_type': 'FOLLOWS'}

        # Define post relationships
        posted_a = {
            's_node_properties': {'email': user_being_followed_a['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'uuid': post_a['uuid']}, 'e_node_labels': 'Post',
            'relationship_type': 'POSTED'}

        posted_b = {
            's_node_properties': {'email': user_being_followed_b['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'uuid': post_b['uuid']}, 'e_node_labels': 'Post',
            'relationship_type': 'POSTED'}

        populate_db(nodes_to_create=user_nodes+[post_a_node, post_b_node], relationships_to_create=[
            follow_a, follow_b, posted_a, posted_b
        ])

        response = app.get(
            f"/users/{user_with_followings['email']}/followings/posts")
        assert response.status == '200 OK'
        json = response.get_json()
        user_post_a = {'content': post_a['content'],
                       'modified': post_a['modified'],
                       'user_email': user_being_followed_a['email']}
        user_post_b = {'content': post_b['content'],
                       'modified': post_b['modified'],
                       'user_email': user_being_followed_b['email']}
        print(json)
        assert len(json) == 2
        assert user_post_a in json
        assert user_post_b in json

    @pytest.mark.xfail
    def test_get_all_posts_of_all_followers_of_non_existing_user(self, app):
        raise NotImplementedError

    # TODO: consider tests at different cardinalities


@pytest.mark.PUT_user_activation
class TestUserPUTActivation:
    def test_PUT_deactivated_users(self, app, populate_db):
        user = User(email='user@test.com', active='True')._asdict()
        user_node = basic_user_node(user)
        populate_db(nodes_to_create=[user_node])

        response = app.put(
            f"/users/deactivate/{user['email']}")
        assert response.status == '204 NO CONTENT'

    def test_PUT_activated_users(self, app, populate_db):
        user = User(email='user@test.com', active='False')._asdict()
        user_node = basic_user_node(user)
        populate_db(nodes_to_create=[user_node])

        response = app.put(
            f"/users/activate/{user['email']}")
        assert response.status == '204 NO CONTENT'
