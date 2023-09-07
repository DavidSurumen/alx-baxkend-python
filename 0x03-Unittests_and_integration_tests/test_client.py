#!/usr/bin/env python3
"""
Test module for github organisations client
"""
from client import (
    GithubOrgClient,
    get_json,
)
from unittest.mock import (
    patch,
    Mock,
    PropertyMock,
)
from parameterized import parameterized
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for GithubOrgClient class
    """
    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, test_org, test_payload, mock_get_json):
        """
        Test that org method returns dictionary of organisations.
        """
        object = GithubOrgClient(test_org)
        mock_get_json.return_value = test_payload
        self.assertTrue(isinstance(mock_get_json, Mock))

        result = object.org

        self.assertEqual(result, test_payload)

        org_url = object.ORG_URL.format(org=test_org)
        mock_get_json.assert_called_once_with(org_url)

    @parameterized.expand([
        ('this_org1', {'repos_url': {'payload': True}}),
    ])
    def test_public_repos_url(self, this_org1, test_payload):
        """
        doc
        """
        with patch('client.GithubOrgClient.org', new_callable = PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            self.assertTrue(isinstance(mock_org, Mock))

            result = GithubOrgClient(this_org1)._public_repos_url

        self.assertEqual(result, {'payload': True})
        mock_org.assert_called_once_with()