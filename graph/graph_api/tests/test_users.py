import uuid
import json
from ast import literal_eval
import base64
from pathlib import Path

import pytest

from .conftest import app, populate_db
from .generate_test_data import User, basic_user_node, Post, basic_post_node, Tag, Chatroom, basic_chatroom_node
from graph_api.apis.image_storing import *


@pytest.mark.GET_user
class TestGET:
    def test_GET_user_with_valid_email_that_exists(self, app, populate_db):
        # Generate test data
        tag_a = Tag(name='King Slaying')._asdict()
        tag_a_node = {'properties': tag_a, 'labels': ['Tag', 'Skill']}

        valid_user = User(full_name='Duke Wellington',
                          email='duke@wellington.com', help_others=[tag_a['name']])._asdict()
        valid_user_node = {'properties': dict(valid_user), 'labels': 'Person'}

        # Define relationships
        tagged_a = {
            's_node_properties': {'email': valid_user['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'name': tag_a['name']}, 'e_node_labels': 'Tag',
            'relationship_type': 'TAGGED'}

        populate_db(nodes_to_create=[valid_user_node, tag_a_node],
                    relationships_to_create=[tagged_a])

        # Test
        response = app.get(f"/users/{valid_user['email']}")
        assert response.status == '200 OK'
        response = response.get_json()
        assert len(response) == len(valid_user)
        for key, value in valid_user.items():
            assert key in response
            assert value == response[key]

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

    def test_GET_user_with_profile_image_has_the_right_image_stored_in_gcs(self, app, populate_db):
        # Generate test data
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image3.jpg"
        with image_path.open(mode="rb") as imageFile:
            image = base64.b64encode(imageFile.read())

        user = User(profile_image=image)._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}

        populate_db(nodes_to_create=[user_node])

        # Test
        response = app.get(f"/users/{user['email']}")
        assert response.status == '200 OK'
        response = response.get_json()
        assert literal_eval(response['profile_image']) == image


@pytest.mark.DELETE_user
class TestDelete:
    # TODO: add tests for ensuring post nodes were deleted
    # TODO: add tests for ensuring all relationships were deleted
    def test_DELETE_user_with_valid_email_that_exists(self, app, populate_db):
        # Generate test data
        user = User(
            university='Gatwick Airpot', full_name='taaj', email='taaj@hotmail.co.uk')._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}
        populate_db(nodes_to_create=[user_node])

        # Test
        response = app.delete(f"/users/{user['email']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        # Assert user was actually deleted in the database
        response = app.get(f"/users/{user['email']}")
        assert response.status == '404 NOT FOUND'
        # TODO: add test to ensure all tagged relationships where deleted.

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

    def test_DELETE_user_with_set_profile_image(self, app, populate_db):
        # Generate test data
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image2.jpg"
        with image_path.open(mode="rb") as imageFile:
            new_image = base64.b64encode(imageFile.read())

        user = User(email='user_to_delete@gmail.com',
                    profile_image=new_image)._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}

        populate_db(nodes_to_create=[user_node])

        image_url = user['profile_image']

        # Test
        response = app.delete(f"/users/{user['email']}")
        assert response.status == '204 NO CONTENT'
        assert get_data_from_gcs(image_url) == ''


