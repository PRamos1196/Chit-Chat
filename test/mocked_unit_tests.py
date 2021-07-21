'''
    mocked_unit_test.py

  This file tests for
  – These should extend unittest. TestCase and use the unittest mocking framework as discussed in Lecture 14
  – These shouldnot make any real API/DB/Socket calls, but instead mock out those out
  – These should tost code paths in your app and be unique to each other (as much as possible)
  – These tests should use a combination of asserts to test the business logic, including assertEqual, assertNotEqual
  assertRaise, and assertDictEqual (and any others that may be useful)
  – These should all be passing in your final commit'''
import unittest
import unittest.mock as mock
import sys
sys.path.append("/home/ec2-user/environment/project2-m2-par25")
import app

KEY_ID = "number"
KEY_INPUT = "data"
KEY_EXPECTED = "expected"
KEY_RESPONSE = "response"

class MockedAppTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_ID: 2,
                KEY_INPUT: {
                    'username': "pedro",
                    'message': "!!joke",
                    'url': 'https://avatarfiles.alphacoders.com/123/123561.png'
                },
              KEY_EXPECTED: "Why was the river rich?Because it had two banks."
            },
        ]
    
    def mocked_joke(self, q):
        mocked_request = mock.Mock()
        mocked_dict = {
                "error": False,
                "category": "Miscellaneous",
                "type": "twopart",
                "setup": "Why was the river rich?",
                "delivery": "Because it had two banks.",
                "flags": {
                    "nsfw": False,
                    "religious": False,
                    "political": False,
                    "racist": False,
                    "sexist": False
                 },
                "id": 184,
                "lang": "en"
        }
        mocked_request.json.return_value = mocked_dict
        return mocked_request
        
    def test_if_success(self):
        for test in self.success_test_params:
            if(test[KEY_ID] == 2):
                with mock.patch('requests.get', self.mocked_joke):
                    message = app.new_message_recieved(test[KEY_INPUT])
                    print(message)
                    expected = test[KEY_EXPECTED]
                self.assertEqual(message, expected)

            
if __name__ == '__main__':
    unittest.main()
       