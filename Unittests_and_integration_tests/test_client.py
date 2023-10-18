#!/usr/bin/env python3
"""test_client"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class"""
    @patch('client.GithubOrgClient.get_json')
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    def test_org(self, org_name, expected_result):
        client = GithubOrgClient(org_name)

        client.get_json.return_value = expected_result

        result = client.org

        client.get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
