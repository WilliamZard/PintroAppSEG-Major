import pytest
import json

from .conftest import app
from flask.json import jsonify
from .generate_test_data import LABEL_TAG, LABEL_GOT, LABEL_KCL, KING_SLAYER, COLES, KING_SLAYER_LABELS, COLES_LABELS, TAG_PROPERTIES


@pytest.mark.POST_tags
class TestPOST:
    def test_POST_tags_with_all_labels(self, app):
        payload = {'labels': list(COLES_LABELS | KING_SLAYER_LABELS)}
        response = app.post("/tags/", json=payload)

        assert response.status == "200 OK"
        assert len(response.json) == 2
        assert COLES in response.json
        assert KING_SLAYER in response.json

    def test_POST_tags_without_specifying_labels(self, app):
        response = app.post("/tags/")
        # TODO: add more details in error message
        assert response.status == "400 BAD REQUEST"

    def test_POST_tags_with_invalid_labels(self, app):
        payload = {'labels': ['bad label']}
        response = app.post("/tags/", json=payload)

        assert response.status == "400 BAD REQUEST"
