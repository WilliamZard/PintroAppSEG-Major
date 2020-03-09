import pytest
import json

from .conftest import app
from flask.json import jsonify
from .generate_test_data import LABEL_TAG, LABEL_GOT, LABEL_KCL, KING_SLAYER, COLES, KING_SLAYER_LABELS, COLES_LABELS, TAG_PROPERTIES


@pytest.mark.GET_tags
class TestGET:
    def test_GET_tags_with_all_labels(self, app):
        payload = list(COLES_LABELS | KING_SLAYER_LABELS)
        response = app.get("/tags/", json=payload)

        assert response.status == "200 OK"
        assert len(response.json) == 2
        assert COLES in response.json
        assert KING_SLAYER in response.json

    @pytest.mark.xfail
    def test_GET_tags_without_specifying_labels(self, app):
        response = app.get("/tags/")
        assert response.status == "404 PAYLOAD MUST SPECIFIY TAG LABELS"
        assert response.data == b''

    # TODO: test for invalid and valid labels.
