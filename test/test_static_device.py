# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.10.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_client.models.static_device import StaticDevice

class TestStaticDevice(unittest.TestCase):
    """StaticDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StaticDevice:
        """Test StaticDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StaticDevice`
        """
        model = StaticDevice()
        if include_optional:
            return StaticDevice(
                name = '',
                token_set = [
                    authentik_client.models.static_device_token.StaticDeviceToken(
                        token = '', )
                    ],
                pk = 56
            )
        else:
            return StaticDevice(
                name = '',
                token_set = [
                    authentik_client.models.static_device_token.StaticDeviceToken(
                        token = '', )
                    ],
                pk = 56,
        )
        """

    def testStaticDevice(self):
        """Test StaticDevice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
