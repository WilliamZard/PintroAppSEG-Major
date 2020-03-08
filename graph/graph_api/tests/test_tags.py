import pytest

from .conftest import app
from flask.json import jsonify
from .generate_test_data import LABEL_TAG, LABEL_GOT, LABEL_KCL, KING_SLAYER, COLES, KING_SLAYER_LABELS, COLES_LABELS, TAG_PROPERTIES


@pytest.mark.GET_tags
class TestGET:
    def test_GET_tags_with_all_labels(self, app):
        payload = list(COLES_LABELS | KING_SLAYER_LABELS)
        response = app.get("/tags/", json=payload)
        tag_properties_not_in_response = 'created'
        expected_tags = [KING_SLAYER, COLES]
        expected_response_data = [
            {k: v for k, v in tag.items() if k not in tag_properties_not_in_response}
            for tag in expected_tags]
        assert response.status == "200 OK"
        assert response.data == jsonify(expected_response_data).data

    def test_GET_tags_without_specifying_labels(self, app):
        response = app.get("/tags/")
        assert response.status == "404 PAYLOAD MUST SPECIFIY TAG LABELS"
        assert response.data == b''
