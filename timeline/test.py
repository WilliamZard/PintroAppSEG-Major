import unittest

import requests

from main import generate_timeline
from unittest import mock
import json


posts = [{"content": "Post A Content", "modified": "2020-03-10T15:23:33.020296000Z",
          "uuid": "6566d860-d71f-4258-a222-7bb013086620"},
         {"content": "Post B Content", "modified": "2020-03-09T15:23:33.020296000Z",
          "uuid": "791a95b0-77f9-4ccb-940f-04cec294b05e"}]


def mocked_requests_get(url, headers):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
    if 'Authorization' not in headers:
        return MockResponse('{}', 401)
    if 'invalid_email' in url:
        return MockResponse('{}', 422)
    if 'does.not@exist.com' in url:
        return MockResponse('{}', 404)

    return MockResponse(json.dumps(posts), 200)


class TestFunction(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_generate_timeline_on_valid_and_existing_email(self, mock_get):
        mocked_request = mock.MagicMock()
        mocked_request.headers = {
            'Authorization': 'Bearer dummy_token'}
        email = 'john.snow@winteriscoming.wes'
        data = {'email': email}
        mocked_request.get_json = mock.Mock(return_value=data)

        response = json.loads(generate_timeline(mocked_request))

        self.assertEqual(len(response), 1)
        results = response['results']
        self.assertEqual(len(results), len(posts))
        self.assertEqual(results[0], posts[0])
        self.assertEqual(results[1], posts[1])

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_generate_timeline_on_non_existing_email(self, mock_get):
        mocked_request = mock.MagicMock()
        mocked_request.headers = {
            'Authorization': 'Bearer dummy_token'}
        email = 'does.not@exist.com'
        data = {'email': email}
        mocked_request.get_json = mock.Mock(return_value=data)

        response = generate_timeline(mocked_request)
        expected_data = "404 USER NOT FOUND"
        self.assertEqual(response, expected_data)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_generate_timeline_on_invalid_email(self, mock_get):
        mocked_request = mock.MagicMock()
        mocked_request.headers = {
            'Authorization': 'Bearer dummy_token'}
        email = 'invalid_email'
        data = {'email': email}
        mocked_request.get_json = mock.Mock(return_value=data)

        response = generate_timeline(mocked_request)

        expected_data = "422 INVALID EMAIL"
        self.assertEqual(response, expected_data)


if __name__ == "__main__":
    unittest.main()
