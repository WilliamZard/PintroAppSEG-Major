import uuid

import pytest
from flask.json import jsonify
from flask import Flask

from .conftest import app, populate_db
from .test_data.posts import Post
from .test_data.users import User


@pytest.mark.GET_post
class TestGET:
    def test_GET_post_that_exists(self, app: Flask, populate_db: None) -> None:
        # Generate Test Data
        post = Post(content='content_x', hashtags="# tag_a #tag_b")._asdict()
        posts = [{'properties': dict(post), 'labels': 'Post'}]
        populate_db(nodes_to_create=posts)

        # Test
        response = app.get(f"/posts/{post['uuid']}")
        assert response.status == '200 OK'
        response = response.get_json()
        assert len(response) == len(post)
        for key, value in post.items():
            assert key in response
            # NOTE: conversion to string is a workaroud until proper handling of arrays in neo4j
            assert str(value) == response[key]

    def test_GET_post_that_does_not_exist(self, app):
        non_existing_uuid = uuid.uuid4()
        response = app.get(f"/posts/{non_existing_uuid}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''


@pytest.mark.PUT_post
class TestPUT:
    def test_PUT_existing_post(self, app: Flask, populate_db: None) -> None:
        # Generate Test Data
        post = Post(content='content_x', hashtags="#tag_a #tag_b")._asdict()
        new_post = Post(content='content_y', hashtags="#new_tag_a")._asdict()
        posts = [{'properties': dict(post), 'labels': 'Post'}]
        populate_db(nodes_to_create=posts)

        # Test
        response = app.put(
            f"/posts/{post['uuid']}", json={'content': new_post['content'], 'hashtags': new_post['hashtags']})
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

    def test_PUT_non_existent_post(self, app: Flask):
        post = Post(content='content_x', hashtags="#new_tag_a")._asdict()

        response = app.put(
            f"/posts/{uuid.uuid4()}", json={'content': post['content'], 'hashtags': post['hashtags']})
        assert response.status == '404 NOT FOUND'
        assert response.data == b''

    def test_PUT_existing_post_with_invalid_payload(self, app: Flask, populate_db: None) -> None:
        # Generate Test Data
        post = Post(content='content_x', hashtags="#tag_a #tag_b")._asdict()
        new_post = Post(content='', hashtags="#new_tag_a")._asdict()
        posts = [{'properties': dict(post), 'labels': 'Post'}]
        populate_db(nodes_to_create=posts)

        # Test
        response = app.put(
            f"/posts/{post['uuid']}", json={'content': new_post['content'], 'hashtags': new_post['hashtags']})
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Post content length must be between 1 and 300.'

        too_big_content = "a"*301
        new_post = Post(content=too_big_content,
                        hashtags="#new_tag_a")._asdict()
        response = app.put(
            f"/posts/{post['uuid']}", json={'content': new_post['content'], 'hashtags': new_post['hashtags']})
        assert response.status == '422 UNPROCESSABLE ENTITY'
        assert response.data == b'Post content length must be between 1 and 300.'


@pytest.mark.POST_post
class TestPOST:
    def test_POST_post_with_valid_payload(self, app: Flask, populate_db: None) -> None:
        # Generate Test Data
        post = Post(content='content_x', hashtags="#tag_a #tag_b"
                    )._asdict()
        user = User(email='created_post@post.com')._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}
        payload = {'content': post['content'],
                   'user_email': user['email'], 'hashtags': post['hashtags']}

        populate_db(nodes_to_create=[user_node])

        # Test
        response = app.post(
            "/posts/", json=payload)
        assert response.status == '201 CREATED'

    def test_POST_post_with_invalid_payload(self, app: Flask, populate_db: None) -> None:
        # Generate Test Data
        empty_post = Post(content='', hashtags="#tag_a #tag_b"
                          )._asdict()
        too_big_post = Post(content='a'*301, hashtags="#tag_a #tag_b"
                            )._asdict()
        user = User(email='created_post@post.com')._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}

        populate_db(nodes_to_create=[user_node])

        # Test
        payload = {'content': empty_post['content'],
                   'user_email': user['email'], 'hashtags': empty_post['hashtags']}
        response = app.post(
            "/posts/", json=payload)
        assert response.status == '422 UNPROCESSABLE ENTITY'

        payload = {'content': too_big_post['content'],
                   'user_email': user['email'], 'hashtags': empty_post['hashtags']}
        response = app.post(
            "/posts/", json=payload)
        assert response.status == '422 UNPROCESSABLE ENTITY'


@pytest.mark.DELETE_post
class TestDELETE:
    def test_DELETE_existing_post(self, app: Flask, populate_db: None) -> None:
        # Generate Test Data
        # Nodes
        post = Post(content='content_x', hashtags="#tag_a #tag_b")._asdict()
        post_node = {'properties': dict(post), 'labels': 'Post'}
        user = User(email='created_post@post.com')._asdict()
        user_node = {'properties': dict(user), 'labels': 'Person'}

        # Relationships
        posted = {
            's_node_properties': {'email': user['email']}, 's_node_labels': 'Person',
            'e_node_properties': {'uuid': post['uuid']}, 'e_node_labels': 'Post',
            'relationship_type': 'POSTED'}

        populate_db(nodes_to_create=[
                    user_node, post_node], relationships_to_create=[posted])

        # Test
        response = app.delete(
            f"/posts/{post['uuid']}")
        assert response.status == '204 NO CONTENT'
        assert response.data == b''

    def test_DELETE_non_existing_post(self, app: Flask):
        response = app.delete(
            f"/posts/{uuid.uuid4()}")
        assert response.status == '404 NOT FOUND'
        assert response.data == b''
