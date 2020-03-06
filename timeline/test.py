from main import generate_timeline
from unittest.mock import Mock
import unittest


class TestFunction(unittest.TestCase):
    def test_generate_timeline_returns_correct_version(self):
        print("here")
        email = 'john.snow@winteriscoming.wes'
        data = {'email': email}
        req = Mock(get_json=Mock(return_value=data), args=data)

        expected_data = [
            {"content": "second_post", "modified": "2020-03-05T21:41:42.000000000Z",
                "uuid": "1066d651-0f2e-4a4d-84c4-093b88558685"},
            {"content": "Post B Content", "modified": "2020-03-05T21:38:49.632236000Z",
                "uuid": "5c7dd8ac-7ff4-44b0-aedb-de9ecd1e1086"},
            {"content": "Post A Content", "modified": "2020-03-05T21:38:49.632236000Z",
                "uuid": "3575c639-5b63-4e02-a959-f13051b855ff"}
        ]
        self.assertEqual(generate_timeline(req), expected_data)

# TODO: test for invalid email


if __name__ == "__main__":
    unittest.main()
