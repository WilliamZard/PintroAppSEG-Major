import json

import pytest

from .conftest import app, populate_db
from .test_data.tags import Tag


@pytest.mark.POST_tags
class TestPOST:
    def test_POST_tags_with_all_labels(self, app, populate_db):
        tag_a = Tag(name='King Slayer')._asdict()
        tag_a_node = {'properties': tag_a, 'labels': ['Tag', 'Skill']}
        tag_b = Tag(name='King Slayer')._asdict()
        tag_b_node = {'properties': tag_b, 'labels': ['Tag', 'Passion']}

        populate_db(nodes_to_create=[tag_a_node, tag_b_node])

        # Just create tags
        payload = {'labels': list(
            set(tag_b_node['labels']) | set(tag_a_node['labels']))}
        response = app.post("/tags/", json=payload)

        assert response.status == "200 OK"
        response = response.get_json()
        assert len(response) == 2
        assert tag_a['name'] in response
        assert tag_a['name'] in response

    def test_POST_tags_without_specifying_labels(self, app, populate_db):
        populate_db()
        response = app.post("/tags/")
        assert response.status == "400 BAD REQUEST"

    def test_POST_tags_with_invalid_labels(self, app, populate_db):
        populate_db()
        payload = {'labels': ['bad label']}
        response = app.post("/tags/", json=payload)

        assert response.status == "400 BAD REQUEST"
