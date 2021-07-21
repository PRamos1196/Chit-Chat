"""
    unmocked_unit_tests.py
    
    This file tests for
    – These should extend unittest.TestCase
    – These should not start up a local Flask server nor test Socket.io functionality
    – These should test code paths in your app and be unique to each other
    – These tests should use a combination of asserts to test the business logic, including assertEqual, assertNotEqual,
      assertRaise, and assertDictEqual (and any others that may be useful)
    – These should all be passing in your final commit
"""
import unittest
import os
import sys
sys.path.append("/home/ec2-user/environment/project2-m2-par25")
import app

key = os.environ["KEY"]
KEY_INPUT = "data"
KEY_EXPECTED = "expected"


class UnmockedAppTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            # Tests to see if message works with the bot and its command
            {
                KEY_INPUT: {
                    "username": "test",
                    "message": "!!help",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: """Commands \n!!about --- About the chat bot itself 
                and what it translates \n!!help --> See all commands that this bot will 
                respond to \n!!funtranslate <insert text here>""",
            },
            {
                KEY_INPUT: {
                    "username": "test",
                    "message": "!!about",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: """Hello i am Cheunh bot, I translate your native tongue
                into a complex and dense tongue that is used in the Star Wars lore""",
            },
            {
                KEY_INPUT: {
                    "username": "pedro",
                    "message": "Hello world",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: "Hello world",
            },
            {
                KEY_INPUT: {
                    "username": "pedro",
                    "message": "!!helloo",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: "This command is not recognized my master... please try something else",
            },
            {
                KEY_INPUT: {
                    "username": "pedro",
                    "message": "!!abouttt",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: "This command is not recognized my master... please try something else",
            },
            {
                KEY_INPUT: {
                    "username": "pedro",
                    "message": "!!funntranslate",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: "This command is not recognized my master... please try something else",
            },
            {
                KEY_INPUT: {
                    "username": "pedro",
                    "message": "!!jooke",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: "This command is not recognized my master... please try something else",
            },
        ]
        self.failure_test_params = [
            {
                KEY_INPUT: {
                    "username": "pedro",
                    "message": "!!about",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: "This command is not recognized my master... please try something else",
            },
            {
                KEY_INPUT: {
                    "username": "pedro",
                    "message": "!!helpp",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: "Commands \n!!about --- About the chat bot itself and what it translates \n!!help --> See all commands that this bot will respond to \n!!funtranslate <insert text here>",
            },
            {
                KEY_INPUT: {
                    "username": "pedro",
                    "message": "Hello World",
                    "url": "https://avatarfiles.alphacoders.com/123/123561.png",
                },
                KEY_EXPECTED: "Commands \n!!about --- About the chat bot itself and what it translates \n!!help --> See all commands that this bot will respond to \n!!funtranslate <insert text here>",
            },
        ]

    def test_emit_all_oauth_users_success(self):
        for test in self.success_test_params:
            response = app.newMessageRecieved(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertEqual(response, expected)

    def test_emit_all_oauth_users_failure(self):
        for test in self.failure_test_params:
            response = app.newMessageRecieved(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertNotEqual(response, expected)


if __name__ == "__main__":
    unittest.main()