@pytest.mark.PUT_user
class TestPut:
    def test_PUT_user_with_valid_email_that_exists(self, app, populate_db):
        # Generate Test Data
        tag_a = Tag(name='King Slayer')._asdict()
        tag_a_node = {'properties': tag_a, 'labels': ['Tag', 'CanHelpWithTag']}
        tag_b = Tag(name='New King Slayer')._asdict()
        tag_b_node = {'properties': tag_b, 'labels': ['Tag', 'CanHelpWithTag']}

        user = User()._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}

        # Define relationships
        tagged_a = {
            's_node_properties': {'email': user['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'name': tag_a['name']}, 'e_node_labels': 'Tag',
            'relationship_type': 'TAGGED'}

        populate_db(nodes_to_create=[user_node, tag_a_node, tag_b_node],
                    relationships_to_create=[tagged_a])

        # Test
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image1.jpg"
        with image_path.open(mode="rb") as imageFile:
            new_image = base64.b64encode(imageFile.read())

        new_user_fields = dict(
            profile_image=str(new_image), full_name='Donald Trump', gender='masculine',
            phone_number='999', short_bio='retired genius', location='Mar O Lago', job_title='Former Best President',
            preferred_name='GOAT', help_others=[tag_b['name']]
        )
        email = user['email']
        response = app.put(
            f"/users/{email}", json=new_user_fields)
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

        # TODO: complete these assertions.

        response = app.get(f"/users/{email}")
        assert response.status == '200 OK'
        response = response.get_json()
        user = User(**new_user_fields
                    )._asdict()
        assert len(response) == len(user)
        for key, value in user.items():
            assert key in response
            if(key == 'profile_image'):
                # Check that image bytes are the equal.
                assert new_image == literal_eval(response[key])
                continue
            assert value == response[key]

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
        tag_a = Tag(name='King Slaying')._asdict()
        tag_a_node = {'properties': tag_a, 'labels': ['Tag', 'CanHelpWithTag']}
        user = User(
            full_name='precious', email='precious@gmail.com', help_others=[tag_a['name']])._asdict()
        populate_db(nodes_to_create=[tag_a_node])

        # Test
        response = app.post(
            "/users/", json=dict(user))
        assert response.status == '201 CREATED'
        assert response.data == b''

        # Assert user was actually created in the database
        response = app.get(f"/users/{user['email']}")
        assert response.status == '200 OK'
        response = response.get_json()
        assert len(response) == len(user)
        for key, value in user.items():
            assert key in response
            assert value == response[key]

    def test_POST_user_with_valid_payload_that_exists(self, app, populate_db):
        # Generate Test Data
        user = User(
            full_name='precious', email='precious@gmail.com')._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}
        populate_db(nodes_to_create=[user_node])

        # Test
        response = app.post(
            "/users/", json=dict(user))
        assert response.status == '409 CONFLICT'
        assert response.data == b'Node with that email already exists.'

    def test_POST_user_with_invalid_payload(self, app):
        # Generate Test Data
        INVALID_USER_TO_BE_CREATED = User(
            full_name='precious', email='praciousgmail.com')._asdict()

        # Test
        response = app.post(
            "/users/", json=INVALID_USER_TO_BE_CREATED)
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Not a valid email address.'

    def test_POST_user_with_image_posts_correct_image_in_gcs(self, app, populate_db):
        # Generate Test Data
        image_path = Path(__file__).parent / \
            "test_data/profile_images/profile_image3.jpg"
        with image_path.open(mode="rb") as imageFile:
            image = base64.b64encode(imageFile.read())

        user_to_add = User(profile_image=str(image))._asdict()

        populate_db()

        # Test
        response = app.post("/users/", json=user_to_add)
        assert response.status == '201 CREATED'
        response = app.get(f"/users/{user_to_add['email']}")
        response = response.get_json()
        assert image == literal_eval(response['profile_image'])


@pytest.mark.GET_user_followers
class TestUsersGETFollowers:
    def test_GET_followers_of_existing_user(self, app, populate_db):
        # Generate Test Data
        # Define users
        user_with_followers = User(email='jj@gmail.com')._asdict()

        user_following_a = User(email='yes_ucl@kcl.ac.uk')._asdict()

        user_following_b = User(email='lello@gmail.com')._asdict()
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

    def test_GET_followers_of_non_existing_user(self, app):
        NONEXISTANT_USER_EMAIL = 'does@exist.not'
        response = app.get(f"/users/{NONEXISTANT_USER_EMAIL}/followers")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_GET_followers_of_user_with_no_followers(self, app, populate_db):
        user = User(email='jj@gmail.com')._asdict()
        user_node = basic_user_node(user)
        populate_db(nodes_to_create=[user_node])

        response = app.get(f"/users/{user['email']}/followers")
        assert response.status == '200 OK'
        assert not response.get_json()


@pytest.mark.GET_user_followings
class TestUsersGETFollowings:
    def test_GET_followings_of_existing_user(self, app, populate_db):
        # Generate Test Data
        # Define users
        user_with_followings = User(email='jj@gmail.com')._asdict()

        user_being_followed_a = User(email='yes_ucl@kcl.ac.uk')._asdict()

        user_being_followed_b = User(email='lello@gmail.com')._asdict()
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
        # Generate Test Data
        # Define users
        user_with_followings = User(email='jj@gmail.com')._asdict()

        user_being_followed_a = User(email='yes_ucl@kcl.ac.uk')._asdict()

        user_being_followed_b = User(email='lello@gmail.com')._asdict()
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
                       'created': post_a['created'],
                       'uuid': post_a['uuid'],
                       'user_email': user_being_followed_a['email']}
        user_post_b = {'content': post_b['content'],
                       'modified': post_b['modified'],
                       'created': post_b['created'],
                       'uuid': post_b['uuid'],
                       'user_email': user_being_followed_b['email']}
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


@pytest.mark.GET_user_chatrooms
class TestGET:
    def test_GET_chatrooms_for_users_that_exist(self, app, populate_db):
        # Generate Data
        users = [
            User(email='user1@test.com')._asdict(),
            User(email='user2@test.com')._asdict(),
            User(email='user3@test.com')._asdict(),
            User(email='user4@test.com')._asdict(),
        ]
        chatrooms = [
            Chatroom()._asdict(),
            Chatroom()._asdict(),
        ]

        # Relationships
        userA_chatroomA = {
            's_node_properties': {'email': users[0]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[0]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        userB_chatroomA = {
            's_node_properties': {'email': users[1]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[0]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        userA_chatroomB = {
            's_node_properties': {'email': users[0]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[1]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }
        userC_chatroomB = {
            's_node_properties': {'email': users[2]['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'chat_id': chatrooms[1]['chat_id']}, 'e_node_labels': 'Chatroom',
            'relationship_type': 'CHATS_IN'
        }

        populate_db(
            nodes_to_create=list(map(basic_user_node, users)) +
            list(map(basic_chatroom_node, chatrooms)),
            relationships_to_create=[
                userA_chatroomA, userB_chatroomA, userA_chatroomB, userC_chatroomB]
        )

        response = app.get(f"/users/{users[0]['email']}/chatrooms")
        assert response.status == '200 OK'
        # the order of chatrooms is arbitrary and sorted by the frontend,
        # so turning it into a set allows orderless checking of the data inside
        json = response.get_json()
        assert len(json) == 2
        assert {"chat_id": str(chatrooms[0]['chat_id']),
                "recipient": users[1]['email']} in json
        assert {"chat_id": str(chatrooms[1]['chat_id']),
                "recipient": users[2]['email']} in json

        response = app.get(f"/users/{users[1]['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": str(chatrooms[0]['chat_id']),
                "recipient": users[0]['email']} in json

        response = app.get(f"/users/{users[2]['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 1
        assert {"chat_id": str(chatrooms[1]['chat_id']),
                "recipient": users[0]['email']} in json

        response = app.get(f"/users/{users[3]['email']}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0

    def test_GET_chatrooms_for_user_that_does_not_exists(self, app, populate_db):
        populate_db()

        nonexistant_email = 'doesnotexist@test.com'
        response = app.get(f"/users/{nonexistant_email}/chatrooms")
        assert response.status == '200 OK'
        json = response.get_json()
        assert len(json) == 0
