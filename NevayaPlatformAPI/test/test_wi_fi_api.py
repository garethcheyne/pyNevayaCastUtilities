# coding: utf-8

"""
    Nevaya Platform

    Access to everything Nevaya  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@nevaya.co.uk
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.wi_fi_api import WiFiApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWiFiApi(unittest.TestCase):
    """WiFiApi unit test stubs"""

    def setUp(self):
        self.api = WiFiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_tariffs(self):
        """Test case for get_tariffs

        Get the available tariffs  # noqa: E501
        """
        pass

    def test_post_wifi_vouchers(self):
        """Test case for post_wifi_vouchers

        Generate vouchers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
